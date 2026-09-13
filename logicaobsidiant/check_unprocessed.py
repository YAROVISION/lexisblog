import os
import glob

workspace_dir = "/Users/kostantinkrivula/Desktop/sqlbase/logica/logicaobsidiant"
clippings_dir = os.path.join(workspace_dir, "Clippings")
concepts_dir = os.path.join(workspace_dir, "wiki", "concepts")
log_file = os.path.join(workspace_dir, "log.md")

# 1. Get all clipping files
clipping_files = []
for root, dirs, files in os.walk(clippings_dir):
    for f in files:
        if f.endswith(".md"):
            clipping_files.append(os.path.join(root, f))

# 2. Gather text to search in
with open(log_file, 'r', encoding='utf-8') as f:
    log_text = f.read()

concept_texts = []
for f in glob.glob(os.path.join(concepts_dir, "*.md")):
    with open(f, 'r', encoding='utf-8') as cf:
        concept_texts.append(cf.read())
combined_concepts = "\n".join(concept_texts)

# 3. Check each file
unprocessed = []
for filepath in clipping_files:
    basename = os.path.basename(filepath)
    if basename not in log_text and basename not in combined_concepts:
        unprocessed.append(filepath)

print(f"Total clipping files: {len(clipping_files)}")
print(f"Total unprocessed files: {len(unprocessed)}")
for u in sorted(unprocessed):
    print(u)
