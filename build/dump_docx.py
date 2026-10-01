import sys, docx
d = docx.Document(sys.argv[1])
body = d.element.body
from docx.table import Table
from docx.text.paragraph import Paragraph
ti=0
for el in body.iterchildren():
    tag = el.tag.split('}')[1]
    if tag=='p':
        p=Paragraph(el,d)
        if p.text.strip(): print(f"P[{p.style.name}] {p.text}")
        elif el.xpath('.//w:txbxContent'): print("P[TEXTBOX]", ' '.join(t.text or '' for t in el.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')))
    elif tag=='tbl':
        t=Table(el,d); print(f"TABLE {ti}"); ti+=1
        for r in t.rows: print('   |', ' | '.join(c.text.replace('\n',' / ') for c in r.cells))
    elif tag=='sdt': print("SDT", ' '.join(t.text or '' for t in el.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t'))[:300])
for s in d.sections:
    for part in (s.header, s.footer):
        print("HDR/FTR:", ' / '.join(p.text for p in part.paragraphs if p.text))
