from tokenize import endpats

for i in range(1,10):#外层循环，控制行
     for j in range(1,i+1):#内层循环,控制列
         print(f"{j} x {i} ={j * i}",end="\t")
     print("")