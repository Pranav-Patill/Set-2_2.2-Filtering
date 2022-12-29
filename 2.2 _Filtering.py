'''
Set 2
2.2	Filtering
Write a Python program to split a string of words separated by commas and spaces into two lists, words and separators using function. 
Input: W3resource Python, Exercises.
Output:
[['W3resource', 'Python', 'Exercises.'], [' ', ', ']]
'''
stri = "The dance, held in the school gym, ended at midnight."
def splitWords(str):
    sep_list=[]
    word_list=[]
    final_list=[]
    temp=""
    for i in range(len(str)):
        temp+=str[i]
        if str[i] in [" ",","]:
            sep_list.append(str[i])
            if temp not in [" ",","]:word_list.append(temp[:-1])
            temp=""
        elif i==len(str)-1:
            word_list.append(temp)
            temp=""
    final_list+=[word_list,sep_list]
    print(final_list)

splitWords(stri)