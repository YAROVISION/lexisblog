import os
import re
import json
import time

def parse_digest_vault(vault_path, output_json_path):
    t0 = time.time()
    nodes = []
    edges = []
    
    node_lookup = {} # maps various representations to canonical node id

    # Regex to find obsidian links: [[Link]] or [[Link|Alias]]
    link_pattern = re.compile(r'\[\[(.*?)(?:\|.*?)?\]\]')
    # Regex for title in frontmatter
    title_pattern = re.compile(r'^title:\s*["\']?([^"\'\n\r]+)["\']?$', re.M)
    category_pattern = re.compile(r'^category:\s*(.+)$', re.M)
    digest_pattern = re.compile(r'^digest:\s*(.+)$', re.M)

    # Step 1: Read all nodes
    for root, dirs, files in os.walk(vault_path):
        if 'Clippings' in dirs:
            dirs.remove('Clippings')
        if '.obsidian' in dirs:
            dirs.remove('.obsidian')
        if 'tools' in dirs:
            dirs.remove('tools')
            
        for file in files:
            if file in ['log.md', 'SCHEMA.md', 'AGENTS.md']:
                # Skip maintenance meta files if desired or keep
                pass
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, vault_path).replace('\\', '/')
                file_stem = file[:-3] # without .md
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Determine folder name / group
                if rel_path.startswith('segments/'):
                    group = "segments"
                    node_id = rel_path[:-3] # e.g. segments/Daidzhest_VP_2025/01.1_segment
                elif rel_path.startswith('entities/'):
                    group = "entities"
                    node_id = file_stem
                elif rel_path.startswith('concepts/'):
                    group = "concepts"
                    node_id = file_stem
                elif rel_path.startswith('sources/'):
                    group = "sources"
                    node_id = file_stem if file_stem != 'index' else 'sources_index'
                else:
                    group = "root"
                    node_id = file_stem

                # Check title from frontmatter or first heading
                title_match = title_pattern.search(content)
                h1_match = re.search(r'^#\s+(.+)$', content, re.M)
                h3_match = re.search(r'^###\s+(.+)$', content, re.M)
                
                if title_match:
                    display_name = title_match.group(1).strip().strip('"\'')
                elif h1_match:
                    display_name = h1_match.group(1).strip()
                elif h3_match:
                    display_name = h3_match.group(1).strip()
                else:
                    display_name = file_stem.replace('_', ' ')

                # Check category from frontmatter
                cat_match = category_pattern.search(content)
                category = cat_match.group(1).strip() if cat_match else group

                # Check digest
                digest_match = digest_pattern.search(content)
                digest_val = digest_match.group(1).strip() if digest_match else ""

                node_obj = {
                    "id": node_id,
                    "name": display_name,
                    "group": group,
                    "category": category,
                    "digest": digest_val,
                    "rel_path": rel_path,
                    "content": content
                }
                nodes.append(node_obj)

                # Register mappings in lookup
                node_lookup[node_id.lower()] = node_id
                node_lookup[file_stem.lower()] = node_id
                node_lookup[rel_path[:-3].lower()] = node_id
                node_lookup[rel_path.lower()] = node_id
                if '/' in rel_path:
                    # e.g. sources/Daidzhest_VP_2025 -> node_id
                    node_lookup[os.path.basename(rel_path)[:-3].lower()] = node_id

    # Step 2: Build edges
    existing_edges = set()
    for node in nodes:
        content = node["content"]
        links = link_pattern.findall(content)
        
        for link in links:
            clean_link = link.split('|')[0].split('#')[0].strip().replace('\\', '/')
            if not clean_link:
                continue
            
            clean_lower = clean_link.lower()
            target_id = None
            if clean_lower in node_lookup:
                target_id = node_lookup[clean_lower]
            else:
                base_target = os.path.basename(clean_link).replace('.md', '').lower()
                if base_target in node_lookup:
                    target_id = node_lookup[base_target]

            if target_id and target_id != node["id"]:
                edge_key = (node["id"], target_id)
                if edge_key not in existing_edges:
                    existing_edges.add(edge_key)
                    edges.append({
                        "source": node["id"],
                        "target": target_id
                    })

    graph_data = {
        "nodes": nodes,
        "links": edges
    }

    os.makedirs(os.path.dirname(output_json_path), exist_ok=True)
    with open(output_json_path, 'w', encoding='utf-8') as f:
        f.write("const DIGEST_GRAPH_DATA = ")
        json.dump(graph_data, f, ensure_ascii=False, separators=(',', ':'))
        f.write(";\n")

    t1 = time.time()
    print(f"Exported {len(nodes)} nodes and {len(edges)} links to {output_json_path} in {t1 - t0:.2f}s")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    vault_dir = os.path.join(base_dir, "digestobsidiant")
    output_path = os.path.join(base_dir, "assets", "js", "digest_graph_data.js")
    parse_digest_vault(vault_dir, output_path)
