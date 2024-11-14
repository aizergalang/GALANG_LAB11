
num_list=[]
while True:
    grades=(input('input grade'))
    if grades==str("done"):
        break
    else:grades=int(grades)
    num_list.append(int(grades))
    
    if grades<40 or grades>100:
        print('grade should be 40 to 100')
        break
    else:
        avg = sum(grades)/len(grades)
        pass=
    
        print()
