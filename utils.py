import requests

def pickanswer(text,tonumber):
    with open("sample_intents.csv", "r") as f:
        content = f.readlines()

    #check if you are getting the expected output, adjust your delimitter
    # print("text>>",text)
    text_fields = text.split(" ")
    #text_fields = text.split("+")
    print("text fields",text_fields)
    # input_words = []

    # for word in text_fields:
    #     print(word)
    #     input_words.append(word)  
    # input_words = [w for w in text_fields]  
    # print("input words: ",input_words)
    
    predict_answer = {}
    for line in content:
        count = 0
        fields = line.split(",")
        target = fields[0]
        print("target>>>",target)
        for word in text_fields:
            print("word: ",word)
            if word in fields[1:]:
                print("fields>>",i)
                count += 1
        predict_answer[target] = count

    print("dict>>>",predict_answer)
    answer = max(predict_answer, key=predict_answer.get)
    print("predict>>",answer)    
    sendSMS(answer,tonumber)


def sendSMS(text,tonumber):

    url = "https://api-prd.kpn.com/communication/nexmo/sms/send"

    payload = "from=3197010240299&to="+tonumber+"&text="+text
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Authorization': "Bearer YOUR_TOKEN",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Host': "api-prd.kpn.com",
        'Accept-Encoding': "gzip, deflate",
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
