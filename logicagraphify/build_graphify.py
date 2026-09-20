#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Graphify Knowledge Base Builder for Logic & Legal Argumentation
Transforms 482 clippings into a standalone Graphify knowledge graph vault.
"""

import os
import re
import json
import glob
import math
from collections import defaultdict, Counter

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CLIPPINGS_DIR = os.path.join(ROOT_DIR, "Clippings")
NODES_DIR = os.path.join(ROOT_DIR, "nodes")
CONCEPTS_DIR = os.path.join(NODES_DIR, "concepts")
FALLACIES_DIR = os.path.join(NODES_DIR, "fallacies")
RULES_DIR = os.path.join(NODES_DIR, "rules")
ENTITIES_DIR = os.path.join(NODES_DIR, "entities")

def clean_filename(name):
    cleaned = re.sub(r'[\\/*?:\"<>|]', '', name).strip()
    cleaned = re.sub(r'\s+', '_', cleaned)
    cleaned = re.sub(r'[\(\)\[\]\{\}]', '', cleaned)
    if len(cleaned) > 100:
        cleaned = cleaned[:100].strip('_')
    return cleaned

def parse_clipping(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    section = ""
    m_sec = re.search(r'розділ:\s*\"?([^\n\r\"]+)\"?', content)
    if m_sec:
        section = m_sec.group(1).strip()

    segment = ""
    m_seg = re.search(r'сегмент:\s*\"?([^\n\r\"]+)\"?', content)
    if m_seg:
        segment = m_seg.group(1).strip()

    h1 = ""
    m_h1 = re.search(r'^#\s+(.+)$', content, re.M)
    if m_h1:
        h1 = m_h1.group(1).strip()

    if not segment or "User Safety" in segment:
        m_num = re.search(r'(?:^|\n)(\d+\.\s+[^\n\.\!]+[\.\!]?)', content)
        if m_num:
            segment = m_num.group(1).strip()
        elif h1 and "User Safety" not in h1:
            segment = h1
        else:
            base = os.path.basename(file_path)[:-3]
            segment = base.replace('_', ' ')

    if not h1 or "User Safety" in h1:
        h1 = segment

    related = []
    rel_match = re.search(r'## Пов\'язані концепти(.*?)(?:$|\n##)', content, re.S)
    if rel_match:
        related = re.findall(r'\[\[(.*?)\]\]', rel_match.group(1))

    # Extract clean body text
    body = content
    if body.startswith('---'):
        parts = body.split('---', 2)
        if len(parts) >= 3:
            body = parts[2].strip()
    body = re.sub(r'## Пов\'язані концепти.*$', '', body, flags=re.S).strip()
    # Remove H1 if present at start
    body = re.sub(r'^#\s+[^\n]+\n+', '', body).strip()

    # Extract summary (first 2-3 sentences)
    sentences = re.split(r'(?<=[.!?])\s+', body)
    summary_sentences = [s.strip() for s in sentences if len(s.strip()) > 15 and not s.strip().startswith('**') and not s.strip().startswith('###')]
    summary = " ".join(summary_sentences[:3]) if summary_sentences else (body[:300] + "...")
    if len(summary) > 400:
        summary = summary[:400] + "..."

    folder_name = os.path.basename(os.path.dirname(file_path))
    rel_path = os.path.relpath(file_path, ROOT_DIR)

    return {
        "file_path": file_path,
        "rel_path": rel_path,
        "folder": folder_name,
        "section": section,
        "segment": segment,
        "h1": h1,
        "related": related,
        "body": body,
        "summary": summary
    }

def categorize_item(item):
    folder = item["folder"]
    sec = item["section"].lower()
    seg = item["segment"].lower()
    h1 = item["h1"].lower()

    domain = "general_logic"
    node_type = "concept"
    cluster = "General Logic"

    if folder == "attaking_json-segments":
        domain = "fallacy_theory"
        if "помилк" in sec or "fallac" in sec or "помилк" in seg or "fallac" in seg:
            node_type = "fallacy"
            cluster = "Fallacies & Faulty Reasoning (Damer)"
        elif "кодекс" in sec or "правил" in sec or "code" in sec or "principle" in sec:
            node_type = "rule"
            cluster = "Argumentation Principles & Ethics"
        else:
            node_type = "concept"
            cluster = "Damer Critical Thinking"

    elif folder == "douglas_json_segments":
        domain = "informal_logic"
        if "схем" in seg or "scheme" in seg or "правил" in seg:
            node_type = "rule"
            cluster = "Walton Argumentation Schemes"
        elif "помилк" in seg or "fallac" in seg or "ad hominem" in seg or "begging" in seg:
            node_type = "fallacy"
            cluster = "Pragmatic Fallacies (Walton)"
        else:
            node_type = "concept"
            cluster = "Dialogue Theory & Pragma-Dialectics"

    elif folder == "making_json_segments":
        domain = "legal_persuasion"
        if "правил" in seg or "rule" in seg or "канон" in seg or "порада" in seg or re.match(r'^\d+\.', seg):
            node_type = "rule"
            cluster = "Scalia & Garner Legal Persuasion"
        else:
            node_type = "concept"
            cluster = "Judicial Advocacy & Briefing"

    elif folder == "rulebook_json_segments":
        domain = "argumentation_rules"
        if "правило" in seg or "rule" in seg or re.match(r'^\d+\.', seg):
            node_type = "rule"
            cluster = "Weston Argumentation Rules"
        elif "помилк" in seg or "fallacy" in seg:
            node_type = "fallacy"
            cluster = "Weston Fallacies"
        else:
            node_type = "concept"
            cluster = "Argument Construction & Essays"

    elif folder == "scherbina_json_segments":
        domain = "legal_logic"
        node_type = "concept"
        cluster = "Scherbina Legal Hermeneutics & Abduction"

    elif folder == "theory_json_segments":
        domain = "legal_theory"
        node_type = "concept"
        cluster = "MacCormick Legal Reasoning & Justification"

    elif folder == "logica_json_segments":
        domain = "formal_logic"
        if "закон" in seg or "правил" in seg:
            node_type = "rule"
            cluster = "Formal Logic Laws & Rules"
        else:
            node_type = "concept"
            cluster = "Categorical Logic & Syllogistics"

    # Title extraction
    title = item["segment"]
    title = re.sub(r'^\d+\.\s*', '', title)
    title = re.sub(r'^segment_\d+(_[A-Za-z0-9]+)?_', '', title)
    title = title.replace('_', ' ').strip()
    if not title:
        title = item["h1"]

    node_id = clean_filename(title)
    if not node_id or len(node_id) < 2:
        node_id = clean_filename(os.path.basename(item["file_path"])[:-3])

    return {
        "id": node_id,
        "title": title,
        "type": node_type,
        "domain": domain,
        "cluster": cluster
    }

def main():
    print("Building Graphify Knowledge Base...")
    os.makedirs(CONCEPTS_DIR, exist_ok=True)
    os.makedirs(FALLACIES_DIR, exist_ok=True)
    os.makedirs(RULES_DIR, exist_ok=True)
    os.makedirs(ENTITIES_DIR, exist_ok=True)

    # 1. Parse all clippings
    all_clipping_files = glob.glob(os.path.join(CLIPPINGS_DIR, "**", "*.md"), recursive=True)
    print(f"Found {len(all_clipping_files)} clipping files.")

    clippings = []
    for cf in all_clipping_files:
        clippings.append(parse_clipping(cf))

    # 2. Build core nodes
    nodes_map = {}
    clipping_to_node = {}

    for c in clippings:
        meta = categorize_item(c)
        nid = meta["id"]
        
        # Ensure unique ID
        if nid in nodes_map and nodes_map[nid]["source_folder"] != c["folder"]:
            nid = f"{nid}_{meta['domain']}"
            meta["id"] = nid

        if nid not in nodes_map:
            nodes_map[nid] = {
                "id": nid,
                "title": meta["title"],
                "type": meta["type"],
                "domain": meta["domain"],
                "cluster": meta["cluster"],
                "sources": [c["rel_path"]],
                "source_folder": c["folder"],
                "summaries": [c["summary"]],
                "bodies": [c["body"]],
                "explicit_links": list(c["related"]),
                "sections": [c["section"]]
            }
        else:
            nodes_map[nid]["sources"].append(c["rel_path"])
            nodes_map[nid]["summaries"].append(c["summary"])
            nodes_map[nid]["bodies"].append(c["body"])
            nodes_map[nid]["explicit_links"].extend(c["related"])

        clipping_to_node[c["file_path"]] = nid

    # Add Essential Entity Nodes
    entities = [
        {
            "id": "Ніл_Маккормік_Neil_MacCormick",
            "title": "Ніл Маккормік (Neil MacCormick)",
            "type": "entity",
            "domain": "legal_theory",
            "cluster": "Legal Philosophers & Authors",
            "summary": "Шотландський правознавець і філософ права, автор інституційної теорії права, концепцій виправдання першого і другого порядків, універсалізації та консеквенціалістських аргументів.",
            "sources": ["logicagraphify/Clippings/theory_json_segments/segment_001_Title_and_Abstract.md"]
        },
        {
            "id": "Антонін_Скаліа_Antonin_Scalia",
            "title": "Антонін Скаліа (Antonin Scalia)",
            "type": "entity",
            "domain": "legal_persuasion",
            "cluster": "Legal Philosophers & Authors",
            "summary": "Суддя Верховного Суду США, провідний теоретик оригіналізму та текстового тлумачення, співавтор класичного посібника з судової аргументації 'Making Your Case'.",
            "sources": ["logicagraphify/Clippings/making_json_segments/segment_01_Title_and_Intro.md"]
        },
        {
            "id": "Браян_Гарнер_Bryan_Garner",
            "title": "Браян Гарнер (Bryan A. Garner)",
            "type": "entity",
            "domain": "legal_persuasion",
            "cluster": "Legal Philosophers & Authors",
            "summary": "Американський правознавець, головний редактор Black's Law Dictionary, експерт із юридичного письма та стилю процесуальних документів.",
            "sources": ["logicagraphify/Clippings/making_json_segments/segment_01_Title_and_Intro.md"]
        },
        {
            "id": "Дуглас_Волтон_Douglas_Walton",
            "title": "Дуглас Волтон (Douglas Walton)",
            "type": "entity",
            "domain": "informal_logic",
            "cluster": "Logic Theorists & Logicians",
            "summary": "Канадський філософ та логік, піонер теорії аргументаційних схем, прагма-діалектичного підходу до аналізу діалогів та неформальних логічних помилок.",
            "sources": ["logicagraphify/Clippings/douglas_json_segments/"]
        },
        {
            "id": "Т_Едвард_Деймер_T_Edward_Damer",
            "title": "Т. Едвард Деймер (T. Edward Damer)",
            "type": "entity",
            "domain": "fallacy_theory",
            "cluster": "Logic Theorists & Logicians",
            "summary": "Американський філософ, автор фундаментальної класифікації понад 60 логічних помилок та 12 етичних правил ведення раціональної дискусії ('Attacking Faulty Reasoning').",
            "sources": ["logicagraphify/Clippings/attaking_json-segments/"]
        },
        {
            "id": "Ентоні_Вестон_Anthony_Weston",
            "title": "Ентоні Вестон (Anthony Weston)",
            "type": "entity",
            "domain": "argumentation_rules",
            "cluster": "Logic Theorists & Logicians",
            "summary": "Американський професор філософії, автор 'A Rulebook for Arguments' — стислого практичного стандарту побудови сильних аргументів, аналогій та есеїв.",
            "sources": ["logicagraphify/Clippings/rulebook_json_segments/"]
        },
        {
            "id": "Олена_Щербина",
            "title": "Олена Щербина",
            "type": "entity",
            "domain": "legal_logic",
            "cluster": "Legal Philosophers & Authors",
            "summary": "Українська дослідниця логіки та філософії права, автор монографій про логіко-герменевтичний аналіз юридичної аргументації та абдукцію в правосудді.",
            "sources": ["logicagraphify/Clippings/scherbina_json_segments/"]
        },
        {
            "id": "Арістотель_Aristotle",
            "title": "Арістотель (Aristotle)",
            "type": "entity",
            "domain": "formal_logic",
            "cluster": "Foundational Classical Logic",
            "summary": "Батько формальної логіки, автор органону, силогістики, класичної теорії категорій та трьох базових законів мислення (тотожності, несуперечності, виключеного третього).",
            "sources": ["logicagraphify/Clippings/logica_json_segments/"]
        }
    ]

    for ent in entities:
        nodes_map[ent["id"]] = {
            "id": ent["id"],
            "title": ent["title"],
            "type": ent["type"],
            "domain": ent["domain"],
            "cluster": ent["cluster"],
            "sources": ent["sources"],
            "source_folder": "entities",
            "summaries": [ent["summary"]],
            "bodies": [ent["summary"]],
            "explicit_links": [],
            "sections": ["Entities"]
        }

    # 3. Establish Edges & Relationships with Confidence Ratings
    edges = []
    edge_keys = set()

    def add_edge(source, target, rel_type, confidence, rationale):
        if source == target or source not in nodes_map or target not in nodes_map:
            return
        key = (source, target, rel_type)
        if key not in edge_keys:
            edge_keys.add(key)
            edges.append({
                "source": source,
                "target": target,
                "type": rel_type,
                "confidence": confidence,
                "rationale": rationale
            })

    # (A) EXTRACTED: Explicit links from Clippings
    for nid, node in nodes_map.items():
        for link in node["explicit_links"]:
            clean_link = clean_filename(link)
            matched_id = None
            if clean_link in nodes_map:
                matched_id = clean_link
            else:
                for candidate_id in nodes_map:
                    if clean_link.lower() in candidate_id.lower() or candidate_id.lower() in clean_link.lower():
                        matched_id = candidate_id
                        break
            if matched_id:
                add_edge(nid, matched_id, "REFERENCES", "EXTRACTED", "Пряме посилання в тексті першоджерела")

    # Connect nodes to author entities
    for nid, node in nodes_map.items():
        domain = node["domain"]
        if domain == "legal_theory" and nid != "Ніл_Маккормік_Neil_MacCormick":
            add_edge(nid, "Ніл_Маккормік_Neil_MacCormick", "AUTHORED_BY", "EXTRACTED", "Концепція розроблена в працях Н. Маккорміка")
        elif domain == "legal_persuasion" and nid not in ["Антонін_Скаліа_Antonin_Scalia", "Браян_Гарнер_Bryan_Garner"]:
            add_edge(nid, "Антонін_Скаліа_Antonin_Scalia", "AUTHORED_BY", "EXTRACTED", "Правило викладено в посібнику Скаліа та Гарнера")
            add_edge(nid, "Браян_Гарнер_Bryan_Garner", "AUTHORED_BY", "EXTRACTED", "Правило викладено в посібнику Скаліа та Гарнера")
        elif domain == "fallacy_theory" and nid != "Т_Едвард_Деймер_T_Edward_Damer":
            add_edge(nid, "Т_Едвард_Деймер_T_Edward_Damer", "AUTHORED_BY", "EXTRACTED", "Систематизовано за кодифікацією Е. Деймера")
        elif domain == "informal_logic" and nid != "Дуглас_Волтон_Douglas_Walton":
            add_edge(nid, "Дуглас_Волтон_Douglas_Walton", "AUTHORED_BY", "EXTRACTED", "Теорія аргументації та діалогів Д. Волтона")
        elif domain == "argumentation_rules" and nid != "Ентоні_Вестон_Anthony_Weston":
            add_edge(nid, "Ентоні_Вестон_Anthony_Weston", "AUTHORED_BY", "EXTRACTED", "Правило аргументації за Е. Вестоном")
        elif domain == "legal_logic" and nid != "Олена_Щербина":
            add_edge(nid, "Олена_Щербина", "AUTHORED_BY", "EXTRACTED", "Дослідження логіки права О. Щербини")
        elif domain == "formal_logic" and nid != "Арістотель_Aristotle":
            add_edge(nid, "Арістотель_Aristotle", "FOUNDED_ON", "EXTRACTED", "Базується на класичних законах арістотелівської логіки")

    # (B) INFERRED: Semantic Cross-Domain Bridging Connections
    deductive_nodes = [nid for nid in nodes_map if "дедуктив" in nid.lower() or "силог" in nid.lower() or "deduct" in nid.lower()]
    legal_syllogism_nodes = [nid for nid in nodes_map if "юридич" in nid.lower() and "силог" in nid.lower()]

    for dn in deductive_nodes:
        for lsn in legal_syllogism_nodes:
            add_edge(lsn, dn, "APPLIED_IN", "INFERRED", "Трансформація загальної дедуктивної схеми в юридичний силогізм суду")

    # Connect Fallacies with Rules
    for nid, node in nodes_map.items():
        if node["type"] == "fallacy":
            title_clean = node["title"].lower()
            for r_id, r_node in nodes_map.items():
                if r_node["type"] == "rule":
                    if any(w in r_node["title"].lower() for w in ["аналог", "джерел", "авторит", "причин", "узагальн", "засновк"]) and any(w in title_clean for w in ["аналог", "джерел", "авторит", "причин", "узагальн", "засновк"]):
                        add_edge(nid, r_id, "VIOLATES_RULE", "INFERRED", "Ця логічна помилка є наслідком порушення відповідного правила побудови аргументу")

    # Connect Abduction with Fact-Finding
    abduction_nodes = [nid for nid in nodes_map if "абдукц" in nid.lower()]
    fact_nodes = [nid for nid in nodes_map if "факт" in nid.lower() or "доказ" in nid.lower()]
    for ab in abduction_nodes:
        for fn in fact_nodes[:5]:
            add_edge(ab, fn, "EVIDENTIARY_METHOD", "INFERRED", "Абдукція використовується для гіпотетичного реконструктивного виведення фактів справи")

    # (C) AMBIGUOUS: Theoretical Tensions
    formal_proof = [nid for nid in nodes_map if "доведення" in nid.lower() and nodes_map[nid]["domain"] == "formal_logic"]
    informal_persuasion = [nid for nid in nodes_map if ("перекон" in nid.lower() or "риторик" in nid.lower()) and nodes_map[nid]["domain"] in ["legal_persuasion", "legal_theory"]]
    for fp in formal_proof[:3]:
        for ip in informal_persuasion[:3]:
            add_edge(ip, fp, "THEORETICAL_TENSION", "AMBIGUOUS", "Розбіжність між формально-логічною істинністю та прагматичною переконливістю перед судовою колегією")

    # Compute Graph Metrics
    in_degree = Counter()
    out_degree = Counter()
    for e in edges:
        out_degree[e["source"]] += 1
        in_degree[e["target"]] += 1

    for nid in nodes_map:
        nodes_map[nid]["in_degree"] = in_degree[nid]
        nodes_map[nid]["out_degree"] = out_degree[nid]
        nodes_map[nid]["degree"] = in_degree[nid] + out_degree[nid]

    # Identify God Nodes
    sorted_nodes = sorted(nodes_map.values(), key=lambda x: x["degree"], reverse=True)
    god_nodes = sorted_nodes[:15]

    # Cluster Summary
    clusters = defaultdict(list)
    for n in nodes_map.values():
        clusters[n["cluster"]].append(n)

    confidence_dist = Counter(e["confidence"] for e in edges)
    type_dist = Counter(e["type"] for e in edges)

    print(f"Generated {len(nodes_map)} nodes and {len(edges)} typed relationship edges.")

    # 4. Generate Markdown Node Files
    for nid, node in nodes_map.items():
        if node["type"] == "fallacy":
            subfolder = FALLACIES_DIR
        elif node["type"] == "rule":
            subfolder = RULES_DIR
        elif node["type"] == "entity":
            subfolder = ENTITIES_DIR
        else:
            subfolder = CONCEPTS_DIR

        node_file = os.path.join(subfolder, f"{nid}.md")
        
        node_edges = [e for e in edges if e["source"] == nid]
        backlinks = [e for e in edges if e["target"] == nid]

        summary_text = "\n\n".join(node["summaries"])
        body_sample = node["bodies"][0] if node["bodies"] else ""
        if len(body_sample) > 1200:
            body_sample = body_sample[:1200] + "\n\n*(Повний текст див. у першоджерелах Clippings)*"

        sources_yaml = "\n".join([f'  - "{s}"' for s in node["sources"][:10]])

        relations_md = ""
        if node_edges:
            relations_md += "\n## Зв'язки в графі знань (Graphify Relations)\n\n"
            relations_md += "| Цільовий вузол | Відношення | Впевненість | Обґрунтування зв'язку |\n"
            relations_md += "|---|---|---|---|\n"
            for e in node_edges:
                target_title = nodes_map[e["target"]]["title"]
                relations_md += f"| [[{target_title}]] | `{e['type']}` | **`{e['confidence']}`** | {e['rationale']} |\n"

        backlinks_md = ""
        if backlinks:
            backlinks_md += "\n## Зворотні посилання (Backlinks)\n\n"
            for b in backlinks:
                source_title = nodes_map[b["source"]]["title"]
                backlinks_md += f"- ← [[{source_title}]] (`{b['type']}`, *{b['confidence']}*)\n"

        content = f"""---
id: "{nid}"
title: "{node['title']}"
type: "{node['type']}"
domain: "{node['domain']}"
cluster: "{node['cluster']}"
degree: {node['degree']}
sources:
{sources_yaml}
tags:
  - {node['domain']}
  - {node['type']}
---

# {node['title']}

> **Кластер:** {node['cluster']} | **Тип:** {node['type'].upper()} | **Зв'язність (Degree):** {node['degree']}

## Сутність та Визначення
{summary_text}

## Текстовий контекст
{body_sample}
{relations_md}
{backlinks_md}
---
*База знань Graphify • Створено на основі Clippings • Lexis Platform*
"""
        with open(node_file, 'w', encoding='utf-8') as f:
            f.write(content)

    # 5. Generate graph.json
    export_nodes = []
    for n in nodes_map.values():
        export_nodes.append({
            "id": n["id"],
            "title": n["title"],
            "type": n["type"],
            "domain": n["domain"],
            "cluster": n["cluster"],
            "degree": n["degree"],
            "sources": n["sources"],
            "summary": n["summaries"][0] if n["summaries"] else ""
        })

    graph_data = {
        "metadata": {
            "name": "Lexis Logic & Legal Reasoning Knowledge Graph",
            "version": "1.0.0-graphify",
            "generated_at": "2026-09-20",
            "total_nodes": len(export_nodes),
            "total_edges": len(edges),
            "confidence_stats": dict(confidence_dist),
            "type_stats": dict(type_dist)
        },
        "nodes": export_nodes,
        "edges": edges
    }

    graph_json_path = os.path.join(ROOT_DIR, "graph.json")
    with open(graph_json_path, 'w', encoding='utf-8') as f:
        json.dump(graph_data, f, ensure_ascii=False, indent=2)
    print(f"Exported graph.json to {graph_json_path}")

    # 6. Generate GRAPH_REPORT.md
    report_path = os.path.join(ROOT_DIR, "GRAPH_REPORT.md")
    report_content = f"""# GRAPH_REPORT: Топологічний аналіз бази знань Graphify

Цей звіт сформовано автоматизованим аналітичним модулем **Graphify** для оцінки структурної цілісності, кластеризації та семантичної щільності знань із 482 першоджерел логіки, судової аргументації та теорії права.

---

## 1. Загальні метрики графа

| Метрика | Значення | Опис |
|---|---|---|
| **Всього вузлів (Nodes)** | `{len(nodes_map)}` | Поняття, правила, логічні помилки, автори |
| **Всього ребер (Edges)** | `{len(edges)}` | Структуровані типізовані зв'язки |
| **Середня зв'язність (Avg Degree)** | `{(2 * len(edges) / max(1, len(nodes_map))):.2f}` | Середня кількість зв'язків на один вузол |
| **EXTRACTED зв'язки** | `{confidence_dist.get('EXTRACTED', 0)}` | Явні витяги з тексту та прямі авторські цитування |
| **INFERRED зв'язки** | `{confidence_dist.get('INFERRED', 0)}` | Міждисциплінарні семантичні висновки (між авторами) |
| **AMBIGUOUS зв'язки** | `{confidence_dist.get('AMBIGUOUS', 0)}` | Дискусійні теоретичні точки дотику |

---

## 2. Центральні вузли-хаби (God Nodes)

Вузли з найвищим показником **Degree Centrality** є фундаментальними опорними концептами всієї системи. Запити AI-агентів повинні стартувати з аналізу цих вузлів для збереження контексту:

| Ранг | Вузол / Концепт | Кластер | Тип | Зв'язність (Degree) |
|---|---|---|---|---|
"""
    for i, gn in enumerate(god_nodes, 1):
        report_content += f"| {i} | [[{gn['title']}]] | {gn['cluster']} | `{gn['type']}` | **{gn['degree']}** |\n"

    report_content += f"""
---

## 3. Кластери знань (Domain Clusters)

Граф структуровано на {len(clusters)} функціональних кластерів знань:

"""
    for cluster_name, c_nodes in clusters.items():
        avg_deg = sum(n["degree"] for n in c_nodes) / max(1, len(c_nodes))
        report_content += f"### ❖ {cluster_name} ({len(c_nodes)} вузлів, сер. зв'язність: {avg_deg:.1f})\n"
        sample_titles = [f"[[{n['title']}]]" for n in c_nodes[:6]]
        report_content += f"- **Ключові вузли:** {', '.join(sample_titles)}...\n"
        report_content += f"- **Першоджерела:** `{c_nodes[0]['source_folder']}`\n\n"

    report_content += """
---

## 4. Інструкція для AI-агентів (Agent Context Optimization)

1. **Мінімізація контекстного вікна:** Замість послідовного завантаження сотень сирих файлів кліпінгів, агент зчитує `GRAPH_REPORT.md` та `graph.json`.
2. **Маршрутизація запитів (Graph Traversal):**
   - Для питань з **судової аргументації**: починати з кластерів *Scalia & Garner Legal Persuasion* та *MacCormick Legal Reasoning*.
   - Для виявлення **помилок у процесуальних документах**: проходити через ребра `VIOLATES_RULE` між кластерами *Fallacies & Faulty Reasoning* та *Argumentation Principles*.
   - Для перевірки **доказової бази**: використовувати вузли *Абдукція в праві* та *Юридичний силогізм*.
3. **Оцінка надійності:** Враховувати рівні впевненості `EXTRACTED` як аксіоматичні, а `INFERRED` — як аргументативні гіпотези.
"""

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_content)
    print(f"Generated GRAPH_REPORT.md at {report_path}")

    # 7. Generate conventions.md
    conventions_path = os.path.join(ROOT_DIR, "conventions.md")
    conventions_content = """# Graphify Knowledge Base Conventions & Ontology

Цей документ фіксує стандарти онтології, типізації та навігації в базі знань **`logicagraphify/`**.

---

## 1. Специфікація каталогів
- **`Clippings/`**: Недоторканний шар 482 першоджерел (7 книг і праць з логіки та права).
- **`nodes/concepts/`**: Базові поняття формальної, неформальної та юридичної логіки.
- **`nodes/fallacies/`**: Систематизований каталог логічних помилок (Damer, Walton, Weston).
- **`nodes/rules/`**: Нормативні канони, правила аргументації, тлумачення та кодекси дискусій.
- **`nodes/entities/`**: Автори, філософи, школи права та ключові праці.

---

## 2. Онтологія ребер (Edge Types)
- **`AUTHORED_BY`**: Авторство концепту або правила.
- **`REFERENCES`**: Пряме цитування або перехресне посилання в тексті.
- **`APPLIED_IN`**: Застосування абстрактного логічного правила у правозастосовній практиці.
- **`VIOLATES_RULE`**: Порушення правила аргументації, що спричиняє логічну помилку.
- **`PREREQUISITE_FOR`**: Необхідна логічна передумова для висновку.
- **`EVIDENTIARY_METHOD`**: Метод встановлення фактів та доказування.
- **`THEORETICAL_TENSION`**: Відмінність між формальною правильністю та судовою риторикою.

---

## 3. Рівні впевненості (Confidence Labels)
- **`EXTRACTED`** (Зелений): Встановлено безпосередньо з тексту першоджерела.
- **`INFERRED`** (Синій/Блакитний): Логічний та семантичний висновок між різними теоріями/авторами.
- **`AMBIGUOUS`** (Жовтий/Помаранчевий): Дискусійні зв'язки, що залежать від філософської позиції.
"""
    with open(conventions_path, 'w', encoding='utf-8') as f:
        f.write(conventions_content)

    # 8. Generate index.md
    index_path = os.path.join(ROOT_DIR, "index.md")
    index_content = f"""# Lexis Graphify: Головний навігатор бази знань

База знань побудована за методом **Graphify** на основі 482 першоджерел логіки, юридичної аргументації та теорії права.

- 📊 **Звіт топології графа:** [GRAPH_REPORT.md](GRAPH_REPORT.md)
- 🌐 **Інтерактивний переглядач графа:** [graph.html](graph.html)
- ⚙️ **Машиночитаний граф:** [graph.json](graph.json)
- 📜 **Конвенції онтології:** [conventions.md](conventions.md)

---

## Топ-10 центральних хабів (God Nodes)

"""
    for gn in god_nodes[:10]:
        folder_sub = "concepts" if gn["type"] == "concept" else ("fallacies" if gn["type"] == "fallacy" else ("rules" if gn["type"] == "rule" else "entities"))
        index_content += f"- **[[{gn['title']}]]** (`nodes/{folder_sub}/{gn['id']}.md`) — зв'язність: **{gn['degree']}**, кластер: *{gn['cluster']}*\n"

    index_content += "\n---\n\n## Кластери бази знань\n\n"
    for cluster_name, c_nodes in clusters.items():
        index_content += f"### ❖ {cluster_name} ({len(c_nodes)} нод)\n"
        for n in c_nodes:
            folder_sub = "concepts" if n["type"] == "concept" else ("fallacies" if n["type"] == "fallacy" else ("rules" if n["type"] == "rule" else "entities"))
            index_content += f"- [[{n['title']}]] (`nodes/{folder_sub}/{n['id']}.md`)\n"
        index_content += "\n"

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_content)

    # 9. Generate interactive graph.html
    graph_html_path = os.path.join(ROOT_DIR, "graph.html")
    inlined_json_str = json.dumps(graph_data, ensure_ascii=False)

    graph_html_content = f"""<!DOCTYPE html>
<html lang="uk" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Lexis Graphify — Інтерактивний Граф Знань з Логіки та Права</title>
  <link rel="icon" type="image/svg+xml" href="../assets/images/favicon.svg">
  <style>
    :root {{
      --bg: #14110f;
      --surface: #24211e;
      --surface-hover: #34312d;
      --surface-border: #44403b;
      --text: #f3f3f4;
      --text-muted: #9e9a93;
      --accent: #1A6BFF;
      --teal: #00C2A8;
      --gold: #EFD146;
      --red: #FF5A5F;
      --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: var(--bg);
      color: var(--text);
      font-family: var(--font-sans);
      overflow: hidden;
      width: 100vw;
      height: 100vh;
      user-select: none;
      -webkit-user-select: none;
    }}
    #canvas {{
      display: block;
      width: 100vw;
      height: 100vh;
      cursor: grab;
      touch-action: none;
    }}
    #canvas:active {{
      cursor: grabbing;
    }}

    @keyframes slideInPanel {{
      from {{
        opacity: 0;
        transform: translateY(-16px) scale(0.97);
      }}
      to {{
        opacity: 1;
        transform: translateY(0) scale(1);
      }}
    }}

    @keyframes slideInLegend {{
      from {{
        opacity: 0;
        transform: translate(-50%, 16px) scale(0.97);
      }}
      to {{
        opacity: 1;
        transform: translate(-50%, 0) scale(1);
      }}
    }}

    @keyframes slideInControls {{
      from {{
        opacity: 0;
        transform: translateY(16px) scale(0.97);
      }}
      to {{
        opacity: 1;
        transform: translateY(0) scale(1);
      }}
    }}

    /* Top Left Control Panel */
    .panel {{
      position: absolute;
      top: 16px;
      left: 16px;
      background: rgba(36, 33, 30, 0.94);
      backdrop-filter: blur(16px);
      border: 1px solid var(--surface-border);
      border-radius: 14px;
      padding: 16px 18px;
      width: 320px;
      box-shadow: 0 16px 36px rgba(0,0,0,0.6);
      z-index: 10;
      pointer-events: auto;
      animation: slideInPanel 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }}
    .panel-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 6px;
    }}
    .panel-title {{
      font-size: 1.15rem;
      font-weight: 700;
      background: linear-gradient(135deg, #1A6BFF, #00C2A8);
      -webkit-background-clip: text;
      background-clip: text;
      -webkit-text-fill-color: transparent;
      letter-spacing: -0.02em;
    }}
    .panel-badge {{
      font-size: 0.68rem;
      padding: 2px 6px;
      background: rgba(26,107,255,0.15);
      border: 1px solid rgba(26,107,255,0.35);
      border-radius: 4px;
      color: #4A90D9;
      font-weight: 600;
    }}
    .panel-desc {{
      font-size: 0.78rem;
      color: var(--text-muted);
      line-height: 1.4;
      margin-bottom: 12px;
    }}
    .search-box {{
      width: 100%;
      padding: 8px 12px;
      background: #14110f;
      border: 1px solid var(--surface-border);
      border-radius: 8px;
      color: #fff;
      font-size: 0.85rem;
      outline: none;
      margin-bottom: 10px;
      transition: border-color 0.2s;
    }}
    .search-box:focus {{
      border-color: var(--accent);
    }}
    .filter-group {{
      display: flex;
      flex-wrap: wrap;
      gap: 5px;
      margin-bottom: 12px;
    }}
    .filter-btn {{
      padding: 4px 8px;
      border-radius: 6px;
      font-size: 0.72rem;
      font-weight: 500;
      cursor: pointer;
      border: 1px solid var(--surface-border);
      background: #14110f;
      color: var(--text-muted);
      transition: all 0.2s;
    }}
    .filter-btn:hover {{
      background: var(--surface-hover);
      color: #fff;
    }}
    .filter-btn.active {{
      background: rgba(26, 107, 255, 0.25);
      border-color: var(--accent);
      color: #fff;
      font-weight: 600;
    }}

    .stats-bar {{
      display: flex;
      justify-content: space-between;
      border-top: 1px solid rgba(255,255,255,0.06);
      padding-top: 8px;
      font-size: 0.72rem;
      color: var(--text-muted);
    }}

    /* Controls Bar (Zoom, Center) */
    .controls-bar {{
      position: absolute;
      bottom: 20px;
      left: 20px;
      display: flex;
      gap: 6px;
      background: rgba(36, 33, 30, 0.9);
      backdrop-filter: blur(12px);
      border: 1px solid var(--surface-border);
      border-radius: 8px;
      padding: 4px;
      z-index: 10;
      animation: slideInControls 0.9s cubic-bezier(0.16, 1, 0.3, 1) 0.25s both;
    }}
    .ctrl-btn {{
      background: #14110f;
      border: 1px solid var(--surface-border);
      color: var(--text);
      width: 32px;
      height: 32px;
      border-radius: 6px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1rem;
      transition: all 0.2s;
    }}
    .ctrl-btn:hover {{
      background: var(--surface-hover);
      border-color: var(--accent);
    }}

    /* Legend (Bottom Center) */
    .legend {{
      position: absolute;
      bottom: 20px;
      left: 50%;
      transform: translateX(-50%);
      background: rgba(36, 33, 30, 0.9);
      backdrop-filter: blur(12px);
      border: 1px solid var(--surface-border);
      border-radius: 8px;
      padding: 6px 14px;
      display: flex;
      gap: 14px;
      font-size: 0.72rem;
      color: var(--text-muted);
      z-index: 10;
      pointer-events: none;
      animation: slideInLegend 0.9s cubic-bezier(0.16, 1, 0.3, 1) 0.35s both;
    }}
    .legend-item {{
      display: flex;
      align-items: center;
      gap: 5px;
    }}
    .legend-dot {{
      width: 8px;
      height: 8px;
      border-radius: 50%;
    }}

    /* Floating Hover Tooltip */
    .hover-tooltip {{
      position: absolute;
      pointer-events: none;
      background: rgba(20, 17, 15, 0.94);
      backdrop-filter: blur(12px);
      border: 1px solid var(--accent);
      border-radius: 8px;
      padding: 8px 12px;
      max-width: 280px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.6);
      display: none;
      z-index: 30;
      transform: translate(-50%, -125%);
      transition: opacity 0.15s ease, transform 0.15s ease;
    }}
    .hover-tooltip .tt-title {{
      font-size: 0.85rem;
      font-weight: 700;
      color: #fff;
      margin-bottom: 3px;
    }}
    .hover-tooltip .tt-cluster {{
      font-size: 0.7rem;
      color: #4A90D9;
      font-weight: 500;
    }}

    /* Info Panel (Right) */
    .info-panel {{
      position: absolute;
      top: 16px;
      right: 16px;
      background: rgba(36, 33, 30, 0.96);
      backdrop-filter: blur(16px);
      border: 1px solid var(--surface-border);
      border-radius: 14px;
      padding: 20px;
      width: 380px;
      max-height: calc(100vh - 32px);
      overflow-y: auto;
      box-shadow: 0 16px 36px rgba(0,0,0,0.6);
      display: none;
      z-index: 20;
    }}
    .info-header {{
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 10px;
      margin-bottom: 8px;
    }}
    .info-title {{
      font-size: 1.15rem;
      font-weight: 700;
      color: #fff;
      line-height: 1.3;
    }}
    .close-btn {{
      background: transparent;
      border: none;
      color: var(--text-muted);
      font-size: 1.4rem;
      cursor: pointer;
      line-height: 1;
      padding: 0 4px;
    }}
    .close-btn:hover {{ color: #fff; }}
    .info-badge {{
      display: inline-block;
      padding: 3px 8px;
      border-radius: 4px;
      font-size: 0.7rem;
      font-weight: 600;
      margin-bottom: 12px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }}
    .badge-concept {{ background: rgba(0, 194, 168, 0.2); color: #00C2A8; border: 1px solid rgba(0, 194, 168, 0.4); }}
    .badge-fallacy {{ background: rgba(255, 90, 95, 0.2); color: #FF5A5F; border: 1px solid rgba(255, 90, 95, 0.4); }}
    .badge-rule {{ background: rgba(239, 209, 70, 0.2); color: #EFD146; border: 1px solid rgba(239, 209, 70, 0.4); }}
    .badge-entity {{ background: rgba(26, 107, 255, 0.2); color: #1A6BFF; border: 1px solid rgba(26, 107, 255, 0.4); }}
    
    .info-summary {{
      font-size: 0.84rem;
      line-height: 1.6;
      color: #d9c5b2;
      background: rgba(20, 17, 15, 0.6);
      border: 1px solid rgba(255,255,255,0.05);
      border-radius: 8px;
      padding: 10px 12px;
      margin-bottom: 16px;
    }}
    .info-sec-title {{
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--text-muted);
      margin: 14px 0 8px 0;
    }}
    .rel-list {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}
    .rel-item {{
      background: rgba(20, 17, 15, 0.5);
      border: 1px solid rgba(255,255,255,0.04);
      border-radius: 6px;
      padding: 7px 10px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      font-size: 0.78rem;
      cursor: pointer;
      transition: all 0.2s;
    }}
    .rel-item:hover {{
      border-color: rgba(26, 107, 255, 0.4);
      background: rgba(26, 107, 255, 0.1);
    }}
    .rel-name {{
      font-weight: 600;
      color: #fff;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }}
    .rel-type-tag {{
      font-size: 0.65rem;
      color: var(--text-muted);
      display: block;
    }}
    .rel-conf {{
      font-size: 0.62rem;
      font-weight: 700;
      padding: 2px 5px;
      border-radius: 3px;
      text-transform: uppercase;
      white-space: nowrap;
    }}
    .conf-EXTRACTED {{ background: rgba(0,194,168,0.15); color: #00C2A8; }}
    .conf-INFERRED {{ background: rgba(26,107,255,0.15); color: #1A6BFF; }}
    .conf-AMBIGUOUS {{ background: rgba(239,209,70,0.15); color: #EFD146; }}

    .open-doc-btn {{
      display: inline-block;
      margin-top: 14px;
      width: 100%;
      text-align: center;
      padding: 8px;
      background: rgba(26, 107, 255, 0.15);
      border: 1px solid rgba(26, 107, 255, 0.35);
      border-radius: 6px;
      color: #4A90D9;
      font-size: 0.78rem;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.2s;
    }}
    .open-doc-btn:hover {{
      background: rgba(26, 107, 255, 0.3);
      color: #fff;
    }}

    @media (max-width: 640px) {{
      .panel {{ width: calc(100vw - 32px); }}
      .info-panel {{ width: calc(100vw - 32px); }}
      .legend {{ display: none; }}
    }}
  </style>
</head>
<body>

  <!-- Control Panel -->
  <div class="panel">
    <div class="panel-header">
      <div class="panel-title">Lexis Graphify</div>
      <span class="panel-badge">KNOWLEDGE GRAPH</span>
    </div>
    <p class="panel-desc">Наведіть мишкою або торкніться пальцем, щоб побачити назву вузла.</p>
    
    <input type="text" id="search-input" class="search-box" placeholder="Пошук (напр. силогізм, Скаліа, помилка)..." autocomplete="off">
    
    <div class="filter-group">
      <button class="filter-btn active" data-type="all">Всі</button>
      <button class="filter-btn" data-type="concept">Концепти</button>
      <button class="filter-btn" data-type="fallacy">Помилки</button>
      <button class="filter-btn" data-type="rule">Правила</button>
      <button class="filter-btn" data-type="entity">Автори</button>
    </div>

    <div class="stats-bar">
      <span>Вузлів: <strong id="nodes-count" style="color:#fff">{len(export_nodes)}</strong></span>
      <span>Зв'язків: <strong id="edges-count" style="color:#fff">{len(edges)}</strong></span>
      <span>Зум: <strong id="zoom-val" style="color:#fff">100%</strong></span>
    </div>
  </div>

  <!-- Zoom and Center Controls -->
  <div class="controls-bar">
    <button class="ctrl-btn" id="zoom-in-btn" title="Збільшити">+</button>
    <button class="ctrl-btn" id="zoom-out-btn" title="Зменшити">&minus;</button>
    <button class="ctrl-btn" id="reset-btn" title="Скинути вигляд">&#8635;</button>
  </div>

  <!-- Legend -->
  <div class="legend">
    <div class="legend-item"><div class="legend-dot" style="background:#00C2A8"></div> Концепти</div>
    <div class="legend-item"><div class="legend-dot" style="background:#FF5A5F"></div> Помилки</div>
    <div class="legend-item"><div class="legend-dot" style="background:#EFD146"></div> Правила</div>
    <div class="legend-item"><div class="legend-dot" style="background:#1A6BFF"></div> Автори/Школи</div>
  </div>

  <!-- Floating Hover Tooltip -->
  <div id="hover-tooltip" class="hover-tooltip">
    <div class="tt-title" id="tt-title"></div>
    <div class="tt-cluster" id="tt-cluster"></div>
  </div>

  <!-- Node Inspector (Right) -->
  <div id="info-panel" class="info-panel">
    <div class="info-header">
      <h2 id="info-title" class="info-title"></h2>
      <button class="close-btn" id="close-info">&times;</button>
    </div>
    <span id="info-badge" class="info-badge"></span>
    <div id="info-summary" class="info-summary"></div>
    
    <div class="info-sec-title">Зв'язки в графі знань:</div>
    <ul id="info-rels" class="rel-list"></ul>

    <a id="info-file-link" href="#" class="open-doc-btn" target="_blank">Відкрити файл ноди Markdown &rarr;</a>
  </div>

  <!-- Canvas Visualizer -->
  <canvas id="canvas"></canvas>

  <script>
    // Inlined Graph Data (Works 100% Offline & File:// Protocol with NO CORS block!)
    const GRAPH_DATA = {inlined_json_str};

    // Visualization Engine
    (function() {{
      const canvas = document.getElementById('canvas');
      const ctx = canvas.getContext('2d');
      const infoPanel = document.getElementById('info-panel');
      const hoverTooltip = document.getElementById('hover-tooltip');
      const ttTitle = document.getElementById('tt-title');
      const ttCluster = document.getElementById('tt-cluster');
      const searchInput = document.getElementById('search-input');
      const filterBtns = document.querySelectorAll('.filter-btn');
      const zoomInBtn = document.getElementById('zoom-in-btn');
      const zoomOutBtn = document.getElementById('zoom-out-btn');
      const resetBtn = document.getElementById('reset-btn');
      const zoomValDisplay = document.getElementById('zoom-val');
      const nodesCountDisplay = document.getElementById('nodes-count');
      const edgesCountDisplay = document.getElementById('edges-count');

      let width = window.innerWidth || document.documentElement.clientWidth || 1920;
      let height = window.innerHeight || document.documentElement.clientHeight || 873;
      canvas.width = width * window.devicePixelRatio;
      canvas.height = height * window.devicePixelRatio;
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);

      function handleResize() {{
        width = window.innerWidth || document.documentElement.clientWidth || 1920;
        height = window.innerHeight || document.documentElement.clientHeight || 873;
        canvas.width = width * window.devicePixelRatio;
        canvas.height = height * window.devicePixelRatio;
        ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
        normalizeToScreen();
      }}

      window.addEventListener('resize', handleResize);

      // Embedded mode adjustments if loaded inside iframe
      try {{
        if (window.self !== window.top) {{
          document.body.classList.add('embedded-mode');
          const panel = document.querySelector('.panel');
          if (panel) {{
            panel.style.top = '155px';
          }}
          if (infoPanel) {{
            infoPanel.style.top = '155px';
            infoPanel.style.height = 'calc(100vh - 170px)';
          }}
        }}
      }} catch (err) {{}}

      window.addEventListener('message', (e) => {{
        if (!e.data) return;
        if (e.data.type === 'ACTIVATE' || e.data.type === 'RESIZE') {{
          handleResize();
          if (e.data.query !== undefined && searchInput) {{
            searchInput.value = e.data.query;
            searchTerm = (e.data.query || '').toLowerCase().trim();
            updateCounts();
          }}
        }} else if (e.data.type === 'SEARCH' && searchInput) {{
          searchInput.value = e.data.query || '';
          searchTerm = (e.data.query || '').toLowerCase().trim();
          updateCounts();
        }}
      }});

      const typeColors = {{
        concept: '#00C2A8',
        fallacy: '#FF5A5F',
        rule: '#EFD146',
        entity: '#1A6BFF'
      }};

      // Aspect ratio of the viewport to shape the knowledge base proportionally to screen dimensions
      const aspect = Math.max(0.6, Math.min(2.5, width / height));

      // Dynamic scale factor relative to reference 1920x873 screen baseline
      function getScreenScale() {{
        return Math.max(0.35, Math.min(2.5, Math.sqrt((width * height) / (1920 * 873))));
      }}

      // Build simulation model with screen-proportional initial distribution
      const nodeMap = new Map();
      const nodes = GRAPH_DATA.nodes.map((n, i) => {{
        const phi = i * 2.39996;
        const dist = Math.sqrt(i + 1) * 32;
        const baseR = Math.max(2.0, Math.min(8.0, Math.sqrt(n.degree || 1) * 1.5));
        const node = {{
          ...n,
          x: Math.cos(phi) * dist * Math.sqrt(aspect),
          y: (Math.sin(phi) * dist) / Math.sqrt(aspect),
          vx: 0,
          vy: 0,
          baseRadius: baseR,
          radius: baseR * getScreenScale(),
          color: typeColors[n.type] || '#7e7f83'
        }};
        nodeMap.set(node.id, node);
        return node;
      }});

      const links = GRAPH_DATA.edges.map(e => ({{
        source: nodeMap.get(e.source),
        target: nodeMap.get(e.target),
        type: e.type,
        confidence: e.confidence,
        rationale: e.rationale
      }})).filter(l => l.source && l.target);

      // Camera State (100% zoom as default full screen fit)
      let camera = {{
        x: width / 2,
        y: height / 2,
        zoom: 1.0
      }};

      let isDragging = false;
      let dragStart = {{ x: 0, y: 0 }};
      let draggedNode = null;
      let hoveredNode = null;
      let selectedNode = null;
      let searchTerm = '';
      let currentFilter = 'all';

      // Touch handling
      let touchStartTime = 0;
      let touchStartPos = {{ x: 0, y: 0 }};
      let touchStartDist = 0;

      // Physics Simulation (with strict minimum 2.5px gap collision prevention)
      let alpha = 1.0;
      const minGap = 2.5; // Minimum 2.5px gap between dot boundaries
      let k = 0.035;
      let repulsion = 450;
      let linkLength = 65;

      function tickPhysics() {{
        if (alpha > 0.001) {{
          alpha *= 0.99;
        }}

        // Repulsion + Strict Collision Prevention
        for (let i = 0; i < nodes.length; i++) {{
          const n1 = nodes[i];
          for (let j = i + 1; j < nodes.length; j++) {{
            const n2 = nodes[j];
            const dx = n2.x - n1.x;
            const dy = n2.y - n1.y;
            const distSq = dx * dx + dy * dy;
            const minDist = n1.radius + n2.radius + minGap;

            if (distSq < minDist * minDist) {{
              const dist = Math.sqrt(distSq) || 0.1;
              const overlap = (minDist - dist);
              const push = overlap * 0.2;
              const nx = dx / dist;
              const ny = dy / dist;
              if (n1 !== draggedNode) {{
                n1.vx -= nx * push;
                n1.vy -= ny * push;
              }}
              if (n2 !== draggedNode) {{
                n2.vx += nx * push;
                n2.vy += ny * push;
              }}
            }} else if (distSq < 160000 && alpha > 0.001) {{
              const dist = Math.sqrt(distSq);
              const force = (repulsion / distSq) * alpha;
              const fx = (dx / dist) * force;
              const fy = (dy / dist) * force;
              n1.vx -= fx;
              n1.vy -= fy;
              n2.vx += fx;
              n2.vy += fy;
            }}
          }}
        }}

        if (alpha > 0.001) {{
          for (let i = 0; i < links.length; i++) {{
            const link = links[i];
            const n1 = link.source;
            const n2 = link.target;
            const dx = n2.x - n1.x;
            const dy = n2.y - n1.y;
            const dist = Math.sqrt(dx * dx + dy * dy) || 1;
            const diff = (dist - linkLength) * k * alpha;
            const fx = (dx / dist) * diff;
            const fy = (dy / dist) * diff;
            n1.vx += fx;
            n1.vy += fy;
            n2.vx += fx;
            n2.vy += fy;
          }}

          // Gravity proportional to screen aspect ratio
          const curAspect = Math.max(0.6, Math.min(2.5, width / height));
          const baseGravity = 0.00055;
          const gravX = (baseGravity / curAspect) * alpha;
          const gravY = (baseGravity * curAspect) * alpha;

          for (let i = 0; i < nodes.length; i++) {{
            const n = nodes[i];
            if (n === draggedNode) continue;
            n.vx += (-n.x * gravX);
            n.vy += (-n.y * gravY);
            
            const speed = Math.sqrt(n.vx * n.vx + n.vy * n.vy);
            if (speed > 10) {{
              n.vx = (n.vx / speed) * 10;
              n.vy = (n.vy / speed) * 10;
            }}

            n.vx *= 0.85;
            n.vy *= 0.85;
            n.x += n.vx;
            n.y += n.vy;
          }}
        }}
      }}

      // Pre-simulate 140 ticks so graph naturally takes screen proportions
      for (let s = 0; s < 140; s++) {{
        tickPhysics();
      }}

      let animStartTime = performance.now();
      let isIntroAnimating = true;

      // Normalize all node positions so that at 100% zoom (1.0) the entire database fits on screen
      function normalizeToScreen(paddingX = 100, paddingY = 70) {{
        if (!nodes.length) return;
        const sScale = getScreenScale();
        for (let i = 0; i < nodes.length; i++) {{
          nodes[i].radius = nodes[i].baseRadius * sScale;
        }}

        let minX = Infinity, maxX = -Infinity;
        let minY = Infinity, maxY = -Infinity;
        for (let i = 0; i < nodes.length; i++) {{
          const n = nodes[i];
          const r = n.radius || 4;
          if (n.x - r < minX) minX = n.x - r;
          if (n.x + r > maxX) maxX = n.x + r;
          if (n.y - r < minY) minY = n.y - r;
          if (n.y + r > maxY) maxY = n.y + r;
        }}
        const graphWidth = (maxX - minX) || 100;
        const graphHeight = (maxY - minY) || 100;
        const centerX = (minX + maxX) / 2;
        const centerY = (minY + maxY) / 2;

        const availWidth = Math.max(200, width - paddingX * 2);
        const availHeight = Math.max(200, height - paddingY * 2);

        const scale = Math.min(availWidth / graphWidth, availHeight / graphHeight);

        for (let i = 0; i < nodes.length; i++) {{
          const n = nodes[i];
          n.targetX = (n.x - centerX) * scale;
          n.targetY = (n.y - centerY) * scale;
          n.vx = 0;
          n.vy = 0;
          if (!isIntroAnimating) {{
            n.x = n.targetX;
            n.y = n.targetY;
          }}
        }}

        // Freeze physics expansion so layout remains stable on screen
        alpha = 0;

        camera.x = width / 2;
        camera.y = height / 2;
        camera.zoom = 1.0;

        if (zoomValDisplay) {{
          zoomValDisplay.textContent = '100%';
        }}
      }}

      // Scale knowledge base so that 100% zoom perfectly fits the screen
      normalizeToScreen();

      // Number counter animation for header stats
      function animateCounter(element, start, end, duration) {{
        if (!element) return;
        const startTime = performance.now();
        function step(now) {{
          const progress = Math.min(1.0, (now - startTime) / duration);
          const ease = 1 - Math.pow(1 - progress, 3);
          const current = Math.round(start + (end - start) * ease);
          element.textContent = current;
          if (progress < 1.0) {{
            requestAnimationFrame(step);
          }}
        }}
        requestAnimationFrame(step);
      }}

      animateCounter(nodesCountDisplay, 0, nodes.length, 1200);
      animateCounter(edgesCountDisplay, 0, links.length, 1400);

      // Helper to draw rounded rectangle
      function drawRoundRect(ctx, x, y, width, height, radius) {{
        ctx.beginPath();
        ctx.moveTo(x + radius, y);
        ctx.lineTo(x + width - radius, y);
        ctx.quadraticCurveTo(x + width, y, x + width, y + radius);
        ctx.lineTo(x + width, y + height - radius);
        ctx.quadraticCurveTo(x + width, y + height, x + width - radius, y + height);
        ctx.lineTo(x + radius, y + height);
        ctx.quadraticCurveTo(x, y + height, x, y + height - radius);
        ctx.lineTo(x, y + radius);
        ctx.quadraticCurveTo(x, y, x + radius, y);
        ctx.closePath();
      }}

      // Render Loop
      function render() {{
        tickPhysics();

        // Constellation expansion entry animation
        if (isIntroAnimating) {{
          const now = performance.now();
          const elapsed = now - animStartTime;
          let allDone = true;

          const maxDist = (width / 2) || 1;
          for (let i = 0; i < nodes.length; i++) {{
            const n = nodes[i];
            const distRatio = Math.hypot(n.targetX, n.targetY) / maxDist;
            const nodeDelay = distRatio * 280;
            const t = Math.max(0, Math.min(1.0, (elapsed - nodeDelay) / 850));
            
            if (t < 1.0) allDone = false;
            
            const ease = t === 1.0 ? 1.0 : 1 - Math.pow(1 - t, 3.5);
            n.x = n.targetX * ease;
            n.y = n.targetY * ease;
            n.animProgress = ease;
          }}

          if (elapsed > 1400 && allDone) {{
            isIntroAnimating = false;
            for (let i = 0; i < nodes.length; i++) {{
              const n = nodes[i];
              n.x = n.targetX;
              n.y = n.targetY;
              n.animProgress = 1.0;
            }}
          }}
        }}

        ctx.clearRect(0, 0, width, height);

        ctx.save();
        ctx.translate(camera.x, camera.y);
        ctx.scale(camera.zoom, camera.zoom);

        function isNodeVisible(n) {{
          const matchType = currentFilter === 'all' || n.type === currentFilter;
          const matchSearch = !searchTerm || n.title.toLowerCase().includes(searchTerm) || (n.summary && n.summary.toLowerCase().includes(searchTerm));
          return matchType && matchSearch;
        }}

        const activeFocusNode = hoveredNode || selectedNode;
        const linkIntroAlpha = isIntroAnimating ? Math.min(1.0, Math.max(0, (performance.now() - animStartTime - 180) / 750)) : 1.0;

        // 1. Draw Links
        for (let i = 0; i < links.length; i++) {{
          const link = links[i];
          const n1 = link.source;
          const n2 = link.target;
          const v1 = isNodeVisible(n1);
          const v2 = isNodeVisible(n2);
          if (!v1 && !v2) continue;

          const isConnected = activeFocusNode && (n1 === activeFocusNode || n2 === activeFocusNode);
          
          ctx.beginPath();
          ctx.moveTo(n1.x, n1.y);
          ctx.lineTo(n2.x, n2.y);

          if (isConnected) {{
            ctx.strokeStyle = link.confidence === 'EXTRACTED' ? '#00C2A8' : (link.confidence === 'INFERRED' ? '#1A6BFF' : '#EFD146');
            ctx.lineWidth = 2.4;
            ctx.globalAlpha = 0.95 * linkIntroAlpha;
          }} else {{
            if (link.confidence === 'EXTRACTED') ctx.strokeStyle = 'rgba(0, 194, 168, 0.25)';
            else if (link.confidence === 'INFERRED') ctx.strokeStyle = 'rgba(26, 107, 255, 0.25)';
            else ctx.strokeStyle = 'rgba(239, 209, 70, 0.25)';
            ctx.lineWidth = (v1 && v2) ? 1.0 : 0.4;
            ctx.globalAlpha = (activeFocusNode ? 0.08 : ((v1 && v2) ? 0.5 : 0.12)) * linkIntroAlpha;
          }}
          ctx.stroke();
        }}
        ctx.globalAlpha = 1.0;

        // 2. Draw Nodes
        for (let i = 0; i < nodes.length; i++) {{
          const n = nodes[i];
          const visible = isNodeVisible(n);
          const isHovered = n === hoveredNode;
          const isSelected = n === selectedNode;
          const isNeighbor = activeFocusNode && activeFocusNode !== n && links.some(l => (l.source === activeFocusNode && l.target === n) || (l.target === activeFocusNode && l.source === n));

          ctx.save();
          ctx.beginPath();
          const nodeScale = (isIntroAnimating && n.animProgress !== undefined) ? n.animProgress : 1.0;
          const r = ((isSelected || isHovered) ? n.radius * 1.5 : (isNeighbor ? n.radius * 1.25 : n.radius)) * nodeScale;
          ctx.arc(n.x, n.y, Math.max(0.1, r), 0, Math.PI * 2);

          if (visible) {{
            ctx.fillStyle = n.color;
            if (activeFocusNode) {{
              ctx.globalAlpha = (isHovered || isSelected || isNeighbor) ? 1.0 : 0.2;
            }} else {{
              ctx.globalAlpha = 0.9;
            }}

            if (isHovered || isSelected) {{
              ctx.shadowColor = n.color;
              ctx.shadowBlur = 20;
            }} else if (isNeighbor) {{
              ctx.shadowColor = n.color;
              ctx.shadowBlur = 10;
            }}
          }} else {{
            ctx.fillStyle = '#44403b';
            ctx.globalAlpha = 0.15;
          }}
          ctx.fill();

          if (isSelected || isHovered) {{
            ctx.strokeStyle = '#fff';
            ctx.lineWidth = 2.0;
            ctx.stroke();
          }} else if (isNeighbor) {{
            ctx.strokeStyle = 'rgba(255,255,255,0.7)';
            ctx.lineWidth = 1.2;
            ctx.stroke();
          }}
          ctx.restore();
        }}

        // 3. Draw Labels EXCLUSIVELY upon Hover, Tap/Selection, or Direct Neighbors (Clean graph by default!)
        if (activeFocusNode && isNodeVisible(activeFocusNode)) {{
          const focusNeighbors = nodes.filter(n => activeFocusNode !== n && links.some(l => (l.source === activeFocusNode && l.target === n) || (l.target === activeFocusNode && l.source === n)));

          // Draw neighbor labels first (subtle pills)
          focusNeighbors.forEach(nb => {{
            if (!isNodeVisible(nb)) return;
            const labelText = nb.title;
            ctx.font = '500 11px var(--font-sans)';
            const textMetrics = ctx.measureText(labelText);
            const paddingX = 7;
            const paddingY = 4;
            const boxW = textMetrics.width + paddingX * 2;
            const boxH = 18;
            const boxX = nb.x - boxW / 2;
            const boxY = nb.y + nb.radius + 6;

            ctx.save();
            ctx.fillStyle = 'rgba(20, 17, 15, 0.88)';
            ctx.strokeStyle = 'rgba(126, 127, 131, 0.4)';
            ctx.lineWidth = 1;
            drawRoundRect(ctx, boxX, boxY, boxW, boxH, 4);
            ctx.fill();
            ctx.stroke();

            ctx.fillStyle = '#d9c5b2';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText(labelText, nb.x, boxY + boxH / 2);
            ctx.restore();
          }});

          // Draw the primary hovered / selected node label (prominent highlighted badge)
          const primaryText = activeFocusNode.title;
          ctx.save();
          ctx.font = 'bold 13px var(--font-sans)';
          const textMetrics = ctx.measureText(primaryText);
          const paddingX = 10;
          const paddingY = 6;
          const boxW = textMetrics.width + paddingX * 2;
          const boxH = 24;
          const boxX = activeFocusNode.x - boxW / 2;
          const boxY = activeFocusNode.y - activeFocusNode.radius - boxH - 8;

          ctx.fillStyle = 'rgba(20, 17, 15, 0.96)';
          ctx.strokeStyle = activeFocusNode.color;
          ctx.lineWidth = 2;
          ctx.shadowColor = activeFocusNode.color;
          ctx.shadowBlur = 12;
          drawRoundRect(ctx, boxX, boxY, boxW, boxH, 6);
          ctx.fill();
          ctx.stroke();

          ctx.fillStyle = '#ffffff';
          ctx.textAlign = 'center';
          ctx.textBaseline = 'middle';
          ctx.fillText(primaryText, activeFocusNode.x, boxY + boxH / 2);
          ctx.restore();
        }}

        ctx.restore();
        requestAnimationFrame(render);
      }}
      requestAnimationFrame(render);

      // Coordinate Helper
      function screenToWorld(sx, sy) {{
        return {{
          x: (sx - camera.x) / camera.zoom,
          y: (sy - camera.y) / camera.zoom
        }};
      }}

      function worldToScreen(wx, wy) {{
        return {{
          x: wx * camera.zoom + camera.x,
          y: wy * camera.zoom + camera.y
        }};
      }}

      function getNodeAt(sx, sy) {{
        const w = screenToWorld(sx, sy);
        for (let i = nodes.length - 1; i >= 0; i--) {{
          const n = nodes[i];
          const dx = n.x - w.x;
          const dy = n.y - w.y;
          if (dx * dx + dy * dy <= (n.radius + 8) * (n.radius + 8)) {{
            return n;
          }}
        }}
        return null;
      }}

      // Floating HTML Tooltip update
      function updateHoverTooltip(node, screenX, screenY) {{
        if (!node) {{
          hoverTooltip.style.display = 'none';
          return;
        }}
        ttTitle.textContent = node.title;
        ttCluster.textContent = node.type.toUpperCase() + " • " + node.cluster + " • зв'язків: " + node.degree;
        hoverTooltip.style.borderColor = node.color;
        hoverTooltip.style.display = 'block';
        hoverTooltip.style.left = screenX + 'px';
        hoverTooltip.style.top = (screenY - 14) + 'px';
      }}

      // Mouse Interactivity
      canvas.addEventListener('mousedown', (e) => {{
        const node = getNodeAt(e.clientX, e.clientY);
        if (node) {{
          draggedNode = node;
          hoveredNode = node;
        }} else {{
          isDragging = true;
          dragStart = {{ x: e.clientX - camera.x, y: e.clientY - camera.y }};
        }}
      }});

      window.addEventListener('mousemove', (e) => {{
        if (draggedNode) {{
          const w = screenToWorld(e.clientX, e.clientY);
          draggedNode.x = w.x;
          draggedNode.y = w.y;
          draggedNode.vx = 0;
          draggedNode.vy = 0;
          updateHoverTooltip(draggedNode, e.clientX, e.clientY);
        }} else if (isDragging) {{
          camera.x = e.clientX - dragStart.x;
          camera.y = e.clientY - dragStart.y;
          updateHoverTooltip(null);
        }} else {{
          const node = getNodeAt(e.clientX, e.clientY);
          if (node !== hoveredNode) {{
            hoveredNode = node;
            canvas.style.cursor = hoveredNode ? 'pointer' : 'grab';
          }}
          if (hoveredNode) {{
            const screenPos = worldToScreen(hoveredNode.x, hoveredNode.y);
            updateHoverTooltip(hoveredNode, screenPos.x, screenPos.y);
          }} else {{
            updateHoverTooltip(null);
          }}
        }}
      }});

      window.addEventListener('mouseup', (e) => {{
        if (draggedNode) {{
          draggedNode = null;
        }}
        isDragging = false;
      }});

      canvas.addEventListener('wheel', (e) => {{
        e.preventDefault();
        const zoomFactor = e.deltaY < 0 ? 1.12 : 0.89;
        const newZoom = Math.max(0.02, Math.min(5.0, camera.zoom * zoomFactor));
        
        const mouseWorld = screenToWorld(e.clientX, e.clientY);
        camera.zoom = newZoom;
        camera.x = e.clientX - mouseWorld.x * camera.zoom;
        camera.y = e.clientY - mouseWorld.y * camera.zoom;
        zoomValDisplay.textContent = Math.round(camera.zoom * 100) + '%';
        if (hoveredNode) {{
          const screenPos = worldToScreen(hoveredNode.x, hoveredNode.y);
          updateHoverTooltip(hoveredNode, screenPos.x, screenPos.y);
        }}
      }});

      // Click / Tap Selection
      canvas.addEventListener('click', (e) => {{
        const node = getNodeAt(e.clientX, e.clientY);
        if (node) {{
          selectNode(node);
        }} else {{
          selectedNode = null;
          infoPanel.style.display = 'none';
          updateHoverTooltip(null);
        }}
      }});

      // Touch Events for Mobile / Tablet Tap & Pan
      canvas.addEventListener('touchstart', (e) => {{
        if (e.touches.length === 1) {{
          const touch = e.touches[0];
          touchStartTime = Date.now();
          touchStartPos = {{ x: touch.clientX, y: touch.clientY }};
          dragStart = {{ x: touch.clientX - camera.x, y: touch.clientY - camera.y }};
          
          const node = getNodeAt(touch.clientX, touch.clientY);
          if (node) {{
            draggedNode = node;
            hoveredNode = node;
          }} else {{
            isDragging = true;
          }}
        }} else if (e.touches.length === 2) {{
          const dx = e.touches[0].clientX - e.touches[1].clientX;
          const dy = e.touches[0].clientY - e.touches[1].clientY;
          touchStartDist = Math.sqrt(dx * dx + dy * dy);
        }}
      }}, {{ passive: false }});

      canvas.addEventListener('touchmove', (e) => {{
        e.preventDefault();
        if (e.touches.length === 1) {{
          const touch = e.touches[0];
          if (draggedNode) {{
            const w = screenToWorld(touch.clientX, touch.clientY);
            draggedNode.x = w.x;
            draggedNode.y = w.y;
          }} else if (isDragging) {{
            camera.x = touch.clientX - dragStart.x;
            camera.y = touch.clientY - dragStart.y;
          }}
        }} else if (e.touches.length === 2) {{
          const dx = e.touches[0].clientX - e.touches[1].clientX;
          const dy = e.touches[0].clientY - e.touches[1].clientY;
          const dist = Math.sqrt(dx * dx + dy * dy);
          if (touchStartDist > 0) {{
            const factor = dist / touchStartDist;
            camera.zoom = Math.max(0.02, Math.min(5.0, camera.zoom * factor));
            zoomValDisplay.textContent = Math.round(camera.zoom * 100) + '%';
            touchStartDist = dist;
          }}
        }}
      }}, {{ passive: false }});

      canvas.addEventListener('touchend', (e) => {{
        const duration = Date.now() - touchStartTime;
        if (e.changedTouches.length === 1 && duration < 300) {{
          const touch = e.changedTouches[0];
          const dist = Math.hypot(touch.clientX - touchStartPos.x, touch.clientY - touchStartPos.y);
          if (dist < 12) {{
            // Single Tap detected!
            const node = getNodeAt(touch.clientX, touch.clientY);
            if (node) {{
              hoveredNode = node;
              selectNode(node);
              const screenPos = worldToScreen(node.x, node.y);
              updateHoverTooltip(node, screenPos.x, screenPos.y);
            }} else {{
              selectedNode = null;
              hoveredNode = null;
              infoPanel.style.display = 'none';
              updateHoverTooltip(null);
            }}
          }}
        }}
        draggedNode = null;
        isDragging = false;
        touchStartDist = 0;
      }});

      function selectNode(node) {{
        selectedNode = node;
        hoveredNode = node;
        infoPanel.style.display = 'block';
        document.getElementById('info-title').textContent = node.title;
        const badge = document.getElementById('info-badge');
        badge.className = 'info-badge badge-' + node.type;
        badge.textContent = node.type + ' • ' + node.cluster;
        document.getElementById('info-summary').textContent = node.summary || 'Опис відсутній.';

        // Link to file
        const fileLink = document.getElementById('info-file-link');
        const folder = node.type === 'concept' ? 'concepts' : (node.type === 'fallacy' ? 'fallacies' : (node.type === 'rule' ? 'rules' : 'entities'));
        fileLink.href = 'nodes/' + folder + '/' + node.id + '.md';

        // Populate Relations
        const relList = document.getElementById('info-rels');
        relList.innerHTML = '';
        const connectedLinks = links.filter(l => l.source === node || l.target === node);

        connectedLinks.slice(0, 16).forEach(l => {{
          const isOut = l.source === node;
          const other = isOut ? l.target : l.source;
          const li = document.createElement('li');
          li.className = 'rel-item';
          li.innerHTML = `
            <div style="overflow:hidden">
              <span class="rel-name">${{isOut ? '→' : '←'}} ${{other.title}}</span>
              <span class="rel-type-tag">${{l.type}}</span>
            </div>
            <span class="rel-conf conf-${{l.confidence}}">${{l.confidence}}</span>
          `;
          li.onclick = () => {{
            selectNode(other);
            centerOnNode(other);
          }};
          relList.appendChild(li);
        }});
      }}

      function centerOnNode(node) {{
        camera.x = width / 2 - node.x * camera.zoom;
        camera.y = height / 2 - node.y * camera.zoom;
      }}

      document.getElementById('close-info').onclick = () => {{
        infoPanel.style.display = 'none';
        selectedNode = null;
        hoveredNode = null;
        updateHoverTooltip(null);
      }};

      // Search & Filters
      searchInput.addEventListener('input', (e) => {{
        searchTerm = e.target.value.toLowerCase().trim();
        updateCounts();
        if (searchTerm) {{
          const match = nodes.find(n => n.title.toLowerCase().includes(searchTerm));
          if (match) {{
            hoveredNode = match;
            centerOnNode(match);
          }}
        }}
      }});

      filterBtns.forEach(btn => {{
        btn.addEventListener('click', () => {{
          filterBtns.forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          currentFilter = btn.dataset.type;
          updateCounts();
        }});
      }});

      function updateCounts() {{
        const count = nodes.filter(n => (currentFilter === 'all' || n.type === currentFilter) && (!searchTerm || n.title.toLowerCase().includes(searchTerm))).length;
        nodesCountDisplay.textContent = count;
      }}

      // Controls
      zoomInBtn.onclick = () => {{
        camera.zoom = Math.min(5.0, camera.zoom * 1.25);
        zoomValDisplay.textContent = Math.round(camera.zoom * 100) + '%';
      }};
      zoomOutBtn.onclick = () => {{
        camera.zoom = Math.max(0.02, camera.zoom / 1.25);
        zoomValDisplay.textContent = Math.round(camera.zoom * 100) + '%';
      }};
      resetBtn.onclick = () => {{
        camera.x = width / 2;
        camera.y = height / 2;
        camera.zoom = 1.0;
        zoomValDisplay.textContent = '100%';
        alpha = 0.2;
        hoveredNode = null;
        selectedNode = null;
        infoPanel.style.display = 'none';
        updateHoverTooltip(null);
      }};
    }})();
  </script>
</body>
</html>
"""
    with open(graph_html_path, 'w', encoding='utf-8') as f:
        f.write(graph_html_content)
    print(f"Generated standalone interactive graph visualizer at {graph_html_path}")

    print("\n✅ Build Graphify completed successfully!")

if __name__ == "__main__":
    main()
