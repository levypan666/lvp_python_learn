favourite_languages = {
  'jen' : ['python', 'ruby'],
  'sarah' : ['c'],
  'edward' : ['ruby','go'],
  'phill' : ['python', 'haskell'],
}

for name, languages in favourite_languages.items():
  
  if len(languages) == 1:
    print("\n" + name.title() + "'s favourite languages is:")
  else:
    print("\n" + name.title() + "'s favourite languages are:")
  
  for language in languages:
      print("\t" + language.title())
