import json, sys
import os
idx = int(sys.argv[1])
txt_path = sys.argv[2]
NL = chr(10)
nb_dir = os.path.dirname(os.path.abspath(__file__))
nb_path = os.path.join(nb_dir, "guia_06.ipynb")
with open(nb_path, encoding="utf-8") as fh:
    nb = json.load(fh)
with open(txt_path, encoding="utf-8") as fh:
    txt = fh.read()
if txt.endswith(NL):
    txt = txt[:-1]
ln = txt.split(NL)
nb["cells"][idx]["source"] = [l + NL for l in ln[:-1]] + [ln[-1]]
with open(nb_path, "w", encoding="utf-8") as fh:
    json.dump(nb, fh, ensure_ascii=False, indent=1)
print(f"Cell {idx} updated")
