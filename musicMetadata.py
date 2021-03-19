#!/usr/bin/env python3
#from google_images_search import GoogleImagesSearch
from tinytag import TinyTag

import unicodedata
import os
import sys
import bing_scraper

def files():
	musicLocation = "D:\\Music\\Audio\\Test\\"

	fileNames = os.listdir(musicLocation)
	for x in range(len(fileNames)):
		print("File Name: {0} {1}".format(x, fileNames[x]))
#formats the name to the song title, essentially removes unwanted numbers spaces etc from song name
def rename(fullMusicPath,tag,musicLocation):
	base = os.path.basename(fullMusicPath)
	#gets the extentions of the file
	baseExt = os.path.splitext(base)[1]
	newFullMusicPath = musicLocation + tag.title + baseExt
	#renames the file with the new name(song title)
	
	try:
	    os.rename(fullMusicPath, newFullMusicPath)
	except WindowsError:
	    os.remove(newFullMusicPath)
	    os.rename(fullMusicPath, newFullMusicPath)
	#returns the title with extension to update list that got read
	return (tag.title + baseExt)
def main():

	musicLocation = "D:\\Music\\Audio\\converted\\"

	fileNames = os.listdir(musicLocation)


	previousAlbum = []
	for x in range(len(fileNames)):
		fullMusicPath =  musicLocation + fileNames[x]
		
		print("File Name: {}".format(fileNames[x]))
		print("NUMBER OF ITEMS IN LIST: {}".format(len(previousAlbum)))
		tag = TinyTag.get(fullMusicPath)
		fileNames[x] = rename(fullMusicPath,tag,musicLocation)
		#if album name not in the list attempts to get album cover of bing if song 
		#has an album name in the metadata
		if(tag.album in previousAlbum):
			print("skipping since i got art already")
		else:
			previousAlbum.append(tag.album)
			print('This track is by %s. ' % tag.artist)
			print('The Album Name is %s' % tag.album)
			image = TinyTag.get(musicLocation + fileNames[x], image=True)
			#added

			#gis = GoogleImagesSearch('AIzaSyAW1g6q5y42WqDag66TykYQDcpqw71Zaz4', '010425534872078538393:ww7sjftw6my')
		    # define search params:
			image_data = image.get_image()
			if( tag.album != None and tag.artist != None):
				#print("has album name and artist")
				if image_data == None:
					'''with open("albumart.jpg", "wb") as f:
					f.write(image_data)
					'''
					parse = str(tag.artist) + " " + str(tag.album) + " album art"
					_search_params = {
						'q': str(tag.artist) + " " + str(tag.album),
						'num': 25,
						'safe': 'off',
						'fileType': 'jpg'
						
					}
					executeScraper = "python bing_scraper.py --search \"" + parse + "\" --download --limit 3 --chromedriver D:\\grrr1\\Dowloads\\chromedriver_win32\\chromedriver"
					print (executeScraper)
					os.system(executeScraper)
					


		
			
		

if __name__ == "__main__":
	#files()
	main()