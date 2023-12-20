favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print("===================")
for language in set(favorite_languages.values()):
    print(language.title())
    
# print("===================")
# for language in sorted(set(favorite_languages.values())):
#     print(language.title())