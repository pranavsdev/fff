import json

def contextainfo():
    with open('speech-sample.json') as json_file:
        data = json.load(json_file)

        speech = []

        for segmentList in data['SegmentList']:
            for word in segmentList['words']:
                text = word['text']
                speech.append(text)
        pickanswer(speech)

def pickanswer(text):
    file = open("contexta-vocab.csv", "r")

    input_words = text

    predict_answer = {}

    for line in file:
        count = 0
        fields = line.split(",")
        target = fields[0]
        for word in input_words:
            for i in range(1, len(fields)):
                if word in fields[i]:
                    count += 1
        predict_answer[target] = count
    answer = max(predict_answer, key=predict_answer.get)
    print("context in the file is: ",answer)    
    #sendSMS(answer,tonumber)

contextainfo()