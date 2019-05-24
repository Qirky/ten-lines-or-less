Scale.default="minor"; Clock.bpm=144

p1 >> keys(var((P(0,1,2,3,4) * P[3,2,5,7]) % 15), dur=PDur(3,8), amp=1/2, rate=linvar([0,12],16)).spread()

p2 >> saw(var([0,-1]), amp=[0,1], vib=12, oct=6, drive=0.5, lpf=linvar([2000,6000],32), lpr=0.3) + var([0,-2,[0,-2]],[24,4,4])

b1 >> sawbass(var([3,2]), dur=PDur(3,8)*2, sus=1/2, cutoff=var([750,2000],32), delay=(0,0.5), oct=(5,[4,6]), amp=var([1,0],[15,1]))

d1 >> play("[--]~", sample=var([0,2],32))
d2 >> play("<X >< (nb)H(l[hI])>", sample=2)
