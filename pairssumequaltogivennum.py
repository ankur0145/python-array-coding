def find(array,len,sum):
    print("pairs whose sum is:",sum)
    for i in range(len):
        for j in range(i,len):
            if array[i]+array[j]==sum:
                print(array[i],array[j])
array=[5,2,3,4,1,6,7]
sum=7
print("array=",array)
find(array,len(array),sum)
