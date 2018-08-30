Clock.bpm=100; Scale.default="minor"
p1 >> pulse([0,-1,-2,-3], dur=8, lpf=600, lpr=0.2, crush=8) + (0,2,4,const(6))
p3 >> blip(p1.pitch, dur=8, sus=4, room=1, oct=6) + [0,0,0,P*(2,4,3,-1)]
p2 >> saw(P[:5][:9][:16], dur=1/4, oct=var([3,4],[12,4])).penta()
d1 >> play("(x )( x)o{ vx[xx]}", crush=16, rate=.8).every([24,5,3], "stutter", 4, dur=3)
d2 >> play("<-s>< ~*~>").every(30.5, "jump", cycle=32)
