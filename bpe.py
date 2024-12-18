import numpy as np
from tqdm import trange
import argparse

def string_to_corpus(text):
    unique_words, count = np.unique(text.split(), return_counts=True)
    vocabulary = np.unique(list(text.replace(" ", "_")))
    unique_words = unique_words + "_"
    corpus = [list(word) for word in unique_words]
    return corpus, count, vocabulary

def update_vocabulary(corpus, count, vocabulary):
    pair_dict = dict()
    for i_word, word in enumerate(corpus):
        for i in range(len(word) - 1):
            pair = f"{word[i]}{word[i+1]}"
            pair_dict[pair] = pair_dict.get(pair, 0) + count[i_word]
    if not pair_dict:
        return None, vocabulary
    first_freq_pair = max(pair_dict, key=pair_dict.get)
    new_vocabulary = np.append(vocabulary, first_freq_pair)
    return first_freq_pair, new_vocabulary

def merge(array, mask):
    output = []
    i = 0
    while i < len(array):
        if i < len(array) - 1 and mask == f"{array[i]}{array[i+1]}":
            output.append(str(mask))
            i += 2
        else:
            output.append(array[i])
            i += 1
    return output

def update_corpus(corpus, max_pair):
    new_corpus = []
    for word_list in corpus:
        new_corpus.append(merge(word_list, max_pair))
    return new_corpus

def train_model(text, iterations=10):
    corpus, count, vocabulary = string_to_corpus(text)
    for _ in trange(iterations, desc="Training"):
        first_freq_pair, vocabulary = update_vocabulary(corpus, count, vocabulary)
        if first_freq_pair is None:
            break
        corpus = update_corpus(corpus, first_freq_pair)
    return vocabulary

def segment(input_text, vocabulary):
    tokens = input_text.replace(" ", "_ ").split()
    for mask in vocabulary:
        tokens = update_corpus(tokens, mask)
    return tokens

def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Corpus Vocabulary Trainer and Segmenter CLI")
    parser.add_argument("text", type=str, help="Input text to train the model (or path to a .txt file)")
    parser.add_argument("--segment", type=str, help="Text to segment based on the trained vocabulary")
    parser.add_argument("--iterations", type=int, default=10, help="Number of iterations for training")
    args = parser.parse_args()

    # Check if the input text is a path to a file
    if args.text.endswith(".txt"):
        text = read_file(args.text)
    else:
        text = args.text

    print("------------ Start Training -----------")
    vocabulary = train_model(text, args.iterations)
    print("------------ End of Training -----------")
    print("Vocabulary:")
    print(vocabulary)

    if args.segment:
        # Handle segmenting from a text file
        if args.segment.endswith(".txt"):
            segment_text = read_file(args.segment)
        else:
            segment_text = args.segment

        print("Segmented Text:")
        print(segment(segment_text, vocabulary))
