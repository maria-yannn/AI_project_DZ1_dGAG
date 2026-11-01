from pypdf import PdfReader
r = PdfReader('paper/paper.pdf.pdf')
full_text = ""
for i in range(len(r.pages)):
    text = r.pages[i].extract_text()
    full_text += f"\n--- PAGE {i+1} ---\n" + text
with open('src/full_text.txt', 'w', encoding='utf-8') as f:
    f.write(full_text)
print(f"Total pages: {len(r.pages)}")
print(f"Total chars: {len(full_text)}")