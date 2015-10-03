import subprocess
from subprocess import call
import sys

assert (len(sys.argv) == 2)
#folder = "clips/rock"
folder = sys.argv[1]

audio_links = ['audioA.mp3', 'audioB.mp3', 'audioC.mp3', 'audioD.mp3', 'audioE.mp3']
call(["rm"] + audio_links)
p = subprocess.Popen(['ls', folder], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for (song, target) in zip(p.stdout.readlines(), audio_links):
    song_path =  folder + "/" + song.strip()
    subprocess.call(['ln', '-s', song_path, target])


