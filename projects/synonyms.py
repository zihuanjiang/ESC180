import math

def norm(vec):
    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    return math.sqrt(sum_of_squares)

def dot_product(vec1,vec2):
    result = 0.0
    for x in vec1:
        if x in vec2:
            result += vec1[x] * vec2[x]
    return result


def cosine_similarity(vec1, vec2):
    dot = dot_product(vec1,vec2)
    length1 = norm(vec1)
    length2 = norm(vec2)
    return dot/length1/length2

def update_value(list,key,initial_value):
    for i in range(len(list)):
        if list[i] != key:
            if list[i] not in initial_value:
                initial_value.update({list[i]:1})
            else:
                initial_value[list[i]] += 1
    return initial_value

def build_semantic_descriptors(sentences):
    result = {}

    for i in range(len(sentences)):
        for j in range(len(sentences[i])):
            if sentences[i][j] not in result:
                result.update({sentences[i][j]:{}})
            update = update_value(sentences[i],sentences[i][j],\
            result[sentences[i][j]])
            result.update({sentences[i][j]:update})
    return result

def build_semantic_descriptors_from_files(filenames):
    final_list = []
    for i in range(len(filenames)):
        x = open(filenames[i], "r", encoding="latin1").read()
        x = x.replace(',',' ')
        x = x.replace('-',' ')
        x = x.replace('--',' ')
        x = x.replace(':',' ')
        x = x.replace(';',' ')
        x = x.replace('  ',' ')
        x = x.lower()
        while True:
            index_1 = x.find('.')  # index for .
            index_2 = x.find('!')  # index for !
            index_3 = x.find('?')  # index for ?
            if index_1 == -1 and index_2 == -1 and index_3 == -1:
                break
            else:
                min_index = index_1
                if index_2 >= 0 and index_2 < min_index:
                    min_index = index_2
                if index_3 >= 0 and index_3 < min_index:
                    min_index = index_3
                string_before_sentence_break = x[0:min_index]
                list = string_before_sentence_break.split()
                final_list.append(list)
                list = []
                x = x[min_index+1:]
    return build_semantic_descriptors(final_list)



def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    index = -1
    recent_choices = choices[0]
    for i in range(len(choices)):
        choices_value = semantic_descriptors.get(choices[i])
        word_value = semantic_descriptors.get(word)
        if choices_value != None and word_value != None:
            choices_index = similarity_fn(choices_value,word_value)
            if choices_index > index:
                index = choices_index
                recent_choices = choices[i]
    return recent_choices


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    correct = 0
    total = 0
    x = open(filename, "r", encoding="latin1")
    list_of_x = []
    for line in x:
        list_of_line = line.split()
        list_of_x.append(list_of_line)

    for j in range(len(list_of_x)):
        word = list_of_x[j][0]
        choices = list_of_x[j][2:]
        guess = most_similar_word(word,choices,semantic_descriptors,\
        similarity_fn)

        if guess == list_of_x[j][1]:
            correct += 1
            total += 1
        else:
            total += 1
    return 100*correct/total
