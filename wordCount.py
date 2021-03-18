text_file = open('mbox-short.txt')
count = 0
w_length = list()
l_length = list()
for line in text_file:
    count += 1
    words = line.split()
    words_length = len(words)
    w_length.append(words_length)
    line = ''.join(words)
    line_length = len(line)
    l_length.append(line_length)
print(f'Total characters: {sum(l_length)}')
print(f'Total lines: {count}')
print(f'Word count: {sum(w_length)} ')