"""Quick audit: verify all asset references and links in README.md resolve properly."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
readme = (ROOT / "README.md").read_text(encoding="utf-8")

pattern = re.compile(r"\./assets/[\w./\-]+")
refs = pattern.findall(readme)

print("Auditing asset references in README.md:")
all_ok = True
for r in refs:
    p = ROOT / r.lstrip("./")
    ok = p.exists()
    if not ok:
        all_ok = False
    print(f"  {'[OK]' if ok else '[MISSING]':10s}  {r}")

print()
print("Auditing links in README.md:")
link_pattern = re.compile(r'href="([^"]+)"')
links = link_pattern.findall(readme)
for l in links:
    print(f"  [LINK]      {l}")

print()
if all_ok:
    print("[SUCCESS] All asset references are valid and exist on disk!")
else:
    print("[WARNING] Missing asset references detected!")
