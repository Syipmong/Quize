import random
import time
import speech_recognition as sr

def mic_speech_recognition(recognizer, microphone):
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError('There is an error with the Recogniser configuration')
    if not isinstance(microphone, sr.Microphone):
        raise TypeError('an error occured with the Microphone configuration')
    

    with microphone as source :
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    response = {
        "success": True
        "error": None
        "transcription": None
    }

    try: 
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError

        response["success"] = False
        response["error"] = "API Unavailable"
    except sr.UnknownValueError

        response["error"] = "Unable to recognize your speech"
    
    return response

if __name__ = "__main__":

    OBJECTS = ["cashew", "apple", "pineapple", "coconut", "banana", "orange", "mango"]
    GUESSES = 3
    LIMIT = 10


    recognizer = sr.Recogniser()
    microphone = sr.Microphone()

    word = random.choice(OBJECTS)


    instructions = (
         "I'm thinking of one of these words:\n"
        "{words}\n"
        "You have {n} tries to guess which one.\n"
    ).format(words=', '.join(OBJECTS), n=GUESSES)
    
    print(instructions)
    time.sleep()
    
