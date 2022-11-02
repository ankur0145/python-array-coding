size=int(input("Enter the number of elements you want in array: "))
arr=[]
for i in range(0,size):
    elem=int(input("Please give value for index "+str(i)+": "))
    arr.append(elem)
num=int(input("Enter a number to remove from array : "))

arr.remove(num)
print("Array after removing",num,"=",arr)
