import os
import re
import json

def parse_obsidian_vault(vault_path, output_json_path):
    nodes = []
    edges = []
    
    # Store existing nodes by their normalized id for quick lookup
    node_ids = set()

    # Regex to find obsidian links: [[Link]] or [[Link|Alias]]
    link_pattern = re.compile(r'\[\[(.*?)(?:\|.*?)?\]\]')

    # Step 1: Read all nodes
    for root, dirs, files in os.walk(vault_path):
        # Ignore Clippings and .obsidian directories
        if 'Clippings' in dirs:
            dirs.remove('Clippings')
        if '.obsidian' in dirs:
            dirs.remove('.obsidian')
            
        for file in files:
            if file in ['log.md', 'conventions.md']:
                continue
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                node_id = file[:-3] # Remove .md
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Determine group based on frontmatter or parent folder
                m_grp = re.search(r'^group:\s*([a-zA-Z0-9_-]+)', content, re.M)
                if m_grp:
                    group = m_grp.group(1).strip()
                else:
                    group = os.path.basename(root)
                    if group == "logicaobsidiant":
                        group = "root"
                    elif 'помилк' in node_id.lower() or 'fallac' in node_id.lower():
                        group = "fallacies"
                
                nodes.append({
                    "id": node_id,
                    "name": node_id,
                    "group": group,
                    "content": content
                })
                node_ids.add(node_id)
                
    # Create a mapping for case-insensitive lookup
    node_id_map = {nid.lower(): nid for nid in node_ids}
                
    # Step 2: Build edges
    for node in nodes:
        content = node["content"]
        links = link_pattern.findall(content)
        
        for link in links:
            # Clean up the link (handle alias and anchor)
            target = link.split('|')[0].split('#')[0].strip()
            
            # Case-insensitive lookup
            target_lower = target.lower()
            if target_lower in node_id_map:
                edges.append({
                    "source": node["id"],
                    "target": node_id_map[target_lower]
                })
                
    # Output the JSON
    graph_data = {
        "nodes": nodes,
        "links": edges
    }
    
    # Make sure output directory exists
    os.makedirs(os.path.dirname(output_json_path), exist_ok=True)
    
    with open(output_json_path, 'w', encoding='utf-8') as f:
        f.write("const GRAPH_DATA = ")
        json.dump(graph_data, f, ensure_ascii=False, indent=2)
        f.write(";")

if __name__ == "__main__":
    # Now script runs from lexisblog
    base_dir = os.path.dirname(os.path.abspath(__file__))
    vault_dir = os.path.join(base_dir, "logicaobsidiant") # changed from logicaobsidiant/wiki
    output_path = os.path.join(base_dir, "assets", "js", "graph_data.js")
    
    parse_obsidian_vault(vault_dir, output_path)
    print(f"Graph data successfully exported to {output_path}")
