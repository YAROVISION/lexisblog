import os
import sys
import glob
import re

WIKI_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEGMENTS_DIR = os.path.join(os.path.dirname(WIKI_DIR), 'agents', 'segments')

def search_wiki(query):
    print(f"=== Пошук у LLM Wiki за запитом: '{query}' ===\n")
    keywords = query.lower().split()
    
    # 1. Search in Wiki pages
    wiki_files = glob.glob(os.path.join(WIKI_DIR, '**', '*.md'), recursive=True)
    wiki_results = []
    
    for wf in wiki_files:
        with open(wf, 'r', encoding='utf-8') as f:
            content = f.read()
        score = sum(content.lower().count(k) for k in keywords)
        if score > 0:
            rel = os.path.relpath(wf, WIKI_DIR)
            wiki_results.append((score, rel, wf))
            
    wiki_results.sort(key=lambda x: x[0], reverse=True)
    print("--- Результати у Wiki сторінках ---")
    for score, rel, path in wiki_results[:10]:
        print(f"  [{score} збігів] [[{rel}]]")
        
    # 2. Search in raw Segments
    seg_files = glob.glob(os.path.join(SEGMENTS_DIR, '**', '*.md'), recursive=True)
    seg_results = []
    for sf in seg_files:
        with open(sf, 'r', encoding='utf-8') as f:
            c = f.read()
        score = sum(c.lower().count(k) for k in keywords)
        if score > 0:
            rel = os.path.relpath(sf, SEGMENTS_DIR)
            seg_results.append((score, rel, sf))
            
    seg_results.sort(key=lambda x: x[0], reverse=True)
    print(f"\n--- Топ результатів у сегментах судової практики (всього {len(seg_results)} знайдено) ---")
    for score, rel, path in seg_results[:10]:
        print(f"  [{score} збігів] {rel}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        search_wiki(' '.join(sys.argv[1:]))
    else:
        print("Використання: python wiki_search.py <пошуковий запит>")
