p1 >> keys(([3,4,5,4],7,[9,9,9,10]), dur=4, spin=8, tremolo=4, room=1, amp=2)

p2 >> sawbass(var([1,0,-2,-4],4), dur=1/2, amp=[1,1,0,1]).sometimes("amp.trim", 3)

p3 >> star(p2.pitch + (P[1,0,1,0,1,0,0,2,1,0]), dur=PDur([5,1,2,2],8)*2, sus=2, oct=6)

d1 >> play("<Vs><[--]><.{.+[ +]}O( [( u)O])>", lpf=var([0,1000],[28,4]))

# Add for some variety
p3.sometimes("offadd", 4) + var([0,2],[PRand([0,2,4])])
