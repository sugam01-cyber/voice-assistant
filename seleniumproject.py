import subprocess
import speech_recognition as sr
user_voice=input("enter some texts: ")
new_vocals=f"Initiating {user_voice}"
subprocess.run(
    [
        "piper",
        "--model",
        "voices/en_US-lessac-medium.onnx",
        "--output_file",
        "voicee.wav"
    ],
    input=new_vocals.encode()
)

subprocess.run(
    [
        "ffplay",
        "-autoexit",
        "-nodisp",
        "voicee.wav"
    ],
)
