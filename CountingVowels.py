#Count the number of vowels inside a string.

CountVowels = lambda string: {**dict.fromkeys(",".join("aeiouy").split(","), 0), **{i:string.lower().count(i) for i in set(vowel for vowel in string.lower() if (vowel in 'aeiouy'))}, "string": string, "total": len(list(filter(lambda i: i in "aeiouy", string.lower())))};

CountVowelsMultipleStrings = lambda *strings, fn=CountVowels: [fn(i) for i in strings]

print(CountVowels("Hello, world... how are you?"));
print(CountVowels("The Quick Brown Fox Jumped Over The LAZY ASS DOG!!!"));
print(CountVowels("HelloO"));
print(CountVowels("LAAAZYYY"));
print(CountVowels("Is the sky really falling???"));

print(CountVowelsMultipleStrings("Hello", "EEK", "tHE Quick Brown something or another"))






