"""Write Course_Info/Datasets.md from the files in DataSets/ (run by build.sh)."""
import os, html

root = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(root, "DataSets")
out = os.path.join(root, "Course_Info", "Datasets.md")

lines = [
    "# Datasets",
    "",
    "Data files used in lectures and notebooks. Notebooks in this course "
    "read them from the `DataSets` folder of the course repository. Most "
    "datasets come from the textbook (ISLP); see [Credits and sources]"
    "(Credits.md).",
    "",
]

def human(n):
    for unit in ("bytes", "KB", "MB", "GB"):
        if n < 1024 or unit == "GB":
            return f"{n:.0f} {unit}" if unit == "bytes" else f"{n:.1f} {unit}"
        n /= 1024

files = []
if os.path.isdir(src):
    for dp, dn, fn in os.walk(src):
        dn[:] = sorted(d for d in dn if not d.startswith("."))
        for f in sorted(fn):
            if f.startswith("."):
                continue
            p = os.path.join(dp, f)
            files.append((os.path.relpath(p, src).replace(os.sep, "/"), os.path.getsize(p)))

if files:
    lines += ["| File | Size |", "|---|---|"]
    for rel, size in files:
        label = html.escape(rel)
        lines.append(f'| <a href="../DataSets/{label}">{label}</a> | {human(size)} |')
else:
    lines.append("Dataset files will be listed here.")

with open(out, "w") as fh:
    fh.write("\n".join(lines) + "\n")
print(f"Datasets page: {len(files)} file(s)")
