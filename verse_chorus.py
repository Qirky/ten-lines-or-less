def bass1():
    p1 >> pluck([0, 2, 3, 5, 7], dur=[1/2, 1/4, 1/2, 1/8, 1/8], oct=4, spin=2).every(3, "shuffle")
    Clock.future(16, bass2)
def bass2():
    p1 >> pluck([0, 5, 3, 2], dur=[1/2, 1/2, 1/2, 1/2, 1/2], oct=4, spin=3).every(4, "reverse")
    Clock.future(16, bass1)
def drums():
    d1 >> play("x(-o=x) x j x x(o[-d]){a=c} ", echo=0.25, mix=0.3).shuffle()
bass1()    
drums()
