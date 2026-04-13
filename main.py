# #C=2pir,s=pir^2
# pi = 3.1415926
# r = float(input("请输入圆的半径："))
# c = 2*pi*r
# s = pi*r**2
# print(f"圆的周长是{c},圆的面积是{s}")
pi=3.1415
r=3
c=2*pi*r
s=pi*r**2
print(f"半径为{r}的图形，其周长等于{c}；面积等于{s}；")
s=15.7
r=c/(2*pi)
s=pi*r**2
print(f"周长为{c}的图形,其半径为{r};面积等于{s};")
s=5
r=round((s/pi)**0.5,3)
C=round(2*pi*r,4)
print(f"面积为{s}的图形,其半径为{r};周长等于{c};")