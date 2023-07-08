import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from tkinter import *

df=pd.read_csv('K:/anumayank/PYTHON IMPORT AND IMP FILES(CLASSROOM)/dataset/dataset/Restaurant_Reviews.txt',delimiter='\t')
cv=CountVectorizer(stop_words='english')

mnb=MultinomialNB()

def mytrain():
	
	X=cv.fit_transform(df.Review).toarray()
	y=df.iloc[:,1].values
	mnb.fit(X,y)

def mypredict():
	msg=e.get()
	X_test=cv.transform([msg]).toarray()
	pred=mnb.predict(X_test)
	if(pred[0]==0):
		outlabel1.configure(text=pred[0],fg='red')
	else:
		outlabel1.configure(text=pred[0],fg='green')
	
root=Tk()
root.state('zoomed')
root.configure(background='yellow')
	
title=Label(root,text='Review Detection',bg='yellow',font=('',40,'bold'))
title.place(x=200,y=10)	

label1=Label(root,text='Enter Msg: ',fg='blue',bg='yellow',font=('',20,'bold'))
label1.place(x=200,y=200)

e=Entry(root,font=('',15,'bold'))
e.place(x=350,y=205)

b=Button(root,text='Predict',command=mypredict,font=('',15,'bold'))
b.place(x=400,y=250)

outlabel1=Label(root,bg='yellow',font=(' ',15,'bold'))
outlabel1.place(x=350,y=350)

mytrain()
root.mainloop()