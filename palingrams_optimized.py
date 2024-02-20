# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 11:48:11 2024

@author: tashr
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 11:40:37 2024

@author: tashr
"""

import load_dictionary
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 18:47:04 2024



@author: tashr
"""

"""Find all word-pair palingrams in a dictionary file."""
import time


word_list = load_dictionary.load('C:/Users/tashr/OneDrive/Desktop/Stat Approache/Week 2/dictionary.txt')

# find word-pair palingrams

start_time = time.time()
def find_palingrams():
    """Find dictionary palingrams."""
    pali_list = []
    words = set(word_list)
    for word in words:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in words:
                    pali_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in words:
                    pali_list.append((rev_word[:end-i], word))
    return pali_list


end_time = time.time()

palingrams = find_palingrams()
# sort palingrams on first word
palingrams_sorted = sorted(palingrams)

# display list of palingrams
print("\nNumber of palingrams = {}\n".format(len(palingrams_sorted)))
for first, second in palingrams_sorted:
    print("{} {}".format(first, second))


print("Runtime for this program was {} seconds.".format(end_time - start_time))
