import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
output_txt = sys.argv[3]
suffix_txt = sys.argv[4]
predicted_verb_list = sys.argv[5]
verbList = sys.argv[6]
letter=""
newString = [None]*0
myList = [None]*0
extracted_verb_list = [None]*0
j=0
ch = ['া','ো','ি','ী','ু','ূ','ৃ','ৄ','ে','ৈ','ৌ','ৗ']


with open(input_file,'r', encoding='utf-8') as file:
    data = file.read().replace(',',' ').replace('।',' ').replace('‘',' ').replace('’',' ').replace('?',' ').split(' ')
    for line in data:
        for i in range(len(line)):
           # print(line[i])
            if line[i]  not in ch:
               a=  line[i].replace(line[i],'.')
               letter += a
            else:
                letter += line[i]
        newString.append(letter)
        letter = ""
        #print(line)
    #print(newString)
    #print(len(newString))
    #print(len(data))

with open(output_txt,'r',encoding='utf-8') as compare_file:
    predicted_data = compare_file.read().replace(',',' ').split(' ')
   # print('predict: %s'%predicted_data)
    for output in newString:
        if output in predicted_data:
            a=1
            #print(data[newString.index(output)])
           # myList.append(data[newString.index(output)])

newlist = [None]*0

for i in myList:
    if i not in newlist:
        newlist.append(i)
#print("New List")
#print(newlist)


import re
#print('suffix')
with open(suffix_txt,'r',encoding='utf-8') as suffix_file:
    suffix_data = suffix_file.read().split('\n')
    for word in data:
        for suffix in suffix_data:
            if word.endswith(suffix):
                word = re.sub(suffix+'$', '', word)
               # print(word)
                myList.append(word)
                break


for i in myList:
    if i not in newlist:
        newlist.append(i)
#print("Extracted Verb List")
#print(newlist)
with open(predicted_verb_list, 'w', encoding='utf-8') as myfile:
    myfile.write('\n'.join(newlist))

with open(verbList,'r',encoding='utf-8') as verbList_file:
    verbList_data = verbList_file.read().split(' ')

    for word in data:
        if word in verbList_data:
            if word != '':
                extracted_verb_list.append(word)
        elif word in myList:
            if word != '':
                extracted_verb_list.append(word)


#print("Final Extracted Verb List :")
#print(extracted_verb_list)




with open(output_file, 'w', encoding='utf-8') as myfile:
    myfile.write('\n'.join(extracted_verb_list))
    myfile.close()


#
#
# def fileExists(file):
#     try:
#         f = open(file,'r')
#         f.close()
#     except FileNotFoundError:
#         return False
#     return True
# def isLineEmpty(line):
#     return len(line.strip()) < 1
# def removeEmptyLines(file):
#     lines = []
#     if not fileExists(file):
#         print ("{} does not exist ".format(file))
#         return
#     out = open(file,'r')
#     lines = out.readlines()
#     out.close()
#     out = open(file,'w')
#     t=[]
#     for line in lines:
#         if not isLineEmpty(line):
#             t.append(line)
#     out.writelines(t)
#     out.close()
#
#
#
# removeEmptyLines('Extracted_verb_list.txt')

#
# verb_past = [None]*0
# with open('past.txt','r',encoding='utf-8') as pastfile:
#     past_suffix = pastfile.read().split('\n')
#     pastfile.close()
# #print('suffix')
# #print(past_suffix)
#
#
# with open('Extracted_verb_list.txt', 'r', encoding='utf-8') as myfile:
#     my_data = myfile.read().split('\n')
#     myfile.close()
# #print('mydata')
# #print(my_data)
# for suffix in past_suffix:
#    # print('add')
#     #print(data)
#     for data in my_data:
#         if data.endswith(suffix):
#             verb_past.append(data)
#
# #print('past')
# #print(verb_past)
#
# with open('Past_verb_list.txt', 'w', encoding='utf-8') as myfile:
#     myfile.write('\n'.join(verb_past))
#     myfile.close()
#
#
# with open('future.txt','r', encoding='utf-8') as futureSuffixFile:
#     future_suffix = futureSuffixFile.read().split('\n')
#     futureSuffixFile.close()
# verb_future = [None]*0
# #print(future_suffix)
# for suf in future_suffix :
#     for ve in my_data:
#         if ve.endswith(suf):
#             verb_future.append(ve)
#
# #print('future')
# #print(verb_future)
#
# with open('Future_verb_list.txt', 'w', encoding='utf-8') as myfile:
#     myfile.write('\n'.join(verb_future))
#     myfile.close()
# verb_future_past = verb_past[:]
#
# for v in verb_future:
#     verb_future_past.append(v)
# #print('future and past')
# #print(verb_future_past)
#
# verb_present = [None]*0
#
# for d in my_data:
#     if d not in verb_future_past:
#         verb_present.append(d)
# #print('present')
# #print(verb_present)
# with open('Present_verb_list.txt', 'w', encoding='utf-8') as myfile:
#     myfile.write('\n'.join(verb_present))
#     myfile.close()