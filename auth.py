import numpy as np
import nltk
import sys

nltk.download('gutenberg')
nltk.corpus.gutenberg.fileids()

known_text_1 = sys.argv[1]
known_text_2 = sys.argv[2]
questioned_text = sys.argv[3]

try:
    known_text_1_words = nltk.corpus.gutenberg.words(known_text_1)
    known_text_1_words = ' '.join(known_text_1_words)
    known_text_2_words = nltk.corpus.gutenberg.words(known_text_2)
    known_text_2_words = ' '.join(known_text_2_words)
    questioned_text_words = nltk.corpus.gutenberg.words(questioned_text)
    questioned_text_words = ' '.join(questioned_text_words)

except:
    print("Warning: The given text name are not found in the data set.")
    sys.exit()


state = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p","q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
#create word2id and id2word dictionary
char2id_dict = {}
for index, char in enumerate(state):
    char2id_dict[char] = index

def create_transition_matrix(text):
    transition_matrix = np.zeros((27, 27))
    
    for i in range(len(text)-1):
        current_char = text[i].lower()
        next_char = text[i+1].lower()
        
        if (current_char in state) & (next_char in state):
            current_char_id = char2id_dict[current_char]
            next_char_id = char2id_dict[next_char]
            transition_matrix[current_char_id][next_char_id] = transition_matrix[current_char_id][next_char_id] + 1
            sum_of_each_row_all  = np.sum(transition_matrix, 1)
    
    for i in range (27):
        single_row_sum = sum_of_each_row_all[i]
        if (sum_of_each_row_all [i] == 0):
            single_row_sum = 1
            
        transition_matrix[ i,: ] =  transition_matrix[ i,: ] / single_row_sum

    return transition_matrix


TM_known_text_1 = create_transition_matrix(known_text_1_words)
TM_known_text_2 = create_transition_matrix(known_text_2_words)

log_likelihood_known_text_1 = 0
log_likelihood_known_text_2 = 0

for i in range(len(questioned_text_words)-1):
    current_char = questioned_text_words[i].lower()
    next_char = questioned_text_words[i+1].lower()

    if (current_char in state) & (next_char in state):
        current_char_id = char2id_dict[current_char]
        next_char_id = char2id_dict[next_char]

        if TM_known_text_1[current_char_id][next_char_id] != 0 and TM_known_text_2[current_char_id][next_char_id] != 0:
            log_likelihood_known_text_1 += np.log(TM_known_text_1[current_char_id][next_char_id])
            log_likelihood_known_text_2 += np.log(TM_known_text_2[current_char_id][next_char_id])

# command-line output
print("log likelihood of {} = {}\n".format(known_text_1, str(log_likelihood_known_text_1)))
print("log likelihood of {} = {}\n".format(known_text_2, str(log_likelihood_known_text_2)))

# Output the result to text file
with open("result.txt", "w+") as f:
    f.write("Questioned text name: {}\n\n".format(questioned_text))
    f.write("log likelihood of {} = {}\n".format(known_text_1, str(log_likelihood_known_text_1)))
    f.write("log likelihood of {} = {}\n\n".format(known_text_2, str(log_likelihood_known_text_2)))

    if log_likelihood_known_text_1 > log_likelihood_known_text_2:
        log_likelihood_larger = known_text_1
        log_likelihood_smaller = known_text_2
    else:
        log_likelihood_larger = known_text_2
        log_likelihood_smaller = known_text_1

    f.write("The questioned text has a higher probability written by the author of {} than that of {}.\n".format(log_likelihood_larger, log_likelihood_smaller))




