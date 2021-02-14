'''
one of the limitations of this model is that it cannot read abbriviations or a single alphabetic character along or separately
so i am just gonna try giving every alphabet letter a corresponding word. eg B--> bee
'''
import math
letters=['A.', 'bee', 'see', 'dee', 'ie', 'ef', 'ji', 'ach', 'ay', 'jay', 'kei', 'el', 'em', 'en', 'ow', 'pee', 'kiw', 'are', 'aiS', 'tea', 'you', 'vee', 'double you', 'eks', 'waai.', 'zed']
def generateSegemnts(text):
   sentences=text.split(". ")
   sentenceList=[]
   for s in sentences:
       queue=[]
       if(len(s.split(" "))>19):
           split_by_comma=s.split(",")
           for i in split_by_comma:
               if(len(i.split(" "))>19):
                   #arr=[" "]
                   arr=splitt(i.split(" "),list())
                   s=' '.join(map(str, arr))
                   sentenceList.append(s)

               else:
                   sentenceList.append(i)
       else:
           sentenceList.append(s)


   return sentenceList

def splitt(text,ar):
    arr=[]
    arr.append(ar)
    arr.append(text[:int(len(text)/2)])
    if(len(arr[-1])>15):
        temp=arr[-1]
        arr.remove(-1)
        a=splitt(temp,arr)
    arr.append(text[int(len(text)/2):])
    if (len(arr[-1]) > 15):
        temp = arr[-1]
        arr.remove(-1)
        a=splitt(temp, arr)

    stringList=[]
    #arr.pop(0)
    arr=arr[1:]
    for se in arr:
        stringList.append(" ".join(se))

    return stringList







if __name__=="__main__":
    tex="Unfortunately, list has a few shortcomings. " \
        "The biggest issue is that it can run into speed issue as it grows. " \
        "The items in list are stored next to each other in memory, " \
        "if the stack grows bigger than the block of memory that currently hold it, " \
        "then Python needs to do some memory allocations This can lead to some append() calls taking much longer than other ones."

    tex2=""
    sentences= generateSegemnts(tex)
    for s in sentences:
        print(s)