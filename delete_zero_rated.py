#!/usr/bin/python
#log# Automatic Logger file. *** THIS MUST BE THE FIRST LINE ***
#log# DO NOT CHANGE THIS LINE OR THE TWO BELOW
#log# opts = Struct({'__allownew': True, 'logfile': 'find_ratings.py'})
#log# args = []
#log# It is safe to make manual edits below here.
#log#-----------------------------------------------------------------------
import gpod
import os
DATABASE = "/media/FRACPOD/"
db = gpod.Database(DATABASE)
removable = []
for track in db:
    if track['rating'] == 0 :
        removable.append(track)
        print(track, track['rating'], track['app_rating'])

allfiles = [file.ipod_filename() for file in db]
allfiles.sort()
print len(allfiles)
print 
print

rm_files = []
for root, dirs, files in os.walk("%siPod_Control/Music/"% DATABASE):
    for name in files:
        if name.lower().endswith("mp3"):
            filename = "%s/%s"% (root, name)
            if not filename in allfiles:
                rm_files.append(filename)

rm_files.sort()
print len(rm_files)



