from pytube import YouTube # Importation du module YouTube à partir de pytube (on n'a pas besoin de tous les modules)
from colorama import init, Fore # Importation des modules init et Fore à partir de colorama (on n'a pas besoin de tous les modules)

def on_complete(stream, filepath): # Première fonction qui nous permet de préciser à l'utilisateur que son téléchargement est terminé
	print("Téléchargement terminé")
	print(filepath)

def on_progress(stream, chunk, bytes_remaining): # Deuxième fontion qui permet à l'utilisateur de savoir où en est son téléchargement
	progress_string = f"{round(100 - (bytes_remaining / stream.filesize * 100),2)}%"
	print(progress_string)

init() # Active les modules init et Fore de colorama

link = input("Lien Youtube : ") #Invite l'utilisateur à entrer l'URL de la vidéo à convertir
video_object = YouTube(link, on_complete_callback = on_complete, on_progress_callback = on_progress)


# Informations
print(Fore.RED + f"title:  \033[39m {video_object.title}")
print(Fore.RED + f"length: \033[39m {round(video_object.length / 60,2)} minutes")
print(Fore.RED + f"views:  \033[39m {video_object.views / 1000000} million")
print(Fore.RED + f"author: \033[39m {video_object.author}")

# Téléchargement

video_object.streams.get_audio_only().download(r"C:\Downloads") #Ne télécharge que l'audio du fichier dans l'emplacement spécifié en paramètre de .download