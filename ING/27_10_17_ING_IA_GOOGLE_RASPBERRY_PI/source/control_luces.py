#!/usr/bin/env python

# Copyright (C) 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from __future__ import print_function

import argparse
import os.path
import json
import RPi.GPIO as GPIO
import time

import google.oauth2.credentials

from google.assistant.library import Assistant
from google.assistant.library.event import EventType
from google.assistant.library.file_helpers import existing_file

#Procesamos lo que la información que ha recogido el asistente de google y emitimos una respuesta
def process_event(event, assistant):
    """Pretty prints events.

    Prints all events that occur with two spaces between each new
    conversation and a single space between turns of a conversation.

    Args:
        event(event.Event): The current event to process.
    """
    print(event)

    if event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED:
        speech_text = event.args["text"]
        print("speech text: " + speech_text)
        GPIO.setup(18,GPIO.OUT)
        if(speech_text == 'light off' or speech_text == 'lights off' or speech_text == 'light of'
            or speech_text == 'lights off' or speech_text == 'lights of'
            or speech_text == 'Light OFF'):
            print("------------")
            print("------------")
            print("Apaga la luz")
            print("------------")
            print("------------")
            GPIO.output(18,GPIO.LOW)
        if(speech_text == 'light on' or speech_text == 'lights on' or speech_text == 'Light ON'):
            print("------------")
            print("------------")
            print("Enciende la luz")
            print("------------")
            print("------------")
            GPIO.output(18,GPIO.HIGH)



def main():
    #Autentificamos nuestra raspberry pi con nuestras credenciales
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--credentials', type=existing_file,
                        metavar='OAUTH2_CREDENTIALS_FILE',
                        default=os.path.join(
                            os.path.expanduser('~/.config'),
                            'google-oauthlib-tool',
                            'credentials.json'
                        ),
                        help='Path to store and read OAuth2 credentials')
    args = parser.parse_args()
    with open(args.credentials, 'r') as f:
        credentials = google.oauth2.credentials.Credentials(token=None,
                                                            **json.load(f))

    #Establecemos el canal de comunicación entre el Google Assistant y el usuario de la Raspberry Pi
    with Assistant(credentials) as assistant:
        for event in assistant.start():
            process_event(event, assistant)


if __name__ == '__main__':

    #Inicializamos el puerto GPIO 18 que es el que usaremos
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT)
    main()
