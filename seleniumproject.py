import subprocess

my_input=input("Enter anything you want to hear: ")
subprocess.run(
    [

        "piper",
        "--model",
        "voices/en_US-lessac-medium.onnx",
        "--output_file",
        "voice.wav"
    ],
    input=my_input.encode()
)

subprocess.run(
    [

            "ffplay",
            "-nodisp",
            "-autoexit",

            "voice.wav"
        ],
        check=True
)

