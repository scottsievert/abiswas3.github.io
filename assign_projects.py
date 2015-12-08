import sys

with open('students') as f:
    a = f.readlines()

j = 3

projects = ['2',
 '3',
 '4',
 '5',
 '6',
 '7',
 '8',
 '9',
 '10',
 '11',
 '12',
 '13',
 '14',
 '15',
 '16',
 '1',
 '2',
 '3',
 '4',
 '5',
 '6',
 '7',
 '9',
 '10',
 '8',
 '11',
 '12',
 '13',
 '14',
 '15',
 '16',
 '1',
 '2',
 '3',
 '4',
 '5',
 '6',
 '7',
 '8',
 '9',
 '10',
 '11',
 '12',
 '13',
 '14',
 '15',
 '1']
# for i in xrange(0, len(a)):
#     projects.append(j)
#     j = (j+1) % 16

f = open('assignment.html', 'w')
sys.stdout = f

print '<!DOCTYPE html>'
print '<html>'
print '<head>'
print '<style>'
print 'table, th, td {'
print '    border: 1px solid black;'
print '    border-collapse: collapse;'
print '}'

print 'th, td {'
print 'padding: 5px;'
print '}'
print '</style>'
print '</head>'
print '<body>'

print '<table style="width:100%">'
print '<tr>'
print '    <th>%s</th>'%('Name')
print '    <th>%s</th>'%('Lab Number')
print '</tr>'

tup = []
count = -1
for i,j in zip(a, projects):
    tup.append((i.strip(),(j)))

#tup2 = sorted(tup, key=lambda t: t[0].split()[1])

#for i,j in zip(a,projects):
i = -1
for t in tup:
    i +=1
    print '<tr>'
    print '    <td>%s</td>'%(t[0])
    print '    <td>%d</td>'%(int(t[1]))
    print '</tr>'
print '</table>'


print '</body>'
print '</html>'
f.close()

