text = input()
words = text.split()
websites = []
for word in words:
    # finish the code here
    if word.lower().startswith("https://") or word.lower().startswith("http://")  or word.lower().startswith("www."):
        websites.append(word)

print('\n'.join(websites))
