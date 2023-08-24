# Problem 1 (a)


file = open("text1.txt", encoding="latin-1").read().split()

word_count = {}
word = []
repetition = []
repeat = 0
counter = 0

for i in range (len(file)):

    for k in range (0, i):

        if file[i] == file[k]:
            repeat += 1

    if  repeat == 0:

        word.append(file[i])

        for j in range (len(file)):
            if file[i] == file[j]:
                counter += 1

        repetition.append(counter)


    repeat = 0
    counter = 0


for i in range (len(word)):
        word_count[word[i]] = repetition[i]

# print(word_count)





# Problem 1 (b)

integer = [0] * 100

for i in range (1, 101):
    integer[i-1] = i

def top10 (L):

    top10 = [0] * 10

    for i in range (0, 10):

        top10[i] = max(L)
        L.remove(max(L))

    return top10


print(top10(integer))





# Problem 1 (c)

file = open("1342-0.txt", encoding="latin-1").read().split()

word_count = {}
frequency = {}
word = []
repetition = []
repeat = 0
counter = 0

for i in range (len(file)):

    for k in range (0, i):

        if file[i] == file[k]:
            repeat += 1

    if  repeat == 0:

        word.append(file[i])

        for j in range (len(file)):
            if file[i] == file[j]:
                counter += 1

        repetition.append(counter)


    repeat = 0
    counter = 0


for i in range (len(word)):
        word_count[word[i]] = repetition[i]



def top10 (L):

    top10 = [0] * 10

    for i in range (0, 10):

        top10[i] = max(L)
        L.remove(max(L))

    return top10


for i in range (0, 10):
        frequency[repetition[i]] = word[i]

print(frequency)





import urllib.request

def get_search_count(search_term):
    search_str = "https://ca.search.yahoo.com/search;_ylt=ApXMDpgZXgEXhwqnhMHHFhUt17V_?p="
    url = search_str + urllib.parse.quote(search_term)

    f = urllib.request.urlopen(url)
    page = f.read().decode("utf-8")
    f.close()

    start = page.index('About ')+len('About ') # page.index('Next</a><span>')+len('Next</a><span>')
    offset = page[start:].index(' search results') # (' results')
    count_str = page[start:start+offset]
    count_str_clean = count_str.replace(',', '')
    count = int(count_str_clean)
    return count



def choose_variant(variants):
    counts = []

    for variant in variants:
        counts.append(get_search_count(variant))

    return variants[counts.index(max(counts))]



print(choose_variant(['"fifth anniversary"', '"five-year anniversary"']))
print(choose_variant(['top ranked school uoft', 'top ranked school waterloo']))














