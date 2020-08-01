#check whether the input follows the wave pattern i.e a1>a2<a3>a4<a5....where a1,a2,a3.... are elements of an array .

def ArrayChallenge(arr):
  arr.sort()
  l=len(arr)
  arr2=[]
  arr1=[]
  for i in range(l//2):
    arr2.append(arr[i])
  j=0
  for i in range(l//2,l):
    arr1.append(arr[i])
  flag=0
  for i in range(len(arr1)-1):
    if(arr1[i]>arr2[i] and arr1[i+1]>arr2[i]):
      flag=0
    else:
      flag=1
      break
  if(flag==0 and l%2==0):
    if(arr1[l//2-1]<=arr2[l//2-1]):
      flag=1
  if(flag==0):
    print("true")
  else:
    print("false")

  

    
  # code goes here
  return arr

# keep this function call here 
ArrayChallenge(input())
