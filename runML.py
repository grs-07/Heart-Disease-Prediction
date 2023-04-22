# sudo -H pip3 install pandas
# sudo -H pip3 install scikit-learn

import pickle
import pandas as pd
import tkinter as tk
from tkinter import ttk


filename = 'heart_disease.h5'
model = pickle.load(open(filename, 'rb'))

data=[[39,1,3,130,100,0,2,100,1,2.2,0,2,2]]
df_test=pd.DataFrame(data,columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
       'exang', 'oldpeak', 'slope', 'ca', 'thal'])

result=model.predict(df_test)


class App:
    def __init__(self, window):
        self.window = window
        self.window.geometry("460x450")
        self.window.maxsize(460,450);self.window.minsize(460,450)
        self.window.title("Predict Heart Disease")
        self.entries = []
        self.result = tk.Label(self.window)
        self.CL = [["Male", "Female"],["Typical Angina", "Atypical Angina", "Non- Anginal pain", "Asymptomatic"],["Yes", "No"],
                   ["Normal", "ST-T wave abnormality", "probable or definite left ventricular hypertrophyby Estes"],["No","YES"],
                   ["up sloping","flat","down sloping"],["0","1","2","3"],["NULL","normal blood flow","fixed defect", "reversible defect"]]
        self.configure()
        self.window.mainloop()

    def getoutput(self):
        combind = [1,2,5,6,8,10,11,12]
        output = []
        for ind, entr in enumerate(self.entries):
            if ind in combind:
                try:output.append(self.CL[combind.index(ind)].index(self.entries[ind].get()))
                except:output.append(0)
            else:
                output.append(int(self.entries[0].get()))
        filename = 'heart_disease.h5'
        model = pickle.load(open(filename, 'rb'))
        data=[output]
        df_test=pd.DataFrame(data,columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach','exang', 'oldpeak', 'slope', 'ca', 'thal'])
        result=model.predict(df_test)
        if result[0] == 1:self.result.config(text="Risk exist for Heart Disease")
        else:self.result.config(text="No Risk exist for Heart Disease")

    def configure(self):
        self.labels = []
        labels = ['Age', 'Sex', 'Chest pain experienced', ' Blood pressure (resting mode in mm/HG)',
                  'Cholesterol (mg/dl)' , 'Blood sugar levels (on fasting > 120)','Electrocardiogram (at rest)',
                  'Maximum heart rate', 'Angina induced', 'ST-depression (on excercise)',
                  'ST segment slope (peak exercise)', ' Major vessels', 'Thalassemia']
        for label in labels:
            self.labels.append(tk.Label(self.window, text = label,pady=5))
        self.entries = [tk.Entry(self.window),ttk.Combobox(state="readonly",values=self.CL[0]),ttk.Combobox(state="readonly",values=self.CL[1]),
                        tk.Entry(self.window),tk.Entry(self.window),ttk.Combobox(state="readonly",values=self.CL[2]),
                        ttk.Combobox(state="readonly",values=self.CL[3]),tk.Entry(self.window),ttk.Combobox(state="readonly",values=self.CL[4]),tk.Entry(self.window),
                        ttk.Combobox(state="readonly",values=self.CL[5]),ttk.Combobox(state="readonly",values=self.CL[6]),
                        ttk.Combobox(state="readonly",values=self.CL[7])]
        index = 0
        self.entries[0].insert(0,"0");self.entries[3].insert(0,"0");self.entries[4].insert(0,"0");self.entries[7].insert(0,"0");self.entries[9].insert(0,"0")
        for labl, entr in zip(self.labels, self.entries):
            labl.grid(row=index,column=0, sticky = tk.W);entr.grid(row=index,column=1) 
            index += 1
        button1  = tk.Button(self.window, text ="Predict", command = self.getoutput)
        button1.grid(row = index, column = 1);index += 1
        self.result.grid(row=index, column=0,columnspan=2)

if __name__=="__main__":
    application = App(tk.Tk())




