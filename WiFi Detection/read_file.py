file = '/Users/lichaohao/Desktop/dec_5.txt'

cnt = 0
try:
	binary = open(file,'r')
##	print(binary.read())

	word = []	
	for line in binary:
		line = line.split(' ')
		if line:
			if line[0] == 'No.':
				word.append(line[0])
				cnt = cnt +  1
	print(word)	
	print(cnt)
finally:
	if binary:
		binary.close()
