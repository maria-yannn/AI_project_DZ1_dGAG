import sys
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "candidates.csv"
errors = []

# 1. Проверяем, что файл существует
if not RESULT.is_file():
    print(f"Ошибка: нет файла {RESULT.relative_to(ROOT)}")
    sys.exit(1)

# 2. Проверяем, что это таблица с нужными столбцами
try:
    with open(RESULT, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
except Exception as e:
    print(f"Ошибка при чтении файла: {e}")
    sys.exit(1)

need_columns = {"gene_id", "protein_name", "evidence_type", "source"}
if not rows or not need_columns.issubset(set(rows[0].keys())):
    errors.append(f"В таблице должны быть столбцы: {', '.join(need_columns)}")
    sys.exit(1)

# 3. Проверяем, что кандидатов не меньше 3
if len(rows) < 3:
    errors.append(f"Найдено только {len(rows)} кандидатов, а нужно минимум 3.")

# 4. Проверяем, что у кандидатов указан источник (source не пустой)
for i, row in enumerate(rows):
    if not row.get("source", "").strip():
        errors.append(f"У кандидата {i+1} не указан источник (source).")

if errors:
    print("\n".join(errors))
    sys.exit(1)
else:
    print("принято")
    sys.exit(0)