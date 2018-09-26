Clock.bpm=144; Scale.default="lydianMinor"
d1 >> play("x-o{-[-(-o)]}", sample=0).every([28,4], "trim", 3)
d2 >> play("(X )( X)N{ xv[nX]}", drive=0.2, lpf=var([0,40],[28,4]), rate=PStep(P[5:8],[-1,-2],1)).sometimes("sample.offadd", 1, 0.75)
d3 >> play("e", amp=var([0,1],[PRand(8,16)/2,1.5]), dur=PRand([1/2,1/4]), pan=var([-1,1],2))
c1 >> play("#", dur=32, room=1, amp=2).spread()
var.switch = var([0,1],[32])
p1 >> karp(dur=1/4, rate=PWhite(40), pan=PWhite(-1,1), amplify=var.switch, amp=1, room=0.5)
p2 >> sawbass(var([0,1,5,var([4,6],[14,2])],1), dur=PDur(3,8), cutoff=4000, sus=1/2, amplify=var.switch)
p3 >> glass(oct=6, rate=linvar([-2,2],16), shape=0.5, amp=1.5, amplify=var([0,var.switch],64), room=0.5)
