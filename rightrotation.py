size=int(input("Enter the number of elements you want in array: "))
arr=[]
for i in range(0,size):
    elem=int(input("Please give value for index "+str(i)+": "))
    arr.append(elem)
for i in range(0,2):

    temp=arr[size-1];
    for j in range(size-1,-1,-1):
        arr[j]=arr[j-1]

    arr[0]=temp;
print("Array after performing right rotation :")
print(arr)
