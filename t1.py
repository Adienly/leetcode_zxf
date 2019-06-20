map = {'(':')',
	  '[':']',
	  '{':'}'}
stack = []
str = "({[]})("
for i in str:
	if i in map:
		stack.append(i)
	else:
		if len(stack)==0:
			print(False)
			break
		else:
			top_element = stack.pop()
			if map[top_element] != i:
				print(False)
				break
if len(stack)!=0:
	print(False)