Clock.bpm=var([120,60,30,15,2],[124,2,1,1/2,1/2]) # wait for the drop!
Scale.default="major"
d1 >> play("<|V0|:><  O ><|[--]5|>", sample=2)
d2 >> play("<...(+|L2|)>< m>")
c1 >> play("n", dur=1/4, sample=PRand(8), pan=PWhite(-1,1))
b1 >> dbass(var([0,-2],8), dur=PDur(3,9), shape=PWhite(0,0.5), sus=2, chop=4, pan=PWhite(-1,1))
p1 >> pads((0,2,4,6), dur=16, amp=1/2, room=1, drive=0, shape=0.2, vib=12, slide=1, slidedelay=0.5, chop=16, delay=0.5)
p2 >> space([[0,2],4], dur=[6,2]).spread()
p3 >> pulse([0,1,0,[1,2],0,4,5,4], lpf=linvar([500,2000],32), lpr=linvar([0.1,1],12), dur=1/2, amp=2*P[1,1,1,1,0,1,1,1]).spread().penta() + var([0,[1,2,3,-1]],[6,2])
cr >> play("#", dur=32, room=1, amp=2).spread()
