from gtts import gTTS
from pathlib import Path
from mutagen.mp3 import MP3
from utils.console import print_step, print_substep
from rich.progress import track
import os


def save_text_to_mp3(reddit_obj):
    print_step("Saving Text to MP3 files 🎶")
    length = 0

    # Create a folder for the mp3 files.
    Path("assets/mp3").mkdir(parents=True, exist_ok=True)

    if os.getenv("Change_Accent") == "TRUE":
        try:
            tts = gTTS(text=reddit_obj["thread_title"], lang="en", slow=False, tld=os.getenv("LANGUAGE_ACCENT_CODE"))
            print_substep("Changing accent to: " + os.getenv("LANGUAGE_ACCENT_CODE"))
        except ValueError:
            tts = gTTS(text=reddit_obj["thread_title"], lang="en", slow=False, tld="com.au")
            print_substep("The language accent code is not valid. Using Australia.")
    else:
        print_substep("Change Accent is set to FALSE or not set. Using Australia")
        tts = gTTS(text=reddit_obj["thread_title"], lang="en", slow=False, tld="com.au")
    tts.save(f"assets/mp3/title.mp3")
    length += MP3(f"assets/mp3/title.mp3").info.length

    for idx, comment in track(enumerate(reddit_obj["comments"]), "Saving..."):
        # ! Stop creating mp3 files if the length is greater than 50 seconds. This can be longer, but this is just a good starting point
        if length > 50:
            break
        tts = gTTS(text=comment["comment_body"], lang="en")
        tts.save(f"assets/mp3/{idx}.mp3")
        length += MP3(f"assets/mp3/{idx}.mp3").info.length

    print_substep("Saved Text to MP3 files Successfully.", style="bold green")
    # ! Return the index so we know how many screenshots of comments we need to make.
    return length, idx
