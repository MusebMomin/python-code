
y1=[3,0,3,2,3,2,3,3,2,3,2,3]
y2=[3,1,3,2,3,2,3,3,2,3,2,3]
y =[0,0,0,0,0,0,0,0,0,0,0,0]
arr=[]

def is_leap_year(year):
    if(year%4 == 0):
        return 1
    else:
        return 0

sum_odd = 0
fri = 0
for year in range(1,100):
    if(is_leap_year(year) == 0):
        y = y1
    else:
        y = y2
    for month in range(0,12):
        if(13 + sum_odd)%7 == 5:
            fri = fri+1
        sum_odd = sum_odd + y[month]
print(fri)