def calc_vowels():
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    string1 = input("Put everything you want: ")
    count = 0
    for i in string1:
        if i in vowels:
            count = count + 1
    print(count)

calc_vowels()

