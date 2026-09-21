import subprocess

my_input=input("Enter anything you want to hear: ")
new_vocals=f"Initiating {my_input}"
subprocess.run(
    [

        "piper",
        "--model",
        "voices/en_US-lessac-medium.onnx",
        "--output_file",
        "voice.wav"
    ],
    input=new_vocals.encode()
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

if my_input=="open firefox" :
    subprocess.run(["firefox"],
                   timeout=20
    )

# subprocess.run(["firefox"],
#                  timeout=10
#                  )
