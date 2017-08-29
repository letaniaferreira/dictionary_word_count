filename = open("test.txt")

big_word_list = []
for line in filename:
    line = line.strip()
    words = line.split(" ")
    for word in words:
        big_word_list.append(word)


word_count = {}

count = 0
for word in big_word_list:
    word_count[word] = word_count.get(word, 0) + 1
    # if word not in word_count:
    #     word_count[word] = count + 1
    # else:
    #     word_count[word] = count + 1
    # # word_count[word] = count
print word_count

