from tkinter import *
import random
root = Tk()
root.geometry('400x240')
root.title('Love Calculator (FLAME game)')
def calculate_love():
    first_name=name1.get()
    Second_name=name2.get()
    names=first_name+"loves"+Second_name
    l=list(names)
    counts = {}
    for element in l:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1
    l2=list(counts.values())
    while len(l2)>2:
        x=0
        temp=[]
        l3=[]
        l4=[]
        if len(l2)%2==0:
            l3=l2[0:len(l2)//2]
            l4=l2[(len(l2)//2) : len(l2)]
            if len(l3)==len(l4):
                for i in range(len(l3)):
                    temp.append(l3[i]+l4[i])
            l2=temp
        else:
            x=l2[(len(l2)//2)]
            l2.remove(l2[(len(l2)//2)])
            l3=l2[0:(len(l2)//2)]
            l4=l2[(len(l2)//2) : len(l2)]
            if len(l3)==len(l4):
                for i in range(len(l3)):
                    temp.append(l3[i]+l4[i])
            temp.append(x)
            l2=temp
    k=str(l2[0]) + str(l2[1])
    k2=int(k)
    while 100 < k2 < 999:
        hundreds_digit = k2 // 100
        tens_digit = (k2 // 10) % 10
        units_digit = k2 % 10
        new_tens_digit = (hundreds_digit + units_digit)
        k2 = new_tens_digit * 10 + tens_digit
    result.config(text=k2)
        
heading = Label(root, text='Know the % she/he loves you', bg="light blue")
heading.pack()
slot1 = Label(root, text="Enter Your Name:")
slot1.pack()
name1 = Entry(root, border=5)
name1.pack()
slot2 = Label(root, text="Enter Your Partner Name:")
slot2.pack()
name2 = Entry(root, border=5)
name2.pack()
bt = Button(root, text="Calculate", height=1,
			width=7, command=calculate_love)
bt.pack()
result = Label(root, text='Love Percentage between both of You:', bg="light green")
result.pack()
root.mainloop()