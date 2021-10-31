# For cracking alien text at rit
# Author Brandon Zazza


def search(wordlist, position1, position2):
    with open(wordlist) as a_file:
        n=0
        for line in a_file:
            if str(line[position1]) == str(line[position2]) and str(line[0]) == "e":
                print(line[2] + line[1], line, n, end=" ")
                n +=1 

def search_default(wordlist):
    with open(wordlist) as a_file:
        n=0
        for line in a_file:
            if str(line[0] == "t") : 
                print(line, n, end=" ")
                n +=1 

def code_check1():
    w1 = '_'
    w2 = 'e'
    w3 = 'i'
    w4 = 'o'
    w5 = 'u'
    w6 = '_'
    w7 = '_'
    w8 = '_'
    w9 = '_'
    w10 = '_'
    w11 = '_'
    code1 = [w1+w2, w3+w4+w5+w6, w7+w4+w1+w8, w9+w2+w1, w2+w9, w4+w10, w1+w2, w3+w4+w5+w6, w4+w9, w11+w9+w4+w2+w9]

    print(code1)

def code_check2():
    w1 = '_'
    w2 = '_'
    w3 = '_'
    w4 = '_'
    w5 = '_'
    w6 = '_'
    w7 = '_'
    w8 = '_'
    w9 = '_'
    code2 = [w1+w2+w3+w3+w4,w5+w6+w4+w7,w7+w8+w3+w3+w9]
    print(code2)

#search_default("4letters.txt")
#search("5letters.txt", 2, 3)
code_check1()
#code_check2()