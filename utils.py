import requests

def pickanswer(text,tonumber):
    file = open("sample_intents.csv", "r")

    #check if you are getting the expected output, adjust your delimitter
    print("text>>",text)
    text_fields = text.split(" ")
    #text_fields = text.split("+")
    print("text fields",text_fields)
    input_words = []

    for i in range(0, len(text_fields)):
        print(text_fields[i])
        input_words.append(text_fields[i])    
    print("input words: ",input_words)
    predict_answer = {}

    for line in file:
        count = 0
        fields = line.split(",")
        target = fields[0]
        print("target>>>",target)
        for word in input_words:
            print("word: ",word)
            for i in range(1, len(fields)):
                if word in fields[i]:
                    print("fields>>",fields[i])
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
#sendSMS()