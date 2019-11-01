# Documentation for APIs
    - SMS : https://developer.kpn.com/marketplace/nexmo-sms-api-documentation
    - Speech to text : https://developer.kpn.com/marketplace/contexta360-speech-text-api-documentation

# About
    This kit give you and idea about two things: 
        - how can you enable a chatbot through sms
        - how can you get the context of the conversation 

# Setup

    - install python (3.7)

    - install miniconda

    - install visual studio code or any other code editor


# Important Files
    - sample-intents.csv : You can save the intents for your chatbot. The first value should be the answer statement followed by words that can be matched against the user's chat value. For example if the input sentence is - 'weather' / 'what is the weather today' then the answer should be 'it is cold'

    - chatbot-app.py : You should execute this file to run the sms-chatbot functionality.

    - speech-sample.json : This file contains the output from Speech-to-text contexta API from /transcripts

    - contexta-vocab.csv : Like the intents file for chatbot this file also contains output context for the matching vocabulary separated with commas(,)

    - context.py :  You should execute this file to get the context from speech-sample.json file


# Execution
    
    - I would recommend creating a conda environment once you have completed the 'Setup'
        ```conda create --name myenv```
    - Choose the environment you created
        ```source activate 'your_conda_env_name'```
        
    - Next:
        (1) pip install Flask
        (2) pip insall flask_restful

    - For chatbot
        ```python chatbot.py```
        You can either host your application on a server that can be availbale on internet. The second option is to expose your local host via ngrok on the port your localhost is running. ```https://dashboard.ngrok.com/get-started```

    - For contexta
        ```python contexta.py```