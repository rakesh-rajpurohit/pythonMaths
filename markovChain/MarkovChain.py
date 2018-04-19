import numpy as np
# import matplotlib as pyplot

from pymarkovchain import MarkovChain
# Create an instance of the markov chain, tell it where to load / save its database
mc = MarkovChain("./markov")
# generate the markov chain's language model
mc.generateDatabase("This is a string of Text. It won't generate an interesting database though.")
mc.generateString()