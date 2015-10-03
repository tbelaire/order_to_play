import subprocess
from subprocess import call

folder = "clips/rock"

p = subprocess.Popen(['ls', folder], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for (song, target) in zip(p.stdout.readlines(), ['audioA.mp3', 'audioB.mp3', 'audioC.mp3', 'audioD.mp3', 'audioE.mp3']):
    song_path =  folder + "/" + song.strip()
    print("ln -s " + "'" + song_path + "'" + " " + target)
    subprocess.call(['ln', '-s', song_path, target])


