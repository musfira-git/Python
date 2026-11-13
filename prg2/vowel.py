word = input("Enter a word:")
vowels = [x for x in word.lower() if x in ["a","e","i","o","u"]]
print("the vowels in the word are:",vowels)