"""
Write a program to determine if two given strings are anagram of each other.
    example:
        s1 = "fairy tales"
        s2 = "rail safety"
"""
s1 = "fairy tales "
s2 = "rail safety "

s3 = "Kirimi"
s4 = "Karimi"


def is_anagram(s1,s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    if len(s1) != len(s2):
        return False

    alphabet = "abcdefghijklmnopqrstuvwxyz"


    s1 = s1.lower()
    s2 = s2.lower()

    dick_1 = dict.fromkeys(list(alphabet), 0)

    dick_2 = dict.fromkeys(list(alphabet), 0)

    for i in range(len(s1)):
        dick_1[s1[i]] +=1
        dick_2[s2[i]] +=1
    return dick_1 == dick_2

print is_anagram(s1, s2)