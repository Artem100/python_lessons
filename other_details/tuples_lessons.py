value_list = ['мадам', 'топот', 'test', 'madam', 'word']

palindroms = [word for word in value_list if word[::-1] == word]
print(palindroms)