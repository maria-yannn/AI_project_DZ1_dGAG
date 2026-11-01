with open('diary.md', 'a', encoding='utf-8') as f:
    f.write('\n## 2026-11-01 — Сжатие статьи paper.pdf\n')
    f.write('- Запрос агенту: каскадное сжатие L1-L3\n')
    f.write('- Что сделал агент: создал memory/L1.md, L2.md, L3.md\n')
    f.write('- Результат: получены три уровня сжатия\n')
    f.write('- Точка проверки: проверю вручную по PDF (позже)\n')
    f.write('- Итог проверки: в процессе\n')
print('Done')