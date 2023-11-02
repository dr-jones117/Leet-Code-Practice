s1 = 'anagram'
s2 = 'nagaram'
s3 = 'rat'
s4 = 'car'

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_dict = {}

    for letter in s:
        if not s_dict.get(letter):
            s_dict[letter] = 1
        else:
            s_dict[letter] += 1

    for letter in t:
        if not s_dict.get(letter):
            return False
        else:
            s_dict[letter] -= 1

    for key, value in s_dict.items():
        if value != 0:
            return False

    return True

def main():
    print(f'\'{s1}\' is an anagram of \'{s2}\': {isAnagram(s1, s2)}')
    print(f'\'{s3}\' is an anagram of \'{s4}\': {isAnagram(s3, s4)}')

if __name__ == '__main__':
    main()

