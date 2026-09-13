import os

workspace = "/Users/kostantinkrivula/Desktop/sqlbase/logica/logicaobsidiant"
concepts_dir = os.path.join(workspace, "wiki", "concepts")
clippings_dir = os.path.join(workspace, "Clippings")

# Load all concepts
concepts = {}
for file in os.listdir(concepts_dir):
    if file.endswith('.md'):
        concept_name = file[:-3]
        filepath = os.path.join(concepts_dir, file)
        with open(filepath, 'r', encoding='utf-8') as f:
            concepts[concept_name] = f.read()

# Gather all clipping files
clipping_files = []
for root, dirs, files in os.walk(clippings_dir):
    for file in files:
        if file.endswith('.md'):
            clipping_files.append(os.path.join(root, file))

modified_count = 0

for clip_path in clipping_files:
    basename = os.path.basename(clip_path)
    # Find which concepts contain this basename
    linked_concepts = []
    for c_name, c_text in concepts.items():
        if basename in c_text:
            linked_concepts.append(c_name)
    
    if linked_concepts:
        # Check if the clip already has "## Пов'язані концепти" to avoid duplicates if run multiple times
        with open(clip_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if "## Пов'язані концепти" not in content:
            # Append backlinks
            backlinks = "\n\n---\n## Пов'язані концепти\n"
            for lc in sorted(linked_concepts):
                backlinks += f"- [[{lc}]]\n"
            
            with open(clip_path, 'a', encoding='utf-8') as f:
                f.write(backlinks)
            modified_count += 1

print(f"Added backlinks to {modified_count} clipping files.")
