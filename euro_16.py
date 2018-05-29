#5/28/18 
#2016 European Championships 
wc14q=pd.read_csv("results-qualifiers.csv")
wc14q['t1'],wc14q['t2']=zip(*wc14q["result"].str.split(':').tolist())
len(wc14q) #268 matches 
wc14q.head(3)
wc14q.info() 

wc14q.t1=pd.to_numeric(wc14q.t1,errors='coerce')
wc14q.t2=pd.to_numeric(wc14q.t2,errors='coerce')

#score differential 
wc14q['score_diff_t1']=wc14q['t1']- wc14q['t2']
wc14q['score_diff_t2']=wc14q['t2']-wc14q['t1']
type(wc14q)
wc14q.to_csv("wc14q.csv")

#dates extracted
wc14q1=pd.read_csv("wc14q1.csv")
wc14q1['match_date'].unique() #unique months 

def date_weighter(date):
    if date==11:
        return 0.9
    if date==10:
        return 0.8
    if date==9:
        return 0.7
    if date==6:
        return 0.4
    if date==3:
        return 0.1

wc14q1['date_score']=wc14q1['match_date'].apply(date_weighter) 

#weighted score differentials 
wc14q1['sd1_weight']=wc14q1['score_diff_t1']*wc14q1['date_score']
wc14q1['sd2_weight']=wc14q1['score_diff_t2']*wc14q1['date_score']
wc14q1.head(4)
wc14q1.to_csv("wc14q1.csv")

#euro cup 2016 (added team ratings) 
euro16=pd.read_csv("euro_2016.csv",encoding="latin-1")
euro16x=euro16[["home","away","score_diff","home_win","home_score_diff","home_score_diff_date","away_score_diff","away_score_diff_date"]]
euro16x.info() 

# build a simple random forest model
euro16x.describe() 
'''
51 games 
'''
#one-hot-encoding
features=pd.get_dummies(euro16x['home_win'])
type(features)
features=features.values 
euro16x=euro16x.values 
euro16x.shape 

X=euro16x[:,4:8]
y=euro16x[:,3]
y=y.astype('int') 

from sklearn.ensemble import RandomForestClassifier
rf_euro=RandomForestClassifier(n_estimators=500)
rf_euro.fit(X,y)
rf_probs=rf_euro.predict_proba(X)

#merge probability with euro cup results
final_euro_probs=np.column_stack([euro16x,rf_probs])
final_euro_probs.shape 
final_euro_probs1=final_euro_probs[:,[0,1,3,8,9,10]]
final_euro_probs1 

###with train test split (check probability accuracy)
from sklearn.metrics import accuracy_score

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.35)
rf_euro1=RandomForestClassifier(n_estimators=500)
rf_euro1.fit(X_train,y_train)
rf_probs1=rf_euro.predict_proba(X_test)