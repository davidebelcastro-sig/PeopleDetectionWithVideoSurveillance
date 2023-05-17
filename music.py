from pydub import AudioSegment
from pydub.playback import play


def sound():
    song = AudioSegment.from_mp3("./sound/allarme.mp3")  #attiva allarme
    signal=0

    while(signal == 0):
        play(song)
        fp=open("result.txt","r",encoding="utf-8")
        for riga in fp:
            if riga=="1":
                signal=1
            break
        fp.close()
    fp=open("result.txt","w",encoding="utf-8")
    fp.close()