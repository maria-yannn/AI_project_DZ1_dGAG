with open(r'C:\Users\Пользователь\Documents\AI_project\data\dGAG_fasta.txt', 'r') as f:
    lines = f.read().strip().split('\n')

seq_name = ''
seq = ''
for line in lines:
    if line.startswith('>'):
        if seq_name:
            total = len(seq)
            gc = seq.count('G') + seq.count('C')
            print(f'{seq_name}: GC={gc}/{total} = {gc/total*100:.2f}%')
        seq_name = line[1:].strip()
        seq = ''
    else:
        seq += line.strip()

# последняя
total = len(seq)
gc = seq.count('G') + seq.count('C')
print(f'{seq_name}: GC={gc}/{total} = {gc/total*100:.2f}%')