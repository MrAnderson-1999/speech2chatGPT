import speech_recognition as sr
import logging
import requests
import os
logging.basicConfig(filename="functions.log", level=logging.DEBUG, filemode='a', format='%(asctime)s %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


def mic_test():
    r = sr.Recognizer()
    m = sr.Microphone()
    try:
        print("Testing surroundings")
        with m as source:
            r.adjust_for_ambient_noise(source)
        print("Set minimum energy threshold to {}".format(r.energy_threshold))
        while True:
            print("Say something!")
            with m as source:
                audio = r.listen(source)
            print("Got it! Test complete...")
            try:
                # recognize speech using Google Speech Recognition
                value = r.recognize_google(audio)
                if len(value) != 0:
                    print("You said {}".format(value))
                    break
            except sr.UnknownValueError:
                print("Oops! Didn't catch that")
            except sr.RequestError as e:
                print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
        return True
    except KeyboardInterrupt:
        pass


def get_voice_input():
    r = sr.Recognizer()
    m = sr.Microphone()
    try:
        print("Testing surroundings")
        with m as source:
            r.adjust_for_ambient_noise(source)
        print("Set minimum energy threshold to {}".format(r.energy_threshold))
        while True:
            print("Say something!")
            with m as source:
                audio = r.listen(source)
            print("Got it! Test complete...")
            try:
                # recognize speech using Google Speech Recognition
                value = r.recognize_google(audio)
                if len(value) != 0:
                    print("You said {}".format(value))
                    return value
            except sr.UnknownValueError:
                print("Oops! Didn't catch that")
            except sr.RequestError as e:
                print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
    except KeyboardInterrupt:
        pass


def openai_request(text):
    api_key = os.environ.get("OPENAI_API_KEY")

    url = "https://api.openai.com/v1/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(api_key)
    }

    payload = {
        "model": "text-davinci-003",
        "prompt": "{}".format(text),
        "temperature": 0,
        "max_tokens": 100
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        logging.debug(f"Error: {response.json()}")
        print(f"Error: {response.json()}")
    else:
        return response.json()["choices"][0]["text"]