import os
import pylyrics3 as pl

directory = "./lyrics/"
if not os.path.exists(directory):
    os.makedirs(directory)

search = pl.get_artist_lyrics("The wonder years")
	
for i in search.keys():
	songname = i
	lyrics = search[i]
	file = open(directory+songname+".txt", "w")
	file.write(i + "\n\n")
	file.write("-------------------------------\n\n")
	file.write(lyrics)
	file.close()

