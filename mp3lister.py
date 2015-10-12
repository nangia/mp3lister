import os
# requires installation of eyed3
# from http://eyed3.nicfit.net
from eyed3 import load


dir = "songs"

num = 0 
print "Number;Directory;FileName;FullPath;Artist;Album;AlbumArtist;Title;TrackNum"
for root, dirs, files in os.walk(dir):
    for file in files:
	# print file
        split = os.path.splitext(file)
        if len(split) > 1:
            if split[1].upper() == ".MP3":
               num += 1
               fullfilename = root + "/" + file
               #print fullfilename
               mp3obj = load(fullfilename)
               #print mp3obj.tag.track_num
               if mp3obj.tag:
	           print '%d;%s;%s;%s;%s;%s;%s;%s;%s' % (num, root, file, fullfilename, mp3obj.tag.artist, mp3obj.tag.album, mp3obj.tag.album_artist, mp3obj.tag.title, mp3obj.tag.track_num)
               else:
	           print '%d;%s;%s;%s;%s;%s;%s;%s;%s' % (num, root, file, fullfilename, "None", "None", "None", "None", "None")

