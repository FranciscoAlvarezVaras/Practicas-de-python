import json, os, base64

NB_DIR = os.path.dirname(os.path.abspath(__file__))
NB_PATH = os.path.join(NB_DIR, "guia_06.ipynb")

with open(NB_PATH, encoding="utf-8") as fh:
    nb = json.load(fh)

cells = nb["cells"]
NL = chr(10)

def ss(c, t):
    ln = t.split(NL)
    c["source"] = [l + NL for l in ln[:-1]] + [ln[-1]]

def dc(b):
    return base64.b64decode(b).decode("utf-8")

DATA_PATH = os.path.join(NB_DIR, "cell_data.json")
with open(DATA_PATH, encoding="utf-8") as fh:
    cell_data = json.load(fh)
for idx_str, content in cell_data.items():
    idx = int(idx_str)
    ss(cells[idx], content)
    print(f"Cell {idx} updated")
with open(NB_PATH, "w", encoding="utf-8") as fh:
    json.dump(nb, fh, ensure_ascii=False, indent=1)
print("Notebook saved!")
