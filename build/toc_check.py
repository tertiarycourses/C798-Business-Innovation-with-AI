import sys, subprocess, re
pdf, entries = sys.argv[1], sys.argv[2:]
n = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout).group(1))
pages = [subprocess.run(['pdftotext','-f',str(i),'-l',str(i),'-layout',pdf,'-'],capture_output=True,text=True).stdout for i in range(1,n+1)]
toc_page = next(i for i,p in enumerate(pages) if 'TABLE OF CONTENTS' in p)
for e in entries:
    title, want = e.rsplit('=',1)
    got = next((i+1 for i,p in enumerate(pages) if i > toc_page and any(l.strip().startswith(title) for l in p.splitlines())), None)
    flag = '' if str(got) == want else '   <-- MISMATCH'
    print(f'{title!r}: toc={want} actual={got}{flag}')
