def statis(x):
    totalsum=0
    for x in data:
        totalsum=totalsum+x
        
    library_size=len(data)
    
    average=totalsum/library_size
    
    return totalsum,average

data = [1,5,6,3,1,2,3]

totalsum,average=statis(data)

print(totalsum)
print(average)