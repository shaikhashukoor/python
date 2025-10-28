#!/usr/bin/env python
# coding: utf-8

# In[4]:


import secondd
while(1):
    print("1.circle \n 2.rectangle \n 3.exit")
    h=int(input("enter your choice"))
if h==1:   
    r=int(input("enter the radius of the circle"))
    print("area=",second.circlea(r))
    print("perimeter=",second.circlep(r))
elif h==2:   
    b=int(input("enter the breadth of the circle"))
    l=int(input("enter the length of the circle"))      
    print("area=",second.rectanglea(b,l))
    print("perimeter=",second.rectanglep(b,l))          
else:
          print("exiting")

      


# In[ ]:




