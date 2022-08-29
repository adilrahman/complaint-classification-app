import pandas as pd
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from utils import product_classifier, sub_product_classifier, issue_classifier, sub_issue_classifier

app = FastAPI()

def save_results(result : dict):
    '''
    description:
        it save the results in results.csv
    '''
    text = f'"{result["complaint"]}","{result["product"]}","{result["sub_product"]}","{result["issue"]}","{result["sub_issue"]}"\n'
    with open("./results.csv","a") as f:
        f.write(text)



def response(complaint : str) -> str:
    '''
    description:
        it predict the results
    '''
    data = {"Consumer complaint narrative" : str(complaint),}
    data = pd.DataFrame(data,index=[0])

    #prediction
    product = product_classifier.predict(data = data)
    sub_product = sub_product_classifier.predict(data = data)
    issue = issue_classifier.predict(data = data)
    sub_issue = sub_issue_classifier.predict(data = data)

    print(product)
    print(sub_product)
    print(issue)
    print(sub_issue)

    predictions = {
         "product"     : product,
         "sub_product" : sub_product,
         "issue"       : issue,
         "sub_issue"   : sub_issue  
    }

    return predictions
 

class Request(BaseModel):
    complaint : str


@app.post("/predict")
def predict(req : Request):
    complaint = str(req.complaint)
    predictions = response(complaint=complaint)

    ## saving results in results.csv file 
    result = predictions.copy()
    result["complaint"] = complaint
    save_results(result)

    return predictions 

@app.get("/")
def home():
    return {"msg" : "hello"}

if __name__ == "__main__":
    uvicorn.run(app)
   
