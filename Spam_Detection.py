import pandas as pd
import numpy as np
import re
email_data=pd.read_csv('spam.csv',encoding='latin1')
email_data=email_data[['v1','v2']]
# print(email_data.head())
# print(email_data[['v1']])

# email_d=np.array(email_data[['v1']])
# email_content=np.array(email_data[['v2']])



#converts pandas dataframe to numpy array
email_data=email_data.values
print(email_data.shape)

postive_spam=dict()
negative_spam=dict()

def bagOfWordsClassification(email_classification,email_content):
    for word in email_content.split():
        if email_classification=='spam':
            postive_spam[word]=postive_spam.get(word,0)+1
            global total_postive
            total_postive+=1
        else:
            negative_spam[word]=negative_spam.get(word,0)+1
            global total_negative
            total_negative+=1
    # print(postive_spam)
    # print(negative_spam)
total_postive=0
total_negative=0
total=0
spam=0
for email in email_data:
    if email[0]=='spam':
        spam+=1
    total+=1
    email[1]=re.sub('[^a-zA-Z]',' ', email[1])
    print(email[1])
    bagOfWordsClassification(email[0],email[1])
print(total,'    ',spam)
pA=spam/total
notpA=(total-spam)/total


def probalityofWord(spam,word):
    if spam:
        if postive_spam.get(word,0.01):
            probaliltiy_postive=postive_spam.get(word,0.01)/total_postive
            return probaliltiy_postive
    else:
        if negative_spam.get(word,0.01):
            probaliltiy_negative=negative_spam.get(word,0.01)/total_negative
            return probaliltiy_negative

def totalProbability(spam,email_content):
    total_probility=1
    for word in email_content.split():
        total_probility*=probalityofWord(spam,word)
    return total_probility

def classify(email):

    isSpam=pA*totalProbability(True,email)
    notSpam=notpA*totalProbability(False,email)

    if isSpam>notSpam:
        print('Spam')
    else:
        print('Not Spam')

classify("WINNER As a valued network customer you have been selected to receive prize reward To claim call Claim code KL Valid hours only")
print(total_negative)
print(total_postive)
