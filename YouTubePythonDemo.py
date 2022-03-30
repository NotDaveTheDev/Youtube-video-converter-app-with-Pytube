from pytube import YouTube

def on_complete(stream, file_path):
	print(stream)
	print(file_path)

def on_progress(stream, chunk, bytes_remaining):
	print( 100 - (bytes_remaining / stream.filesize * 100))

video_object = YouTube(
	"https://www.youtube.com/watch?v=NtzDjNhPZgU", 
	on_complete_callback = on_complete,
	on_progress_callback = on_progress)

# Video information
print(video_object.title)
print( f'{video_object.length / 60} minutes')
print(video_object.views)
print(video_object.author)
# print(video_object.description)

# Video streams (indique les différents flux de vidéo ; nous permet de choisir la qualité, la résolution, le son, etc. Décommenter pour renvoyer ces informations)
#for streams in video_object.streams:
	#print (streams)
	#printer les attributs de l'URL entrée plus haut nous permet de connaître ces attributs.
print (video_object.streams.get_highest_resolution()) 
print (video_object.streams.get_lowest_resolution())
print (video_object.streams.get_audio_only())

# Download
video_object.streams.get_highest_resolution().download() #Télécharge la vidéo à la meilleure qualité.