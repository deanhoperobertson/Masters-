
def readfile(filename):
    f = open(filename)
    sentences = []
    sentence = []
    for line in f:
        if len(line) == 0 or line.startswith('-DOCSTART') or line[0] == "\n":
            if len(sentence) > 0:
                sentences.append(sentence)
                sentence = []
            continue
        splits = line.split(' ')
        sentence.append([splits[0], splits[-1].strip()])

    if len(sentence) > 0:
        sentences.append(sentence)
        sentence = []
    return sentences

def readstring(filename):
    f = filename.split('\n')
    sentences = []
    sentence = []
    for line in f:
        if len(line) == 0 or line.startswith('-DOCSTART') or line[0] == "\n":
            if len(sentence) > 0:
                sentences.append(sentence)
                sentence = []
            continue
        splits = line.split(' ')
        sentence.append([splits[0], splits[-1].strip()])

    if len(sentence) > 0:
        sentences.append(sentence)
        sentence = []
    return sentences

def get_sentence(dataset,sentence_number):
    sentence = []
    for i in dataset[sentence_number-1]:
        sentence.append(i[0])
    return(sentence)

def get_label(dataset,sentence_number):
    sentence = []
    for i in dataset[sentence_number-1]:
        sentence.append(i[1])
    return(sentence)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def extract_words(dictionary):
    words = []
    tags = []
    for sentence in dictionary:
        for word in sentence:
            words.append(word[0])
            tags.append(word[1]) 
    return(words,tags)   
