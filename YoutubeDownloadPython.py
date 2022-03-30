from pytube import YouTube
from colorama import init, Fore

def on_complete(stream, filepath):
	print("Téléchargement terminé")
	print(filepath)

def on_progress(stream, chunk, bytes_remaining):
	progress_string = f"{round(100 - (bytes_remaining / stream.filesize * 100),2)}%"
	print(progress_string)
init()
link = input("Lien Youtube : ")
video_object = YouTube(link, on_complete_callback = on_complete, on_progress_callback = on_progress)


# Informations
print(Fore.RED + f"title:  \033[39m {video_object.title}")
print(Fore.RED + f"length: \033[39m {round(video_object.length / 60,2)} minutes")
print(Fore.RED + f"views:  \033[39m {video_object.views / 1000000} million")
print(Fore.RED + f"author: \033[39m {video_object.author}")

# Téléchargement
print(
	Fore.RED + "Télécharger :" + 
	Fore.GREEN + "(m)eilleur qualité \033[39m |" +
	Fore.YELLOW + "(b)asse qualité \033[39m + |" +
	Fore.BLUE + "(a)udio seulement \033[39m +| (s)ortir")
download_choice = input("Choix : ")

match download_choice:
	case "m":
		video_object.streams.get_highest_resolution().download(r"C:\Users\amerc\Downloads")
	case "b":
		video_object.streams.get_lowest_resolution().download(r"C:\Users\amerc\Downloads")
	case "a":
		video_object.streams.get_audio_only().download(r"C:\Users\amerc\Downloads")