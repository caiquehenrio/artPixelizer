#imported libraries

from colorama import Fore, Style, init
from moviepy.editor import VideoFileClip
from PIL import Image
import os
import time

#initialize colorama

init(autoreset=True)

#list of characters for different brightness levels

BRIGHTNESS_CHARS = [" ", ".", "-", ":", "o", "O", "8", "@"]

#function to determine color based on luminosity

def get_color_by_brightness(brightness):

    if brightness < 0.2:
        return Fore.RED
    elif brightness < 0.4:
        return Fore.YELLOW
    elif brightness < 0.6:
        return Fore.GREEN
    elif brightness < 0.8:
        return Fore.CYAN
    else:
        return Fore.WHITE

#function to determine character based on brightness

def get_char_by_brightness(brightness):

    index = int(brightness * (len(BRIGHTNESS_CHARS) - 1))
    return BRIGHTNESS_CHARS[index]

#function that converts a frame to textual art with characters and colors

def frame_to_word_art(frame, new_width=30, scale_factor=0.6):

    frame = frame.convert("L")
    width, height = frame.size
    aspect_ratio = height / width
    new_height = max(1, int(aspect_ratio * new_width * scale_factor))
    frame = frame.resize((new_width, new_height))

    #load the pixels and convert to colored ASCII art

    pixels = frame.load()
    word_art = []
    for y in range(new_height):
        line = ""
        for x in range(new_width):
            brightness = pixels[x, y] / 255
            char = get_char_by_brightness(brightness)
            color = get_color_by_brightness(brightness)
            line += color + char
        word_art.append(line)
    return "\n".join(word_art)

#main function to display video as text art in terminal

def video_to_terminal(video_path, fps=10, new_width=100):

    try:
        clip = VideoFileClip(video_path)
        for frame in clip.iter_frames(fps=fps, dtype="uint8"):
            frame_image = Image.fromarray(frame)
            frame_art = frame_to_word_art(frame_image, new_width=new_width)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(frame_art)
            time.sleep(1 / fps)
    except Exception as e:
        print(f"error processing video: {e}")


#finalize application

video_to_terminal("yourFilePathHere", fps=20, new_width=60)
