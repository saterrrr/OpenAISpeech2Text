# basic Python program that takes user text as an input and prints back an answer from openAI
# press tab and start talking, after you finish press alt to get an answer
import os
import time

import openai
import speech_recognition
import keyboard

# The Recognizer is initialized.
sr = speech_recognition.Recognizer()
openai.api_key = "YOUR_API_KEY"

while True:
    try:
        with speech_recognition.Microphone() as UserVoiceInputSource:
            if keyboard.read_key() == "tab":
                sr.adjust_for_ambient_noise(UserVoiceInputSource, duration=0.5)

                # The Program listens to the user voice input.
                UserVoiceInput = sr.listen(UserVoiceInputSource)
                UserVoiceInput_converted_to_Text = sr.recognize_google(UserVoiceInput, language="en-US")
                UserVoiceInput_converted_to_Text = UserVoiceInput_converted_to_Text.lower()
                query = UserVoiceInput_converted_to_Text

            if keyboard.read_key() == "alt":
                print("Q:" + query)
                query = UserVoiceInput_converted_to_Text
                response = openai.Completion.create(
                    model="text-davinci-002",
                    prompt=query,
                    temperature=0.3,
                    max_tokens=200,
                    top_p=1.0,
                    frequency_penalty=0.0,
                    presence_penalty=0.0
                )
            query = ""
            # time.sleep(2)
            print(response.choices[0].text)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")
