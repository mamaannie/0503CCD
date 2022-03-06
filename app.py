#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask
app = Flask(__name__)


# In[2]:


from flask import render_template, request
import joblib
                    
@app.route("/", methods =["GET","POST"])
def index ():
    
    if request.method =="POST":
        income = request.form.get("income")
        age = request.form.get("age")
        loan = request.form.get("loan")
        income = float (income)
        age = float (age)
        income = float (income)
        print(income, age, loan) 
        
        model1 = joblib.load("CCD_DT")
        pred1 = model1.predict([[income, age, loan]])
        s1 = "The default loan base on Decision Tree model is : " + str(pred1)   
        
        model2 = joblib.load("CCD_RF")
        pred2 = model2.predict([[income, age, loan]])
        s2 = "The default loan base on Random Forest model is : " + str(pred2)  
        
        model3 = joblib.load("CCD_GB")
        pred3 = model3.predict([[income, age, loan]])
        s3 = "The default loan base on Gradient Booster model is : " + str(pred3)  
  
        model4 = joblib.load("CCD_Reg")
        pred4 = model4.predict([[income, age, loan]])
        s4 = "The default loan base on Linear Regression model is : " + str(pred4)  
        
        model5 = joblib.load("CCD_NN")
        pred5 = model5.predict([[income, age, loan]])
        s5 = "The default loan base on Neural Network model is : " + str(pred5)  
        
        return(render_template("index.html", result1 =s1, result2 = s2, result3 =s3, result4 = s4, result5 =s5))
    else:
        return(render_template("index.html", result1 ="Please enter", result2 ="your income",result3 ="your age", result4 = "and your loan", result5 ="in the above boxes."))


# In[ ]:


if __name__== "__main__":
    app.run()


# In[ ]:




