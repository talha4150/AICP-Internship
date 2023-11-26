#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Talha Ahmad AICP Week-04
#CNIC: 37406-2961444-3

HexLength = 3
#Note: Last Digit of CNIC = 3

def calcArea():
  area = 1.5*1.732* HexLength**2
  print('Area of Hexagon is: ',area)

def calcAngleSum():
  angle = 120
  sum = (6-2) * angle
  print('Sum of angles og Hexagon is: ',sum)

def calcPeri():
  perimeter = 6 *HexLength
  print('Perimeter of Hexagon is: ',perimeter)

def display1():
  calcArea()
  calcPeri()
  calcAngleSum()


     

SquareLength = 4
#Note: Square Length = Last Digit of CNIC + 1 = 3+1= 4

def calAreaSquare():
  area = squareLength**2
  print('Area of Square is: ',area)

def calcPeriSquare():
  perimeter = SquareLength*4
  print('Perimeter of Square is: ',perimeter)

def display2():
  calAreaSquare()
  calcPeriSquare()
     

while True:
  choice = input('Please Enter your choice: ')
  print()
  if choice == '1':
    display1()
  elif choice=='2':
    display2()
  else:
    break
    


# In[ ]:




