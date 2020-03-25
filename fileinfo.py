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
#以下组合在次数统计内
#所有词数统计
def all_number(text_edited):
    global num_word,num_num
    num_word=[]
    num_num=[]
    for word in text_edited:
        if word not in num_word:
            num_word.append(word)
            num_num.append(text_edited.count(word))
#所有词对应数量的显示
def all_number_print(num_word,num_num):
    num_pr_n=0
    while num_pr_n<len(num_word):
        print(str(num_word[num_pr_n]),str(num_num[num_pr_n]))
        num_pr_n+=1
#找出最多的六个词
def most_num(num_word,num_num):
    global most_six
    num_lis_n=0
    num_sort_six=[]
    while num_lis_n<len(num_word):
        num_sort_six.append([num_num[num_lis_n],num_word[num_lis_n]])
        num_lis_n+=1
    num_sort_six.sort()
    most_six=num_sort_six[-6:]
#显示六个关键词
def most_num_print(most_six):
    for i in range(6):
        print(most_six[i])
#将关键词做成图表
def chart(most_six):
    most_six_or=[]
    most_six_num=[]
    for i in most_six:
        most_six_or.append(i[-1])
        most_six_num.append(i[0])
    N=6
    ind=np.arange(N)
    num=most_six_num
    figure=plt.bar(ind,num,width=0.35,align='center',tick_label=most_six_or)
    plt.ylabel('The number of the word')
    plt.title('The key word of the text')
    for a,b in zip(ind,num):
        plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=7)
    plt.show()
#次数统计界面
def count_word(num_word,num_num):
    count_words=Tk()
    count_words.title('词数统计')
    button_all_number_print=Button(count_words,text='所有有效单词各词数统计',command=lambda:all_number_print(num_word,num_num))
    button_most_num=Button(count_words,text='关键词',command=lambda:(most_num_print(most_six)))
    button_chart=Button(count_words,text='关键词词数统计表',command=lambda:(chart(most_six)))
    button_exit_count=Button(count_words,text='退出',command=destroy_count)
    button_all_number_print.grid(row=0,column=0)
    button_most_num.grid(row=0,column=1)
    button_chart.grid(row=1,column=0)
    button_exit_count.grid(row=1,column=1)
