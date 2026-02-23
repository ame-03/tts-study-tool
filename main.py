from splitter import split_text
from tts_engine import synthesize
from player import play_audio

def main():
    text = "And this heat, this energy, it's always on, it's clean, and it actually holds our whole world together."

    chunks = split_text(text, max_words=15)

    first_chunk = chunks[0]

    filename = "output.mp3"

    synthesize(first_chunk, filename)
    play_audio(filename)

if __name__ == "__main__":
    main()