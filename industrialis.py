Clock.bpm=144; Root.default =- 1; Scale.default="minor"
b1 >> bass(dur=1/4, formant=PRand(8)[:8], rate=PRand(5,10)[:8], pan=PWhite(-1,1))

cp >> play("* ")
d1 >> play(P["V::"][:16] & P["<v ><  |o1| >"], drive=0.1, rate=1.2)

b2 >> sawbass(var([0,5,2,[3,6]],[8,6,1,1]), dur=PDur(3,8)).spread()
