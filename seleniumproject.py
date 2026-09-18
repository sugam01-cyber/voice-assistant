import subprocess

my_input="Hello! My name is Alex, and this is a quick test of my voice assistant. Today is September 16th, 2026, and the current time is approximately 9:35 p.m. I can speak naturally, pause between sentences, and handle numbers like 1, 25, 3.14159, and $1,299.99. I can also pronounce words such as “automation,” “authentication,” “PostgreSQL,” “FastAPI,” “Python,” and “artificial intelligence” without sounding robotic. Now, let’s test punctuation: commas, periods, question marks, exclamation marks—and even parentheses (like this). If everything works correctly, the voice should sound clear, smooth, confident, and human, with natural emphasis rather than speaking every word at exactly the same speed. Finally, here’s a slightly tricky sentence: “The quick brown fox jumps over the lazy dog,” while a developer quietly types print('Hello, world!') in the background. If you can hear every word clearly, congratulations—the voice pipeline is working!"
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
