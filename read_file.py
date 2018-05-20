def read_sister_cities():
    sister_cities = []
    with open('./sister_cities.txt', encoding='utf-8') as f:
        for line in f:
            sister_cities.append(line.strip('\n').strip('(').strip(')').strip('?').lower())
    return sister_cities

def make_matrix(songs):
    matrix = []
    for sentence in songs:
        entry = []
        for word in sentence.split(' '):
            entry.append(word)
        matrix.append(entry)
    return matrix

def get_sentence_matrix():
    songs = read_sister_cities()
    sentences = make_matrix(songs)

    # print(sentences)
    return sentences