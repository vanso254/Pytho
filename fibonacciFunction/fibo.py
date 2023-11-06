# def fibonacci(nterms): 
#     data=[]    
#     n1,n2=0,1
#     count=0
#     if nterms <=0:
#         print("Please enter a positive number")
#     elif nterms==1:
#         print(n1)
#     else:
#         for nterms in range(2,nterms):            
#             while count<nterms:
#                 z=data.append(n1)          
#                 nth=n1+n2
#                 n1=n2
#                 n2=nth
#                 count+=1
                
#     return z

def fibonacci(nterms):
    data = []
    n1, n2 = 0, 1

    if nterms <= 0:
        print("Please enter a positive number")
    elif nterms == 1:
        data.append(n1)
    else:
        data.append(n1)
        data.append(n2)
        for _ in range(2, nterms):
            nth = n1 + n2
            data.append(nth)
            n1, n2 = n2, nth

    return data


