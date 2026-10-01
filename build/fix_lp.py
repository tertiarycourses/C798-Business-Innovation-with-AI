import sys, re, docx
sys.path.insert(0, 'build')
from docxutil import *
src, out = sys.argv[1], sys.argv[2]
d = docx.Document(src)
T = 'Business Innovation with Artificial Intelligence'
replace_everywhere(d, [(T, 'Business Innovation with AI')])
P = d.paragraphs
for p in P:
    t = p.text
    if t == 'TGS Ref No: TGS-2020504518': set_par(p, 'Course Code: C798')
    elif t == 'Version 23': set_par(p, 'Version 1.0')
    elif t == 'Learning Outcomes and TSC Mapping': set_par(p, 'Learning Outcomes')
    elif t == 'Facilitation and Assessment Approach': set_par(p, 'Facilitation Approach')
    elif re.match(r'LO\d / A\d / K\d: ', t): set_par(p, re.sub(r'^(LO\d) / A\d / K\d: ', r'\1: ', t))
    elif t.startswith('Each assessed criterion'):
        set_par(p, 'Each outcome is explicitly taught in the listed topics and rehearsed in the listed labs.')
    elif t.startswith('Verified totals:'):
        set_par(p, 'Verified totals: 450 minutes (7.5 hours) instructional time; 30-minute lunch excluded.')
for p in list(d.paragraphs):
    t = p.text
    if t.startswith(('Written Assessment (WA-SAQ)', 'Oral Questioning (OQ)', 'The approved assessment covers', 'Display and verify AM, PM')):
        del_par(p)
tb = d.tables
# 0 version record
v = tb[0]
del_row(v, v.rows[2])
for c, txt in zip(v.rows[1].cells, ['1.0', '1 October 2026', 'Initial release of the one-day course: five topics and five guided labs.', 'Dr. Alfred Ang']):
    set_cell(c, txt)
# 1 TOC
for r in tb[1].rows:
    if r.cells[0].text == 'Learning Outcomes and TSC Mapping': set_cell(r.cells[0], 'Learning Outcomes')
    if r.cells[0].text == 'Facilitation and Assessment Approach': set_cell(r.cells[0], 'Facilitation Approach')
# 2 course info
ci = tb[2]
for r in list(ci.rows):
    k = r.cells[0].text
    if k == 'Course reference': set_cell(r.cells[0], 'Course code'); set_cell(r.cells[1], 'C798')
    elif k in ('TSC', 'Assessment'): del_row(ci, r)
    elif k == 'Duration': set_cell(r.cells[1], '1 day · 7.5 instructional hours')
    elif k == 'Timing': set_cell(r.cells[1], '09:30–17:30 · 30-minute lunch')
# 3 alignment matrix: drop TSC + Assessment columns
drop_columns(tb[3], [1, 4])
# 4 schedule
sch = tb[4]
plan = {
 'Course orientation': ('09:30–09:55', '25 min', 'Course orientation, learner introduction, ground rules and course outcomes', None, '1–7'),
 'Topic 1': ('09:55–11:10', '75 min', None, None, '8–34'),
 'Topic 2': ('11:10–12:35', '85 min', None, None, '35–69'),
 'Lunch break': ('12:35–13:05', '30 min', None, None, None),
 'Topic 3': ('13:05–14:25', '80 min', None, None, '70–98'),
 'Topic 4': ('14:25–15:45', '80 min', None, None, '99–125'),
 'Topic 5': ('15:45–17:05', '80 min', None, None, '126–154'),
 'Course recap': ('17:05–17:30', '25 min', 'Course recap, implementation commitments and course feedback', 'Review, Q&A, feedback', '155–160'),
}
for r in list(sch.rows)[1:]:
    act = r.cells[2].text
    key = next((k for k in plan if act.startswith(k)), None)
    if key is None:
        del_row(sch, r); continue
    tm, du, a, m, sl = plan[key]
    set_cell(r.cells[0], tm); set_cell(r.cells[1], du)
    if a: set_cell(r.cells[2], a)
    if m: set_cell(r.cells[3], m)
    if sl: set_cell(r.cells[4], sl)
d.save(out)
print('wrote', out)
