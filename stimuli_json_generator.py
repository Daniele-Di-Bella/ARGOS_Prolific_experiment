import os
import json

BASE_DIR = './experiment1'
data = []
id_counter = 1

for source_folder in os.listdir(BASE_DIR):
    folder_path = os.path.join(BASE_DIR, source_folder)
    if not os.path.isdir(folder_path):
        continue
    source = source_folder
    for fname in os.listdir(folder_path):
        fpath = os.path.join(folder_path, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            markdown = f.read()
        data.append({
            "id": id_counter,
            "source": source,
            "markdown": markdown
        })
        id_counter += 1

with open(os.path.join(BASE_DIR, 'stimuli.json'), 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
