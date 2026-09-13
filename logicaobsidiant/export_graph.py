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
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                node_id = file[:-3] # Remove .md
                
                # Determine group based on the parent folder name
                group = os.path.basename(root)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                nodes.append({
                    "id": node_id,
                    "name": node_id,
                    "group": group,
                    "content": content
                })
                node_ids.add(node_id)
                
    # Step 2: Build edges
    for node in nodes:
        content = node["content"]
        links = link_pattern.findall(content)
        
        for link in links:
            # Clean up the link (e.g. removing anchors # if any, but let's keep it simple for now)
            target = link.split('#')[0].strip()
            
            # Optionally add target to nodes if it doesn't exist (unresolved links)
            # But let's only link existing nodes for a clean graph
            # Or we can add them to see broken links. Let's only add if exists.
            if target in node_ids:
                edges.append({
                    "source": node["id"],
                    "target": target
                })
                
    # Output the JSON
    graph_data = {
        "nodes": nodes,
        "links": edges
    }
    
    # Make sure output directory exists
    os.makedirs(os.path.dirname(output_json_path), exist_ok=True)
    
    with open(output_json_path, 'w', encoding='utf-8') as f:
        json.dump(graph_data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    vault_dir = "/Users/kostantinkrivula/Desktop/sqlbase/logica/logicaobsidiant/wiki"
    output_path = "/Users/kostantinkrivula/Desktop/sqlbase/lexisblog/assets/graph_data.json"
    parse_obsidian_vault(vault_dir, output_path)
    print(f"Graph data successfully exported to {output_path}")
