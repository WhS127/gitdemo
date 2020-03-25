import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
#导入标点、文本和停用词
punctuation=[',','.','/','?',';',':','!','-','_','(',')','[',']','{','}']
op_stop_words=open('stop_words.txt')
stop_words=op_stop_words.read().split('\n')
op_text=open('text.txt')
original_text=op_text.read()
#退出两个界面
def destroy():
    top.destroy()
def destroy_count():
    count_words.destroy()
#进行文本的处理
def text_edit(original_text,stop_words):
    global text_edited
    coun=-1
    coun_all=1
    text_list=original_text.split()
    text_edited=[]
    for word in text_list:
        if word[-1] in punctuation:
            text_edited.append(word[:-2].lower())
        else:
            text_edited.append(word.lower())
    len_origin=len(text_edited)
    while coun_all<=len_origin:
        if text_edited[coun] in stop_words:
            text_edited.pop(coun)
            coun_all+=1
        else:
            coun=coun-1
            coun_all+=1
#显示原文本
def print_text(original_text):
    print(original_text)
#显示总次数
def print_total_num(original_text):
    print(len(original_text))
