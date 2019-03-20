b1 >> fuzz([0, 2, 3, 5, 7, 9], dur=1/2)
k1 >> play("x ").every(4, "amen")
h1 >> play("- - -- -- [--]  ", amp=1.4)
Clock.every(8, lambda: b1.shuffle())
