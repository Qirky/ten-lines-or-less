Clock.bpm=110; Scale.default="major"
p1 >> pluck((2,[4,4,4,4,5],6,[8,8,9]), dur=1/4, sus=1/2, vib=0, pan=PWhite(-1,1), vibdepth=0.02, coarse=0, oct=[4,5], fmod=PWhite(-4,4), lpf=PWhite(2000,4000), lpr=PWhite(0.2,0.4))

d1 >> play(P["x-(iS)"][:8].rotate(var([1,3])), rate=1.5, dur=1/4, delay=var([0,(0,0.75)],PRand(8)))
d2 >> play("<x=><  |@3| >", sample=2)
d3 >> play("n", dur=1/4, amp=PWhite(0.5,1), rate=PWhite(.98,1.02), pan=0.5, sample=6)

b1 >> sawbass(var([0,1,-2],[8,8,16]), dur=PDur(5,16), cutoff=P[1000,5000][:5], sus=1/2)

p2 >> blip([0,2,3,P*(4,5)], dur=2*P[4,2,1,1], sus=8, rate=linvar([0,8],100), amp=2, room=1, pan=-0.5).penta() + var([2,3],16)    
