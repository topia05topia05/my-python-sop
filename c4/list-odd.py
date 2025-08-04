#(1)二倍して１引く方法
date = [i * 2 - 1 for i in range(1, 6)]
print(date)

#(2)range()を工夫する方法
date = [ i for i in range(1, 6, 2)]
print(date)

#(3)内包表記でfrとifを組み合わせる方法
date = [i for i in range(1, 6) if i % 2 == 1]
print(date)