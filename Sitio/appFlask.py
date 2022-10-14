
from crypt import methods
from distutils.log import debug
import pandas as pd
import numpy as np
import sklearn
import joblib
from appFlask import Flask, render_template,request
app=Flask(__name__ )
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/prediccion', methods=['GET','POST'])
def predict():
      if request.methods =='POST':
        try:
          var_1=float (request.form['var_1'])
          var_2=float (request.form['va:_2'])
          pred_args=[var_1,var_2]
          pred_arr=np.array (pred_args)
          preds=pred_arr.reshape(1,-1)
          modelo=open(". /modelo.pk1","rb")
          modelo_clas=joblib.load(modelo)
          prediccion_modelo=modelo_clas.predict (preds)
          prediccion_modelo=round (float (prediccion_modelo) ,2)
          if prediccion_modelo == 1.0:
            prediccion_modelo = "Aprueba"
          else:
            predicción_modelo = "lo aprueba"
        except ValueError:
          return "Por favor entra nombre válidos"
        return render_template ('prediccion.html',predicion=prediccion_modelo)
      if __name__=='__main__':
        app.run(debug=True)