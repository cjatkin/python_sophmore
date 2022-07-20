def hello():
	text = "hello"
	return text


def randNum():
	random.seed()
	text = ''
	i = 0
	while i < 20:
		num = random.randint(1,10)
		text += str(num)
		i += 1

	return text
		
