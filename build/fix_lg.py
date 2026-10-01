import sys, re, docx
sys.path.insert(0, 'build')
from docxutil import *
src, out = sys.argv[1], sys.argv[2]
d = docx.Document(src)
replace_everywhere(d, [('Business Innovation with Artificial Intelligence', 'Business Innovation with AI'),
                       (', governance documents and assessment responses.', ' and governance documents.')])
for p in d.paragraphs:
    t = p.text
    if t == 'TGS Ref No: TGS-2020504518': set_par(p, 'Course Code: C798')
    elif t == 'Version 23': set_par(p, 'Version 1.0')
    elif t == 'A1-A5 · K1-K4': set_par(p, 'LO1-LO5')
    elif t == 'Learning Outcomes and TSC Alignment': set_par(p, 'Learning Outcomes and Alignment')
    elif re.match(r'LO\d / A\d / K\d: ', t): set_par(p, re.sub(r'^(LO\d) / A\d / K\d: ', r'\1: ', t))
    elif t.startswith('Alignment: LO'): set_par(p, re.sub(r' · A\d(?:-A\d)? · K\d(?:-K\d)?', '', t))
    elif t.startswith('Appendix G - Assessment Flow and Support'):
        set_par(p, t.replace('Assessment Flow and Support', 'Course Support'))
    elif t == 'Courseware and assessment instructions are available through the LMS.':
        set_par(p, 'Courseware and lab instructions are available through the LMS.')
    elif t.startswith('Raise access, assessment or appeal questions'):
        set_par(p, 'Raise access or course questions through the trainer or training administrator.')
for p in list(d.paragraphs):
    if p.style.name == 'List Number' and re.search(r'TRAQOM|Digital Attendance|Written Assessment|assessment answers|Assessment Summary Record', p.text):
        del_par(p)
for t in list(d.tables):
    c0 = t.rows[0].cells[0].text
    if c0.startswith('Purpose: This guide supports the WSQ course'):
        set_cell(t.rows[0].cells[0], 'Purpose: This guide supports the course Business Innovation with AI (C798). It is designed for concept study, facilitated discussion and practical work.')
    elif c0.startswith('Assessment: The approved plan'):
        t._tbl.getparent().remove(t._tbl)
    elif c0.startswith('Assessment preparation:'):
        set_cell(t.rows[0].cells[0], c0.replace('Assessment preparation:', 'Practice:'))
    elif c0 == 'Outcome and TSC element':
        set_cell(t.rows[0].cells[0], 'Outcome'); set_cell(t.rows[0].cells[1], 'Topics and labs')
        for r in t.rows[1:]:
            set_cell(r.cells[0], r.cells[0].text.split(' / ')[0])
            set_cell(r.cells[1], re.sub(r'; WA Q\d; OQ OQ\d\.', '.', r.cells[1].text))
v = d.tables[0]
for r in list(v.rows)[2:]: del_row(v, r)
for c, txt in zip(v.rows[1].cells, ['1.0', '1 October 2026', 'Initial release of the one-day course: concept guide, cases and five guided labs.', 'Dr. Alfred Ang']):
    set_cell(c, txt)
d.save(out)
print('wrote', out)
