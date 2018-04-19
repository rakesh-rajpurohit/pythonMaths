import numpy as np


def cos_sim(a, b):
    """ Takes 2 vectors a, b and returns the cosine similarity according to the definition
        of the dot product """
    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)

    return dot_product/ (norm_a * norm_b);


sentence_m = np.array([1, 1, 1, 1, 0, 0, 0, 0, 0])
sentence_h = np.array([0, 0, 1, 1, 1, 1, 0, 0, 0])
sentence_w = np.array([0, 0, 0, 1, 0, 0, 1, 1, 1])


print(cos_sim(sentence_m, sentence_h))
print(cos_sim(sentence_m, sentence_w))