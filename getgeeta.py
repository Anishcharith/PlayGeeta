import urllib.request
import os
from os.path import expanduser
home = expanduser("~")

verses=[46,72,43,42,29,47,30,28,34,42,55,20,35,27,20,24,28,78]
exception=[]
os.chdir(home)
if os.path.exists('.Bhagavadgeeta/'):
    print("countinueing the download")
    for i in range(18):
        for j in range(1,verses[i]+1):
            if os.path.exists('.Bhagavadgeeta/'+str(i+1).zfill(2)+'-'+str(j).zfill(2)+'.mp3'):
                continue
            else:
                try:
                    urllib.request.urlretrieve('http://www.bhagavad-gita.org/AudioArchive/Gita/English/verses/'+str(i+1).zfill(2)+'-'+str(j).zfill(2)+'.mp3',filename='.Bhagavadgeeta/'+str(i+1).zfill(2)+'-'+str(j).zfill(2)+'.mp3')
                except:
                    exception.append(str(i)+str(j))
else:
    os.mkdir('.Bhagavadgeeta/')
    for i in range(18):
        for j in range(1,verses[i]+1):
            try:
                urllib.request.urlretrieve('http://www.bhagavad-gita.org/AudioArchive/Gita/English/verses/'+str(i+1).zfill(2)+'-'+str(j).zfill(2)+'.mp3',filename='.Bhagavadgeeta/'+str(i+1).zfill(2)+'-'+str(j).zfill(2)+'.mp3')
            except:
                exception.append(str(i)+str(j))

print('Finished the download')
