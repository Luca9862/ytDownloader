from pytube import YouTube  
import tkinter as tk

def downloadVideo(link_video, path):
    link_video.download(path)

root = tk.Tk()
root.title("Youtube Downloader by @lucacanali")

link_label = tk.Label(root, text="Link", font=("Arial", 20)).grid(row=0, column=0)
link_input = tk.Entry(root, width=50)
link_input.grid(row=0, column=1)
parh_label = tk.Label(root, text="Path", font=("Arial", 20)).grid(row=1, column=0)
path_input = tk.Entry(root, width=50)
path_input.grid(row=1, column=1)
button = tk.Button(root, text="Download", font=("Arial", 20), command=lambda: downloadVideo(YouTube(link_input.get()), path_input.get())).grid(row=2, column=0, columnspan=2)
root.mainloop()