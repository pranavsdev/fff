import requests

def pickanswer(text,tonumber):
    file = open("sample_intents.csv", "r")

    print("text>>",text)
    text_fields = text.split("+")
    input_words = []

    for i in range(0, len(text_fields)):
        print(text_fields[i])
        input_words.append(text_fields[i])    

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
    #sendSMS(answer,tonumber)


def sendSMS(text,tonumber):

    url = "https://api-prd.kpn.com/communication/nexmo/sms/send"

    payload = "from=VIRTUAL_NUMBER&to="+tonumber+"&text="+text
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Authorization': "Bearer YOUR_BEARE_TOKEN",
        'User-Agent': "PostmanRuntime/7.17.1",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "ae0d9bff-7ca8-4988-a6fd-083f0727f1de,90d43f4e-fd63-485b-944e-21a5ce7d89ee",
        'Host': "api-prd.kpn.com",
        'Accept-Encoding': "gzip, deflate",
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
#sendSMS()