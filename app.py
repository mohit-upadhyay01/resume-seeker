import numpy as np
import urllib.request
import re

from collections.abc import Mapping

from flask import Flask, request, jsonify, render_template, send_file, send_from_directory, session

app = Flask(__name__)

app.secret_key = 'dljsaklqk24e21cjn!Ew@@dsa5'


def listToString(s):
 
    str1 = "" 
    for ele in s:
        str1 += ele
    return str1


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [str(x) for x in request.form.values()]


    name = list(int_features[0].replace(" ", "_"))                    # name =  "Samarth_Xnxx_Bkkkkfgd_"
    rollno = int_features[1].replace(" ", "_")                        # rollno = "B21XX001_"

    # rollno[0].upper()
    rollno = rollno.upper()
    if rollno[-1] != "_":
        rollno += "_"
    
    name[0] = name[0].upper()
    k=0;    
    for i in range(len(name)):
        if k==1:
            name[i] = name[i].upper()
            k=0
        if name[i] == "_":
            k=1
    if k==0:
        name += '_'

    # return render_template('index.html', prediction_text=str(listToString(name) + '  --  ' + rollno ))
    name = listToString(name)
    # print(listToString(name) ,"  ", rollno[0:8], rollno)

    # https://spc.iitj.ac.in/media/resume/Lokesh_Tanwar_B21EE035_5411_IITJodhpur.pdf

    

    s = "https://spc.iitj.ac.in/media/resume/" +  name + rollno      #"https://spc.iitj.ac.in/media/resume/Lokesh_Tanwar_B21EE035_'
    
    end = "_IITJodhpur.pdf"
    print(s)
    l = "uploads/" + rollno + ".pdf"

    # i = 5411
    # urllib.request.urlretrieve(s+str(i)+end, l)
    # print(s+str(i)+end)

    for i in range(999, 9999):
      try:
        if i < 10:
            # urllib.request.urlretrieve(s+"000"+str(i)+end, "raunak.pdf")
            urllib.request.urlretrieve(s+"000"+str(i)+end, l)
            break
        elif i < 100:
            urllib.request.urlretrieve(s+"00"+str(i)+end, l)
            break
        elif i < 1000:
            urllib.request.urlretrieve(s+"0"+str(i)+end, l)
            break
        else:
            urllib.request.urlretrieve(s+str(i)+end, l)
            break
      except:
        pass

    #   if(i%50==0):
    #     print(i)

    print(name, rollno)
    session["n"]=name
    session["r"]=rollno

    return render_template('test1.html')

@app.route('/download_file')      #faltu, just to understand
def download_file():     
    pat = "uploads/" + "block_diag" + ".pdf"
    return send_file(pat)
    # return send_file(pat, as_attachment=True)
    # return send_from_directory(app.config['UPLOAD_FOLDER'], 'file.pdf')


@app.route('/downloadss')
def downloadss():     
    try:
        pat = "uploads/" + session.get("r",None) + ".pdf"
        return send_file(pat)
    except:
        pat = "uploads/iitj.png"
        return send_file(pat)



if __name__ == "__main__":
    app.run(host='localhost',port=80)
