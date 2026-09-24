import os
import glob
import re

WIKI_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def lint_wiki():
    print("=== Запуск перевірки здоров'я Wiki (Wiki Lint) ===\n")
    wiki_files = glob.glob(os.path.join(WIKI_DIR, '**', '*.md'), recursive=True)
    all_names = set(os.path.splitext(os.path.basename(f))[0] for f in wiki_files)
    
    broken_links = []
    orphans = set(all_names) - {'index', 'AGENTS', 'SCHEMA', 'log', 'overview'}
    
    for wf in wiki_files:
        with open(wf, 'r', encoding='utf-8') as f:
            content = f.read()
        links = re.findall(r'\[\[([^\]\|]+)(?:\|[^\]]+)?\]\]', content)
        for target in links:
            target_clean = os.path.splitext(os.path.basename(target))[0]
            if target_clean in orphans:
                orphans.remove(target_clean)
            if target_clean not in all_names:
                broken_links.append((os.path.basename(wf), target))
                
    print(f"Всього сторінок у Wiki: {len(wiki_files)}")
    print(f"Непрацюючих посилань (Broken links): {len(broken_links)}")
    for src, tgt in broken_links[:5]:
        print(f"  ❌ {src} -> [[{tgt}]]")
        
    print(f"Ізольованих сторінок (Orphans): {len(orphans)}")
    for o in list(orphans)[:5]:
        print(f"  ⚠️ {o}")
        
    print("\nПеревірку здоров'я завершено!")

if __name__ == '__main__':
    lint_wiki()
