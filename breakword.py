from collections import Counter
#Chuyển dấu câu thành ||| để split chỉ thành mảng 1 chiều
def default(texts):
    texts = texts.replace('- ',"|||")
    texts = texts.replace('"',"|||")
    texts = texts.replace("'","|||")
    texts = texts.replace('\n',"|||")
    texts = texts.replace('.',"|||")
    texts = texts.replace('...',"|||")
    texts = texts.replace(',',"|||")
    texts = texts.replace(':',"|||")
    texts = texts.replace('|',"|||")
    texts = texts.replace('/',"|||")
    texts = texts.replace('?',"|||")
    texts = texts.replace(';',"|||")
    texts = texts.replace('!',"|||")
    texts = texts.replace('(',"|||")
    texts = texts.replace(')',"|||")
    texts = texts.replace('[',"|||")
    texts = texts.replace(']',"|||")
    texts = texts.replace('{',"|||")
    texts = texts.replace('}',"|||")
    return texts
# đọc file sau đó chia thành các đơn vị nhỏ < câu
def splitFile(filename):
    f=open(filename,'r',encoding='UTF-8')
    results=f.read()
    results = default(results)
    out=results.split('|||')
    while((' ') in out):
        out.remove(' ')
    while(('') in out):
        out.remove('')
    return out
print(splitFile("input1.txt"))

# trái sang phải từ dài nhất có nghĩa. Kết quả trả về danh sách các từ
def tokenizer(text, dict, is_show=False):
    input1=text.split(" ")
    words=[]
    s=0
    while True:
        #Số kí tự đã tách
        e=len(input1)
        while e>s:
            tmp_word=input1[s:e]
            is_word=""
            for item in tmp_word:
                is_word+=item+" "
            is_word=is_word[:-1]
            e-=1
            if is_word.lower() in dict:
                words.append(is_word)
                break
            if e==s:
                words.append(is_word)
                break
        if e>=len(input1):
            break
        if is_show:
            print("s = ",s)
            print("e = ",e)
            print(words[len(words)-1])
            print(" "*100)
        s=e+1
    return words

#nối lại thành đơn vị string trước đó
def restore(words):
    result_list=[]
    result_string=""
    for item in words:
        result_list.append(item.replace(" ", "_"))
    for item in words:
        result_string+=(item.replace(" ", "_"))
        result_string+=" "
    return result_string
#Mỗi câu sẽ được chia thành danh sách các từ
def listWord_sentence(filename, sentence):
    with open(filename, 'r', encoding='UTF-8') as f:
        l_strip = [s.strip() for s in f.readlines()]
    tt=""
    list_word = []
    for i in sentence:
        words = tokenizer(i, l_strip)
        list_word.append(words)
    return list_word
def restoreAll_sentence(list_word):
    tt=""
    for i in list_word:
        tt+=restore(i)
    return tt

#trả về list nhiều đoạn với dạng chữ_chữ thành từ
def Main(filename, sentence):
    with open(filename, 'r', encoding='UTF-8') as f:
        l_strip = [s.strip() for s in f.readlines()]
    tt=""
    for i in sentence:
        words = tokenizer(i, l_strip)
        CountWord(words)
        string_restore = restore(words)
        tt+= string_restore
    #test1=tokenizer(default(texts), l_strip)
    return tt

def listAll_word(fileIn, fileDict):   
    sentence = splitFile(fileIn)
    print(sentence)
    list_word = listWord_sentence(fileDict, sentence)
    list_All_word=[]
    for i in list_word:
        list_All_word.extend(i)
    print()
    while(' ' in list_All_word):
        list_All_word.remove(' ')
    while('' in list_All_word):
        list_All_word.remove('')
    return list_All_word

def countWord(list_All_Word):
    return len(list_All_Word)

def frequencyWord(word, list_All_word):
    s=0
    for i in list_All_word:
        if(i.lower() == word.lower()):
            s+=1
    return s

def maxFrequency_word(list_All_word):
    max_=0
    #print("Danh sách các từ trong văn bản là:")
    #print(list_All_word)
    temp=list_All_word[:]
    for i in range(len(temp)):
        temp[i]=temp[i].lower()
    max_word=[]
    max_word.append(0)
    value_word=[]
    for i in range(len(temp)):
        t=temp.count(temp[i])
        if(max_<=t and temp[i] not in value_word):
            max_= t
            max_word.append(i)
            value_word.append(temp[i])
    ttt=[]
    for i in max_word:
        if(temp.count(temp[i])==max_ ):
            ttt.append(i)
    print("Từ xuất hiện nhiều nhất : tần suất")
    for i in ttt:
        print(list_All_word[i], ": ",max_)

#plit sentence

import re

def terminal(texts):
    texts = texts.replace('- ',"|||- ")
    texts = texts.replace('... ',"... |||")
    texts = texts.replace('.\n',".|||")
    texts = texts.replace('...\n',"...|||")
    #texts = texts.replace('. ',".|||")
    texts = texts.replace('... ',"...|||")
    texts = texts.replace('? ',"?|||")
    texts = texts.replace('?\n',"?|||")
    texts = texts.replace('; ',";|||")
    texts = texts.replace('! ',"!|||")
    texts = texts.replace(';\n',";|||")
    texts = texts.replace('!\n',"!|||")
    texts = texts.replace(':\n',":|||")
    texts = texts.replace('\n',"|||")
    return texts

def checkVietHoa(text):
    list1=list(text)
    for i in range(len(text)):
        if(text[i]=='.'):
            if(i+2<len(text)):
                if(text[i+1]==' '):
                    if(text[i+2]<='a' or text[i+2]>= 'z'):
                        list1[i+1]='|'
    text=''.join(list1)
    text=text.replace("|", "|")
    return text.split("|")
def Complete(list_text):
    result=[]
    for i in list_text:
        result.extend(checkVietHoa(i))
    return result
def splitSentence(filename):
    f = open(filename, 'r', encoding = 'utf-8')
    data = f.read()
    data=terminal(data)
    data = data.split('|||')
    for i in data:
        if(i=="" or i == " " or i=='\n'):
            data.remove(i)
    list1 = Complete(data)

    for i in list1:
        if(i=="" or i == " " or i=='\n'):
            list1.remove(i)
    print(list1)
    return len(list1)

list_All_Word = listAll_word("input1.txt", "dictionary.txt")
print(list_All_Word)
print("Tổng số từ là: ", countWord(list_All_Word))

maxFrequency_word(list_All_Word)

value="khảo"
print("Số lần xuất hiện của từ :", value,": trong đoạn là:", frequencyWord(value, list_All_Word))
value="khảo sát"
print("Số lần xuất hiện của từ :", value,": trong đoạn là:", frequencyWord(value, list_All_Word))
value = input("Nhập từ cần đếm:")
print("Số lần xuất hiện của từ :", value,": trong đoạn là:", frequencyWord(value, list_All_Word))
#test split sentence
print()
countSentence = splitSentence("taiSaoPhaiHoc.txt")
print()
print("Số câu của bài trên là:", countSentence)









