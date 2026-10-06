import numpy as np
from sklearn.ensemble import RandomForestRegressor

def make_features(prices):
    x=np.asarray(prices,dtype=float); X=[]; y=[]
    for i in range(10,len(x)):
        c=x[i-10:i,0]; v=x[i-10:i,1]
        r=np.diff(c)/c[:-1]
        X.append([c[-1],c.mean(),c.std(),r[-1],r.mean(),c[-5:].mean(),c.mean(),v[-1],v.mean()])
        y.append(x[i,0])
    return np.asarray(X),np.asarray(y)

def forecast(prices):
    X,y=make_features(prices)
    if len(X)<5: raise ValueError("At least 15 observations are required.")
    split=max(3,int(len(X)*.8))
    model=RandomForestRegressor(n_estimators=100,random_state=42,n_jobs=-1)
    model.fit(X[:split],y[:split])
    pred=float(model.predict(X[-1].reshape(1,-1))[0])
    prev=float(prices[-1][0])
    return pred,("UP" if pred>=prev else "DOWN")
