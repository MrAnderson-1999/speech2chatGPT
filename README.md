# Voice-based OpenAI API
This is a python script that uses the Google Speech Recognition library to recognize speech and send it as a prompt to the OpenAI API. It then receives a response and prints it in the console.
![](https://github.com/Leonavshalom/speech2chatGPT/speechGPT.gif)


Requirements
-
- Python 3
- SpeechRecognition pip install SpeechRecognition
- requests pip install requests
- OpenAI API key

Usage
-
- **Clone** the repository
```
git clone https://github.com/<username>/voice-openai-api.git
```


- **Install** the requirements
```
pip install -r requirements.txt
```

- **Set** the OpenAI API key as an environment variable
```
export OPENAI_API_KEY=sk-kdkHi0YxxxxxxxxxxxxxxxxxxxxxxxxxxxXuBx29cM1o
```

- **Run** the script
```
python main.py
```
- Speak a question when prompted

Note
-
- Make sure you have a working microphone
- Make sure to use the correct model name in the openai_request function.
- Make sure to have the correct api key, the current one is only an example.
