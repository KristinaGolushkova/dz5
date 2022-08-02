with open('file.txt') as f:
	a = f.read()
	print(sum(map(str.isalpha, a)), 'letters')
	print(len(a.split()), 'words')
	print(a.count('\n') + 1, 'lines')