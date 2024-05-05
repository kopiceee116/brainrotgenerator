import cleanup
import smallvideos, finalvideo
import hangcsinalo
import szetszedes, karcolas

url = input("reddit link ")

hangcsinalo.hangkeszites(szetszedes.szetszedes(karcolas.szeddkiaszoveget(url)))
smallvideos.makeVids('BgVid2.mp4','split.txt','hang')
finalvideo.concatenate_videos(finalvideo.getVideoFiles("Videos"), 'output.mp4')

cleanup.RemoveFolder('hang')
cleanup.RemoveFolder('Videos')
cleanup.RemoveFile('saved.txt')
cleanup.RemoveFile("split.txt")