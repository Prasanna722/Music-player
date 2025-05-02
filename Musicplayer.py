import os
import tkinter as tk
from tkinter import filedialog
from pygame import mixer

mixer.init()

current_index = 0
song_list = []

root = tk.Tk()
root.title("Music Player 🎶")
root.geometry("400x450")
root.config(bg="#1e1e1e")

def load_songs():
    global song_list, current_index
    folder = filedialog.askdirectory()
    if folder:
        os.chdir(folder)
        files = [file for file in os.listdir(folder) if file.endswith(".mp3")]
        song_list = files
        song_listbox.delete(0, tk.END)
        for song in song_list:
            song_listbox.insert(tk.END, song)
        current_index = 0
        song_listbox.select_set(current_index)

def play_song():
    global current_index
    if song_list:
        song = song_list[current_index]
        mixer.music.load(song)
        mixer.music.play()
        status_label.config(text=f"Now Playing: {song}")
        song_listbox.select_clear(0, tk.END)
        song_listbox.select_set(current_index)

def stop_song():
    mixer.music.stop()
    status_label.config(text="Music Stopped")

def pause_song():
    mixer.music.pause()
    status_label.config(text="Music Paused")

def resume_song():
    mixer.music.unpause()
    status_label.config(text="Music Resumed")

def next_song():
    global current_index
    if song_list:
        current_index = (current_index + 1) % len(song_list)
        play_song()

def prev_song():
    global current_index
    if song_list:
        current_index = (current_index - 1) % len(song_list)
        play_song()

# UI Elements
status_label = tk.Label(root, text="Load and Play a Song 🎶", fg="white", bg="#1e1e1e")
status_label.pack(pady=10)

song_listbox = tk.Listbox(root, width=50, height=10, bg="black", fg="lime")
song_listbox.pack(pady=10)

btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack(pady=10)

play_btn = tk.Button(btn_frame, text="▶ Play", width=10, command=play_song)
play_btn.grid(row=0, column=0, padx=5)

pause_btn = tk.Button(btn_frame, text="⏸ Pause", width=10, command=pause_song)
pause_btn.grid(row=0, column=1, padx=5)

resume_btn = tk.Button(btn_frame, text="⏵ Resume", width=10, command=resume_song)
resume_btn.grid(row=1, column=0, padx=5, pady=5)

stop_btn = tk.Button(btn_frame, text="⏹ Stop", width=10, command=stop_song)
stop_btn.grid(row=1, column=1, padx=5, pady=5)

nav_frame = tk.Frame(root, bg="#1e1e1e")
nav_frame.pack(pady=5)

prev_btn = tk.Button(nav_frame, text="⏮ Previous", width=12, command=prev_song)
prev_btn.grid(row=0, column=0, padx=10)

next_btn = tk.Button(nav_frame, text="Next ⏭", width=12, command=next_song)
next_btn.grid(row=0, column=1, padx=10)

load_btn = tk.Button(root, text="📁 Load Songs Folder", command=load_songs, bg="darkorange", fg="white")
load_btn.pack(pady=10)

root.mainloop()
