import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
#导入标点、文本和停用词
punctuation=[',','.','/','?',';',':','!','-','_','(',')','[',']','{','}']
op_stop_words=open('stop_words.txt')
stop_words=op_stop_words.read().split('\n')
op_text=open('text.txt')
original_text=op_text.read()

