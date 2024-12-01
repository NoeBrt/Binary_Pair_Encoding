import numpy as np
import tqdm
text="low low low low lowest lowest newer newer newer newer newer newer wider wider wider new new"

def string_to_corpus(text):
    unique_words,count=np.unique(text.split(),return_counts=True)
    vocabulary = np.unique(list(text.replace(" ","_")))
    unique_words=unique_words+"_"    
    corpus=[list(world) for world in unique_words]
    return corpus,count,vocabulary

def update_vocabulary(corpus,count,vocabulary):
    pair_dict=dict()
    for i_word,word in enumerate(corpus):
        for i in range(len(word)-1):
            pair=f"{word[i]}{word[i+1]}"
            if pair in pair_dict:
                pair_dict[pair] += count[i_word]  # Add the frequency
            else:
                pair_dict[pair] = count[i_word]  # Initialize the frequency
    if not pair_dict:
        return None,vocabulary
    first_freq_pair=max(pair_dict, key=pair_dict.get)
    new_vocabulary=np.append(vocabulary,first_freq_pair) 
    return first_freq_pair,new_vocabulary

def merge(array,mask):
    output=[]
    i=0
    while i <(len(array)):
        if i < len(array)-1 and mask == f"{array[i]}{array[i+1]}" :
            output.append(str(mask))
            i+=2
        else:
            output.append(array[i])
            i+=1
    print(output)
    return output

def update_corpus(corpus,max_pair):
    new_corpus=[]
    for word_list in corpus:
       new_corpus.append(merge(word_list,max_pair))
    return new_corpus
    

print("------------start training-----------")
corpus,count,vocabulary=string_to_corpus(text)
print(corpus)
print(count)
k=10

from tqdm import trange

for i in trange(k):
    first_freq_pair, vocabulary = update_vocabulary(corpus, count, vocabulary)
    if first_freq_pair is None: 
        break  # Stop the loop early
    corpus = update_corpus(corpus, first_freq_pair)

#print after tqdm
if first_freq_pair is None:
    print("No more pairs, stopping")



print("------------end of training-----------")

print("Vocabulary :")
print(vocabulary)


def segment(input_text, vocabulary):
    tokens=input_text.replace(" ","_ ").split()
    for mask in vocabulary:
        tokens=update_corpus(tokens,mask)
    return tokens

print("segment :")
print(segment("the new low is newer but lowest",vocabulary))
        
        


