import joblib
clf_from_joblib = joblib.load("model_dump_data_csv.pkl")
features = [0]*20
classes = [0]*7

def get_features(voice_text):	
    global features
    for i in range(20):
        features[i]=0
    voice_text = voice_text.split(" ")
    for word in voice_text:
        if(word=="back"):
            features[0]=1
        elif(word=="backward"):
            features[1]=1
        elif(word=="break"):
            features[2]=1
        elif(word=="come"):
            features[3]=1
        elif(word=="fast"):
            features[4]=1
        elif(word=="forward"):
            features[5]=1
        elif(word=="go"):
            features[6]=1
        elif(word=="left"):
            features[7]=1
        elif(word=="leftside"):
            features[8]=1
        elif(word=="move"):
            features[9]=1
        elif(word=="quick"):
            features[10]=1
        elif(word=="reverse"):
            features[11]=1
        elif(word=="right"):
            features[12]=1
        elif(word=="rightside"):
            features[13]=1
        elif(word=="slow"):
            features[14]=1
        elif(word=="slowly"):
            features[15]=1
        elif(word=="stop"):
            features[16]=1
        elif(word=="straight"):
            features[17]=1
        elif(word=="take"):
            features[18]=1
        elif(word=="turn"):
            features[19]=1

