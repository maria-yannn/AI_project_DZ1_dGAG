from pypdf import PdfReader
r = PdfReader('paper/paper.pdf.pdf')
print(f'Pages: {len(r.pages)}')
for i in range(len(r.pages)):
    text = r.pages[i].extract_text()
    print(f'--- PAGE {i+1} ---')
    print(text[:2000])
    print()