import speech_recognition as sr
import logging
import requests
logging.basicConfig(filename="functions.log", level=logging.DEBUG, filemode='a', format='%(asctime)s %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


def get_voice_input():
    r = sr.Recognizer()
    m = sr.Microphone()

    try:
        logging.debug("A moment of silence, please...")
        with m as source:
            r.adjust_for_ambient_noise(source)
        logging.debug("Set minimum energy threshold to {}".format(r.energy_threshold))
        while True:
            logging.debug("Say something!")
            with m as source:
                audio = r.listen(source)
            logging.debug("Got it! Now to recognize it...")
            try:
                # recognize speech using Google Speech Recognition
                value = r.recognize_google(audio)
                if len(value) != 0:
                    logging.debug("You said {}".format(value))
                    return value
            except sr.UnknownValueError:
                logging.debug("Oops! Didn't catch that")
            except sr.RequestError as e:
                logging.debug("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
    except KeyboardInterrupt:
        pass


def openai_request(text):
    api_key = "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"

    url = "https://api.openai.com/v1/engines/davinci/completions"

    data = {
        "prompt": text,
        "temperature": 0.5,
        "max_tokens": 100
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code != 200:
        logging.debug(f"Error: {response.json()}")
    else:
        return response.json()