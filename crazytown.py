Scale.default = Scale.minor
p1 >> pluck([0,0, 3, 3, 4, -2,4, -2],dur=[1/2,1,1/2, 1, 1/2, 1, 1/2, 1/4, 1/4],oct=3, amp=1.3,lpf=linvar([400,4000],16)).every(4, "trim", 3)
d1 >> play("x-o-x-o-x-o-x-oo(oo)",room=0.8, mix=0.4,amp=[0.7, 0.6, 0.7, 0.8]).every(5, "trim", 2)
p2 >> pads([0,2,4,6], dur=4, spin=4, oct=4,amp=2.0, chop=[8,16], hpf=linvar([500,2000],16), hpr=0.2).every(8, "shuffle")
p3 >> karp([0,2,4,6,9], dur=[1,2,1.5], amp=0.5,echo=0.75, decay=0.5, sustain=0.1).every(8, "shuffle")




