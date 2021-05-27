from pygame import mixer
mixer.init()
l = ['Nadiyonpaar.mp3','chandh.mp3']
m = int(input("Choose song\n1.Nadiyoonpaar\n2.Chandh"))
s = l[m-1]

mixer.music.load(s)
mixer.music.set_volume(0.7)
mixer.music.play()
while True:

	print("Press 'p' to pause, 'r' to resume")
	print("Press 'e' to exit the program")
	inst = input(" ")

	if inst == 'p':

		# Pausing the music
		mixer.music.pause()
	elif inst == 'r':

		# Resuming the music
		mixer.music.unpause()
	elif inst == 'e':

		# Stop the mixer
		mixer.music.stop()
		break
