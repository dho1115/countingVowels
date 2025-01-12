#Count the number of vowels inside a string.
CountVowels = lambda string: {**dict.fromkeys(",".join("aeiouy").split(","), 0), **{i:string.lower().count(i) for i in set(vowel for vowel in string.lower() if (vowel in 'aeiouy'))}, "string": string, "total": len(list(filter(lambda i: i in "aeiouy", string.lower())))};

#Insert multiple strings.
CountVowelsMultipleStrings = lambda *strings, fn=CountVowels: [fn(i) for i in strings]

#Test.
print(CountVowelsMultipleStrings("Hello", "EEK", "tHE Quick Brown something or another"))






