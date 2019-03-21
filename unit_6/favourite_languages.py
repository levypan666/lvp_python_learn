#搭建字典
favourite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'pill': 'python',
}

print("The following languages have been mentioned:")
for language in set(favourite_languages.values()):
	print(language.title()) 