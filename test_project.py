from fastapi.testclient import TestClient
from backend.app.model import make_features,forecast
from backend.app.main import app

def test_model():
    rows=[[100+i,1000+i*10] for i in range(30)]
    X,y=make_features(rows)
    assert len(X)==len(y)
    pred,d=forecast(rows)
    assert pred>0 and d in {"UP","DOWN"}

def test_api():
    c=TestClient(app)
    assert c.get("/health").json()["author"]=="Rayyan Anwar"
    rows=[{"close":100+i,"volume":1000+i*10} for i in range(30)]
    assert c.post("/api/v1/forecast",json={"prices":rows}).status_code==200
