import re
from collections import defaultdict
with open('input/errors-ewts.csv') as f:
    raw = f.read()
    #raw = raw.replace('`not expected', '` not expected')
    lines = raw.split('\n')

data = []
for line in lines:
    columns = re.split(r'(?:^"|","|",,"|"$)', line)
    msgs = [a for a in columns[3].split(',') if a != '']
    entry = [columns[1], columns[2], msgs]
    data.append(entry)


error_types = []
by_error_type = defaultdict(list)
for entry in data:
    msgs = entry[2]
    for msg in msgs:
        msg = msg.replace('line 1: ', '')
        error_pattern = re.sub(r'`[^`]*`', r'`X`', msg)
        error_types.append(error_pattern)

        by_error_type[error_pattern].append(entry)
error_types = sorted(list(set(error_types)))

for type, entries in by_error_type.items():
    print('{} occurences:\t\t{}'.format(len(entries), type))

etc_count = 0
for line in lines:
    if 'character `.`.' in line:
        etc_count += 1
print('number of lines with misplaced dots:', etc_count)

print('ok')