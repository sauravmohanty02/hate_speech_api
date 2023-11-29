import pandas as pd 
import numpy as np
from flask import Flask , request , jsonify , render_template 
from sklearn.feature_extraction.text import CountVectorizer
from cuss_inspect import predict
import pickle 

# create flask 
app = Flask(__name__) 

#load model 
model = pickle.load(open('model.pkl','rb'))

@app.route('/predicter',methods=['POST'])
def predicter() :
    json_ = request.json 
    # print(json_['abc'])
    x = json_['abc']
    # query_df = pd.DataFrame(json_['abc'])
    # return jsonify({'prediction': prediction})
    y=predict(x)
    if(y==0):
        return("No Hate and Offensive Speech")
    else:
        return("Hate Speech")
    

if __name__ == "__main__" :
    app.run(debug = True)

