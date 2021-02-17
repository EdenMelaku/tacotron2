'''
one of the limitations of this model is that it cannot read abbriviations or a single alphabetic character along or separately
so i am just gonna try giving every alphabet letter a corresponding word. eg B--> bee
'''

'''
besides the above limitation the model cannot generate sentences that are longer than 11seconds when read, so approximately the model can read approximately 20 words with in 11 sec.
we will do a number of steps to segment a given article in several steps

step 1 - split an article in to a number of sentences by using "." or period, in english language a sentence ends by a dot.
step 2- we will get a number of sentences by aoolying step one, if there is any sentence longer than 20 sec then we will apply step 2 which is 
        separating sentences by comma "," , only applies if a comma exists in the sentence.
step 3- is sentntence is not reduced in to a number of short sentence segments by step 2 then we will apply step 3 which is 
        separating a sentence if there exists a conjuctive word in it , we apply the splitting consicutively in the following order
        and, that, but, or, as, if, when, than, because, while, where, after, so, though, since, until, whether, before, although, nor, like, once, unless, now, except

'''
import math
#letters=['A.', 'bee', 'see', 'dee', 'ie', 'ef', 'ji', 'ach', 'ay', 'jay', 'kei', 'el', 'em', 'en', 'ow', 'pee', 'kiw', 'are', 'aiS', 'tea', 'you', 'vee', 'double you', 'eks', 'waai.', 'zed']
def generateSegemnts(text):
   sentences=text.split(".")
   sentenceList=[]

   for s in sentences:
       #print("set--- "+s)
       queue=[]
       if(len(s.split(" "))>19):
           split_by_comma=s.split(",")
           for i in split_by_comma:
               if(len(i.split(" "))>19):
                   splited_by_conj=split_by_conjuction(i.split(" ")).split("*")
                   for sent in splited_by_conj:
                       if (len(sent.split(" ")) > 19):
                           splited_by_comma=splitt_by_word_count(sent.split(" "))
                           sentenceList.extend(splited_by_comma.split("*"))
                       else:
                           sentenceList.append(sent)

               else:
                   sentenceList.append(i)
       else:
           sentenceList.append(s)

   return sentenceList
array_of_sent=[]
def splitt_by_word_count(text):
    newtex=text
    x= math.ceil(len(text)/15)
    y= math.floor(len(text)/x)
    i=y
    print("length = "+str(len(text)))
    print("x = " + str(x))
    print("y = " + str(y))
    j=0
    while(j<x-1):
        newtex.insert(i+j,"*")
        j+=1
        i+=y
    stringList=""
    text.pop(0)

    for se in text:
        stringList+=se+" "

    return stringList
def split_by_conjuction(text):
    #split by and
    if ("and" in text):
        index = text.index("and")
        text[index] = "and * "
    if ("or" in text):
        index = text.index("or")
        text[index] = "or * "
    if ("but" in text):
        index = text.index("but")
        text[index] = "but * "
    if ("because" in text):
        index = text.index("because")
        text[index] = "because * "
    if ("since" in text):
        index = text.index("since")
        text[index] = "since * "
    if ("so" in text):
        index = text.index("so")
        text[index] = "so * "
    if ("than" in text):
        index = text.index("than")
        text[index] = "than * "
    if ("that" in text):
        index = text.index("that")
        text[index] = "that * "
    stringList=""
    for se in text:
        stringList += se + " "


    return stringList


if __name__=="__main__":
    tex="Unfortunately, list has a few shortcomings. " \
        "The biggest issue is that it can run into speed issue as it grows. " \
        "then Python needs to do some memory allocations This can lead to some append() calls taking much longer than other ones or in other words this can be explained and also i believe i can do it and everyone can do it too."\
        "The items in list are stored next to each other in memory, " \
        "if the stack grows bigger than the block of memory that currently hold it. "

    tex2=""
    sentences= generateSegemnts(tex)
    for s in sentences:
        print(s)