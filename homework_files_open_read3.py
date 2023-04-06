with open('1.txt', 'rt', encoding='utf-8') as f:
    lines1 = f.readlines()
    f1 = f.name
    ln1 = [len(lines1), lines1, f1] 
    
with open('2.txt', 'rt', encoding='utf-8') as f:
    lines2 = f.readlines()
    f2 = f.name
    ln2 = [len(lines2), lines2, f2] 

with open('3.txt', 'rt', encoding='utf-8') as f:
    lines3 = f.readlines()
    f3 = f.name
    ln3 = [len(lines3), lines3, f3]

ln = [ln1, ln2, ln3]
ln.sort()

open('123.txt', 'w').close()

with open('123.txt', 'w') as f:
    for id, line, file in ln:
        f.write(f'{file}\nКоличество строк: {str(id)}\n')
        for lin in line:
            f.write(lin)
        f.write(f'\n')

with open('123.txt') as f:
    print(f.read())