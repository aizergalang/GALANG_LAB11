list=[]
for i in range (1,11):
    words=(input(f'enter word:{i}'))
    list.append(words)
num= int(input('enter a lenght/number:'))
for x in list:
    if len(x) >= num:
        print(x)
        
    

    
    


    
    