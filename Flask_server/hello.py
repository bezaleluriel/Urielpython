import pandas as pd
from flask import Flask

# name of the module is __name__
app = Flask(__name__)


#routing with /
@app.route("/")
def getCars():
    df = pd.read_csv(r'Z:\___advanced python\CARS1.csv')
    json = df.to_json()
    return json
