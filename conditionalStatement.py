#trafic light
light = input("light:")
if(light == 'red'):
    print('stop')
elif(light == 'yellow'):
    print('look')
elif(light == 'green'):
    print('go')
else:
    print('light is broken')
#grade of student
marks = input('marks :')
if(marks>=90):
    print('A')
elif(marks >= 80 and marks <90):
    print('b')        
elif(marks>=70 and marks < 80):
    print("c") 
else:
    print("no fee")       
