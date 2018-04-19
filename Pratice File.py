#import math
#pointOne = input("Please enter the coordinates of the first point (x,y): ")
#pointTwo = input("Please enter the coordinates of the first point (x,y): ")

#x1 = int(pointOne[:pointOne.find(',')])
#y1 = int(pointOne[pointOne.find(',')+1:])
#x2 = int(pointTwo[:pointOne.find(',')])
#y2 = int(pointTwo[pointOne.find(',')+1:])


#distance = math.sqrt((x2 - x1)^2 + (y2 - y1)^2)
#print ("The distance between these two points is", distance, "units.")


#hits = int(input("Please enter the number of hits: "))
#bats = int(input("Please enter the number of bats: "))

#average = round(hits/ bats, 3)
#print ("The batting average of this player is aproximately: %f." %(average))

#times = 1
#def getMarks():
    #global times
    #a = input("Please enter your test mark #%i: " %(times))
    #times = times + 1
    #return a

#def getPercent(x):
    #a = (x/ 60)*100
    #return a
    
#def calAverage(a, b, c, d, e):
    #x = (a + b + c+ d + e)/ 5
    #return x

#mark1 = int(getMarks())
#mark2 = int(getMarks())
#mark3 = int(getMarks())
#mark4 = int(getMarks())
#mark5 = int(getMarks())

#mark1Percent = getPercent(mark1)
#mark2Percent = getPercent(mark2)
#mark3Percent = getPercent(mark3)
#mark4Percent = getPercent(mark4)
#mark5Percent = getPercent(mark5)

#average = calAverage (mark1Percent, mark2Percent, mark3Percent, mark4Percent, mark5Percent)

#print ("%-10s%-10s" %("Mark", "Percent"))
#print ("%-10i%-10.1f" %(mark1, mark1Percent))44
#print ("%-10i%-10.1f" %(mark2, mark2Percent))
#print ("%-10i%-10.1f" %(mark3, mark3Percent))
#print ("%-10i%-10.1f" %(mark4, mark4Percent))
#print ("%-10i%-10.1f" %(mark5, mark5Percent))
#print ("The average for the test is:", str(round(average, 1)) + "%")

#import math

#def getDistance(x1, x2, y1, y2):
    #x = math.sqrt((x2 - x1)**2+(y2 - y1)**2)
    #x = round(x, 3)
    #return x

#def getSlope(x1, x2, y1, y2):
    #x = (y2 - y1)/(x2 - x1)
    #x = round(x, 3)
    #return x

#pointOne = input("Please enter the coordinates of the first point (x,y): ")
#pointTwo = input("Please enter the coordinates of the first point (x,y): ")

#x1 = int(pointOne[:pointOne.find(',')])
#y1 = int(pointOne[pointOne.find(',')+1:])
#x2 = int(pointTwo[:pointTwo.find(',')])
#y2 = int(pointTwo[pointTwo.find(',')+1:])

#slope = getSlope(x1, x2, y1, y2)
#distance = getDistance(x1, x2, y1, y2)

#print ("These two points has a distance of", str(distance), "units, and a slope of", str(slope) + '.')


#def findABCDE(a):
    #x = a.count('A') + a.count('B') + a.count('C') + a.count('D') + a.count('E')
    #return x

#total = findABCDE(input("Please enter a string: "))
#print ("There were", total, "occurrences of A, B, C, D or E")


#def printField(s, i):
    #y = int(((i - len(s))-2) // 2)
    #y2 = (((i - len(s))-2) - y)
    #print ("."*i)
    #print ("." + " "*y + s + " "*y2 + ".")
    #print ("."*i)

#string = input("Please enter your sentence: ")
#field = int(input("Please enter your field size: "))

#printField(string, field)


#def seperateName(a):
    #x = a[a.find(" ") + 1:]
    #y = a[:a.find(" ")]
    #return y, x

#firstName, lastName = seperateName(input("Please enter your full name: "))
#print ("%s, %s" %(lastName, firstName))


#def fileExtension(a):
    #x = a[a.find('.'):]
    #return x
#print ("Your file extension is:","\"", fileExtension(input("Please enter your full file name: ")), "\"")


#string = input("Please input your sentence: ")
#print ("%-20s" %string)
#print ("%20s" %string)

import threading
import pygame           
import sys       

pygame.init()
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SIZE = (1000, 1000)
screen = pygame.display.set_mode(SIZE)
events = pygame.event.get()
x = 150
y = 150
moveX = 0
moveY = 0
moveCount = 0
directionOfOpening = 0
bulletX = 0
bulletY = 0
true = True

def moveBulletPostitions():
    global bulletX, bulletY
    if directionOfOpening == 1:
        while -100 <= bulletX <= 1100 and -100 <= bulletY <= 1100:
            pygame.draw.circle (screen, YELLOW, (bulletX, bulletY), 50, 0)
            bulletX = bulletX - 1
            pygame.time.wait(10)
            pygame.display.flip()
    elif directionOfOpening == 2:
        while -100 <= bulletX <= 1100 and -100 <= bulletY <= 1100:
            pygame.draw.circle (screen, YELLOW, (bulletX, bulletY), 50, 0)
            bulletY = bulletY - 1
            pygame.display.flip()
            pygame.time.wait(10)
    elif directionOfOpening == 3:
        while -100 <= bulletX <= 1100 and -100 <= bulletY <= 1100:
            pygame.draw.circle (screen, YELLOW, (bulletX, bulletY), 50, 0)
            bulletX = bulletX + 1
            pygame.display.flip() 
            pygame.time.wait(10)
    elif directionOfOpening == 4:
        while -100 <= bulletX <= 1100 and -100 <= bulletY <= 1100:
            pygame.draw.circle (screen, YELLOW, (bulletX, bulletY), 50, 0)
            bulletY = bulletY + 1
            pygame.time.wait(10)
            pygame.display.flip() 
            
def shootBullet():
    print ("Here")
    while True:
        for event in pygame.event.get():
            key=pygame.key.get_pressed()    
            if key[pygame.K_SPACE] == True:
                global bulletX, bulletY
                bulletX = y + moveY
                bulletY = x + moveX
                moveBulletPostitions()


def foreGround():
    print("I am gay")
    global true
    global x, y, moveX, moveY, moveCount
    while true == True:
        for event in pygame.event.get():
            key=pygame.key.get_pressed()
            if key[pygame.K_d] == True:
                key=pygame.key.get_pressed()
                d_Pressed = key[pygame.K_d]
                while d_Pressed == True:
                    if (moveCount % 20) == 0:
                        pygame.draw.rect(screen, WHITE, (0, 0, 1000, 1000))
                        pygame.draw.circle (screen, YELLOW, (x+moveX, y+moveY), 125, 0)
                        pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY), 125, 5)
                        pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY-40), 10, 0)
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX+124, y+moveY), 5)
                        pygame.display.flip()
                        moveX = moveX + 5
                        moveCount = moveCount + 1
                        print (moveCount, "here")
                        pygame.time.wait(20)
                        for event in pygame.event.get():
                            if pygame.K_d == True:
                                d_Pressed = True
                            else:
                                d_Pressed = False
                    elif (moveCount % 20) - 19 == 0:
                        pygame.draw.rect(screen, WHITE, (0, 0, 1000, 1000))
                        pygame.draw.circle (screen, YELLOW, (x+moveX, y+moveY), 125, 0)
                        pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY), 125, 5)
                        pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY-40), 10, 0)
                        pygame.draw.polygon (screen, WHITE, ((x+moveX, y+moveY), (x+moveX+150, y+moveY+25), (x+moveX+150, y+moveY-25)))
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX+120, y+moveY+22), 5)
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX+120, y+moveY-22), 5)                
                        pygame.display.flip()
                        moveX = moveX + 5  
                        moveCount = moveCount + 1
                        print (moveCount, "4th")
                        pygame.time.wait(20)
                        for event in pygame.event.get():
                            if pygame.K_d == True:
                                d_Pressed = True
                            else:
                                d_Pressed = False                  
                    elif (moveCount % 20) - 16 == 0:
                        pygame.draw.rect(screen, WHITE, (0, 0, 1000, 1000))
                        pygame.draw.circle (screen, YELLOW, (x+moveX, y+moveY), 125, 0)
                        pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY), 125, 5)
                        pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY-40), 10, 0)
                        pygame.draw.polygon (screen, WHITE, ((x+moveX, y+moveY), (x+moveX+150, y+moveY+100), (x+moveX+150, y+moveY-100)))
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX+100, y+moveY+70), 5)
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX+100, y+moveY-70), 5)                
                        pygame.display.flip()
                        moveX = moveX + 5  
                        moveCount = moveCount + 1
                        print (moveCount, "4th")
                        pygame.time.wait(20)
                        for event in pygame.event.get():
                            if pygame.K_d == True:
                                d_Pressed = True
                            else:
                                d_Pressed = False                              
                    elif (moveCount % 20) - 17 == 0:
                        pygame.draw.rect(screen, WHITE, (0, 0, 1000, 1000))
                        pygame.draw.circle (screen, YELLOW, (x+moveX, y+moveY), 125, 0)
                        pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY), 125, 5)
                        pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY-40), 10, 0)
                        pygame.draw.polygon (screen, WHITE, ((x+moveX, y+moveY), (x+moveX+150, y+moveY+75), (x+moveX+150, y+moveY-75)))
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX+110, y+moveY+55), 5)
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX+110, y+moveY-55), 5) 
                        pygame.display.flip()
                        moveX = moveX + 5
                        moveCount = moveCount + 1
                        print (moveCount, "4th")
                        pygame.time.wait(20)
                        for event in pygame.event.get():
                            if pygame.K_d == True:
                                d_Pressed = True
                            else:
                                d_Pressed = False
                    elif (moveCount % 20) - 18 == 0:
                        pygame.draw.rect(screen, WHITE, (0, 0, 1000, 1000))
                        pygame.draw.circle (screen, YELLOW, (x+moveX, y+moveY), 125, 0)
                        pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY), 125, 5)
                        pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY-40), 10, 0)
                        pygame.draw.polygon (screen, WHITE, ((x+moveX, y+moveY), (x+moveX+150, y+moveY+50), (x+moveX+150, y+moveY-50)))
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX+115, y+moveY+40), 5)
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX+115, y+moveY-40), 5)   
                        pygame.display.flip()
                        moveX = moveX + 5
                        moveCount = moveCount + 1
                        print (moveCount, "4th")
                        pygame.time.wait(20)
                        for event in pygame.event.get():
                            if pygame.K_d == True:
                                d_Pressed = True
                            else:
                                d_Pressed = False                            
                    else:
                        pygame.draw.rect(screen, WHITE, (0, 0, 1000, 1000))
                        pygame.draw.circle (screen, YELLOW, (x+moveX, y+moveY), 125, 0)
                        pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY), 125, 5)
                        pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY-40), 10, 0)
                        pygame.draw.polygon (screen, WHITE, ((x+moveX, y+moveY), (x+moveX+150, y+moveY+125), (x+moveX+150, y+moveY-125)))
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX+92, y+moveY+80), 5)
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX+92, y+moveY-80), 5)                
                        pygame.display.flip()
                        moveX = moveX + 5
                        moveCount = moveCount + 1
                        print (moveCount)
                        pygame.time.wait(10)
                        for event in pygame.event.get():
                            if pygame.K_d == True:
                                d_Pressed = True
                            else:
                                d_Pressed = False  
    
                pygame.draw.rect(screen, WHITE, (0, 0, 1000, 1000))
                pygame.draw.circle (screen, YELLOW, (x+moveX, y+moveY), 125, 0)
                pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY), 125, 5)
                pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY-40), 10, 0)
                pygame.draw.polygon (screen, WHITE, ((x+moveX, y+moveY), (x+moveX+150, y+moveY+125), (x+moveX+150, y+moveY-125)))
                pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX+92, y+moveY+80), 5)
                pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX+92, y+moveY-80), 5)                
                pygame.display.flip()
                moveX = moveX + 5
                directionOfOpening = 3
                moveCount = moveCount + 1
                print (moveCount)
                pygame.time.wait(10)
            elif key[pygame.K_a] == True:
                key=pygame.key.get_pressed()
                a_Pressed = key[pygame.K_a]
                while a_Pressed == True:
                    if (moveCount % 20) == 0: #or (moveCount %20) - 19 == 0 or (moveCount %20) - 18 == 0
                        pygame.draw.rect(screen, WHITE, (0, 0, 1000, 1000))
                        pygame.draw.circle (screen, YELLOW, (x+moveX, y+moveY), 125, 0)
                        pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY), 125, 5)
                        pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY-40), 10, 0)
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX-124, y+moveY), 5)
                        pygame.display.flip()
                        moveX = moveX - 5
                        moveCount = moveCount + 1
                        print (moveCount, "here")
                        pygame.time.wait(20)
                        for event in pygame.event.get():
                            if pygame.K_a == True:
                                a_Pressed = True
                            else:
                                a_Pressed = False
                    elif (moveCount % 20) - 19 == 0:
                        pygame.draw.rect(screen, WHITE, (0, 0, 1000, 1000))
                        pygame.draw.circle (screen, YELLOW, (x+moveX, y+moveY), 125, 0)
                        pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY), 125, 5)
                        pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY-40), 10, 0)
                        pygame.draw.polygon (screen, WHITE, ((x+moveX, y+moveY), (x+moveX-150, y+moveY+25), (x+moveX-150, y+moveY-25)))
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX-120, y+moveY+22), 5)
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX-120, y+moveY-22), 5)                
                        pygame.display.flip()
                        moveX = moveX - 5  
                        moveCount = moveCount + 1
                        print (moveCount, "4th")
                        pygame.time.wait(20)
                        for event in pygame.event.get():
                            if pygame.K_a == True:
                                a_Pressed = True
                            else:
                                a_Pressed = False                  
                    elif (moveCount % 20) - 16 == 0:
                        pygame.draw.rect(screen, WHITE, (0, 0, 1000, 1000))
                        pygame.draw.circle (screen, YELLOW, (x+moveX, y+moveY), 125, 0)
                        pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY), 125, 5)
                        pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY-40), 10, 0)
                        pygame.draw.polygon (screen, WHITE, ((x+moveX, y+moveY), (x+moveX-150, y+moveY+100), (x+moveX-150, y+moveY-100)))
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX-100, y+moveY+70), 5)
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX-100, y+moveY-70), 5)                
                        pygame.display.flip()
                        moveX = moveX - 5  
                        moveCount = moveCount + 1
                        print (moveCount, "4th")
                        pygame.time.wait(20)
                        for event in pygame.event.get():
                            if pygame.K_a == True:
                                a_Pressed = True
                            else:
                                a_Pressed = False                              
                    elif (moveCount % 20) - 17 == 0:
                        pygame.draw.rect(screen, WHITE, (0, 0, 1000, 1000))
                        pygame.draw.circle (screen, YELLOW, (x+moveX, y+moveY), 125, 0)
                        pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY), 125, 5)
                        pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY-40), 10, 0)
                        pygame.draw.polygon (screen, WHITE, ((x+moveX, y+moveY), (x+moveX-150, y+moveY+75), (x+moveX-150, y+moveY-75)))
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX-110, y+moveY+55), 5)
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX-110, y+moveY-55), 5) 
                        pygame.display.flip()
                        moveX = moveX - 5
                        moveCount = moveCount + 1
                        print (moveCount, "4th")
                        pygame.time.wait(20)
                        for event in pygame.event.get():
                            if pygame.K_a == True:
                                a_Pressed = True
                            else:
                                a_Pressed = False
                    elif (moveCount % 20) - 18 == 0:
                        pygame.draw.rect(screen, WHITE, (0, 0, 1000, 1000))
                        pygame.draw.circle (screen, YELLOW, (x+moveX, y+moveY), 125, 0)
                        pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY), 125, 5)
                        pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY-40), 10, 0)
                        pygame.draw.polygon (screen, WHITE, ((x+moveX, y+moveY), (x+moveX-150, y+moveY+50), (x+moveX-150, y+moveY-50)))
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX-115, y+moveY+40), 5)
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX-115, y+moveY-40), 5)   
                        pygame.display.flip()
                        moveX = moveX - 5
                        moveCount = moveCount + 1
                        print (moveCount, "4th")
                        pygame.time.wait(20)
                        for event in pygame.event.get():
                            if pygame.K_a == True:
                                a_Pressed = True
                            else:
                                a_Pressed = False                            
                    else:
                        pygame.draw.rect(screen, WHITE, (0, 0, 1000, 1000))
                        pygame.draw.circle (screen, YELLOW, (x+moveX, y+moveY), 125, 0)
                        pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY), 125, 5)
                        pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY-40), 10, 0)
                        pygame.draw.polygon (screen, WHITE, ((x+moveX, y+moveY), (x+moveX-150, y+moveY+125), (x+moveX-150, y+moveY-125)))
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX-92, y+moveY+80), 5)
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX-92, y+moveY-80), 5)                
                        pygame.display.flip()
                        moveX = moveX - 5
                        moveCount = moveCount + 1
                        print (moveCount)
                        pygame.time.wait(10)
                        for event in pygame.event.get():
                            if pygame.K_a == True:
                                a_Pressed = True
                            else:
                                a_Pressed = False  
    
                pygame.draw.rect(screen, WHITE, (0, 0, 1000, 1000))
                pygame.draw.circle (screen, YELLOW, (x+moveX, y+moveY), 125, 0)
                pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY), 125, 5)
                pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY-40), 10, 0)
                pygame.draw.polygon (screen, WHITE, ((x+moveX, y+moveY), (x+moveX-150, y+moveY+125), (x+moveX-150, y+moveY-125)))
                pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX-92, y+moveY+80), 5)
                pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX-92, y+moveY-80), 5)                
                pygame.display.flip()
                moveX = moveX - 5
                directionOfOpening = 1
                moveCount = moveCount + 1
                print (moveCount)
                pygame.time.wait(10)
            elif key[pygame.K_w] == True:
                key=pygame.key.get_pressed()
                w_Pressed = key[pygame.K_w]
                while w_Pressed == True:
                    if (moveCount % 20) == 0: #or (moveCount %20) - 19 == 0 or (moveCount %20) - 18 == 0
                        pygame.draw.rect(screen, WHITE, (0, 0, 1000, 1000))
                        pygame.draw.circle (screen, YELLOW, (x+moveX, y+moveY), 125, 0)
                        pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY), 125, 5)
                        pygame.draw.circle (screen, BLACK, (x+moveX+40, y+moveY), 10, 0)
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX, y+moveY-124), 5)
                        pygame.display.flip()
                        moveY = moveY - 5
                        moveCount = moveCount + 1
                        print (moveCount, "here")
                        pygame.time.wait(20)
                        for event in pygame.event.get():
                            if pygame.K_w == True:
                                w_Pressed = True
                            else:
                                w_Pressed = False
                    elif (moveCount % 20) - 19 == 0:
                        pygame.draw.rect(screen, WHITE, (0, 0, 1000, 1000))
                        pygame.draw.circle (screen, YELLOW, (x+moveX, y+moveY), 125, 0)
                        pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY), 125, 5)
                        pygame.draw.circle (screen, BLACK, (x+moveX+40, y+moveY), 10, 0)
                        pygame.draw.polygon (screen, WHITE, ((x+moveX, y+moveY), (x+moveX-25, y+moveY-150), (x+moveX+25, y+moveY-150)))
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX-22, y+moveY-120), 5)
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX+22, y+moveY-120), 5)                
                        pygame.display.flip()
                        moveY = moveY - 5  
                        moveCount = moveCount + 1
                        print (moveCount, "4th")
                        pygame.time.wait(20)
                        for event in pygame.event.get():
                            if pygame.K_w == True:
                                w_Pressed = True
                            else:
                                w_Pressed = False                  
                    elif (moveCount % 20) - 16 == 0:
                        pygame.draw.rect(screen, WHITE, (0, 0, 1000, 1000))
                        pygame.draw.circle (screen, YELLOW, (x+moveX, y+moveY), 125, 0)
                        pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY), 125, 5)
                        pygame.draw.circle (screen, BLACK, (x+moveX+40, y+moveY), 10, 0)
                        pygame.draw.polygon (screen, WHITE, ((x+moveX, y+moveY), (x+moveX+100, y+moveY-150), (x+moveX-100, y+moveY-150)))
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX+70, y+moveY-100), 5)
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX-70, y+moveY-100), 5)                
                        pygame.display.flip()
                        moveY = moveY - 5 
                        moveCount = moveCount + 1
                        print (moveCount, "4th")
                        pygame.time.wait(20)
                        for event in pygame.event.get():
                            if pygame.K_w == True:
                                w_Pressed = True
                            else:
                                w_Pressed = False                              
                    elif (moveCount % 20) - 17 == 0:
                        pygame.draw.rect(screen, WHITE, (0, 0, 1000, 1000))
                        pygame.draw.circle (screen, YELLOW, (x+moveX, y+moveY), 125, 0)
                        pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY), 125, 5)
                        pygame.draw.circle (screen, BLACK, (x+moveX+40, y+moveY), 10, 0)
                        pygame.draw.polygon (screen, WHITE, ((x+moveX, y+moveY), (x+moveX+75, y+moveY-150), (x+moveX-75, y+moveY-150)))
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX+55, y+moveY-110), 5)
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX-55, y+moveY-110), 5) 
                        pygame.display.flip()
                        moveY = moveY - 5
                        moveCount = moveCount + 1
                        print (moveCount, "4th")
                        pygame.time.wait(20)
                        for event in pygame.event.get():
                            if pygame.K_w == True:
                                w_Pressed = True
                            else:
                                w_Pressed = False           
                    elif (moveCount % 20) - 18 == 0:
                        pygame.draw.rect(screen, WHITE, (0, 0, 1000, 1000))
                        pygame.draw.circle (screen, YELLOW, (x+moveX, y+moveY), 125, 0)
                        pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY), 125, 5)
                        pygame.draw.circle (screen, BLACK, (x+moveX+40, y+moveY), 10, 0)
                        pygame.draw.polygon (screen, WHITE, ((x+moveX, y+moveY), (x+moveX+50, y+moveY-150), (x+moveX-50, y+moveY-150)))
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX+40, y+moveY-115), 5)
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX-40, y+moveY-115), 5)   
                        pygame.display.flip()
                        moveY = moveY - 5
                        moveCount = moveCount + 1
                        print (moveCount, "4th")
                        pygame.time.wait(20)
                        for event in pygame.event.get():
                            if pygame.K_w == True:
                                w_Pressed = True
                            else:
                                w_Pressed = False                            
                    else:
                        pygame.draw.rect(screen, WHITE, (0, 0, 1000, 1000))
                        pygame.draw.circle (screen, YELLOW, (x+moveX, y+moveY), 125, 0)
                        pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY), 125, 5)
                        pygame.draw.circle (screen, BLACK, (x+moveX+50, y+moveY), 10, 0)
                        pygame.draw.polygon (screen, WHITE, ((x+moveX, y+moveY), (x+moveX+125, y+moveY-150), (x+moveX-125, y+moveY-150)))
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX+80, y+moveY-92), 5)
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX-80, y+moveY-92), 5)                
                        pygame.display.flip()
                        moveY = moveY - 5
                        moveCount = moveCount + 1
                        print (moveCount)
                        pygame.time.wait(10)
                        for event in pygame.event.get():
                            if pygame.K_w == True:
                                w_Pressed = True
                            else:
                                w_Pressed = False 
    
                pygame.draw.rect(screen, WHITE, (0, 0, 1000, 1000))
                pygame.draw.circle (screen, YELLOW, (x+moveX, y+moveY), 125, 0)
                pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY), 125, 5)
                pygame.draw.circle (screen, BLACK, (x+moveX+50, y+moveY), 10, 0)
                pygame.draw.polygon (screen, WHITE, ((x+moveX, y+moveY), (x+moveX+125, y+moveY-150), (x+moveX-125, y+moveY-150)))
                pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX+80, y+moveY-92), 5)
                pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX-80, y+moveY-92), 5)                
                pygame.display.flip()
                moveY = moveY - 5
                directionOfOpening = 2
                moveCount = moveCount + 1
                print (moveCount)
                pygame.time.wait(10)    
            elif key[pygame.K_s] == True:
                key=pygame.key.get_pressed()
                s_Pressed = key[pygame.K_s]
                while s_Pressed == True:
                    if (moveCount % 20) == 0: #or (moveCount %20) - 19 == 0 or (moveCount %20) - 18 == 0
                        pygame.draw.rect(screen, WHITE, (0, 0, 1000, 1000))
                        pygame.draw.circle (screen, YELLOW, (x+moveX, y+moveY), 125, 0)
                        pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY), 125, 5)
                        pygame.draw.circle (screen, BLACK, (x+moveX+40, y+moveY), 10, 0)
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX, y+moveY+124), 5)
                        pygame.display.flip()
                        moveY = moveY + 5
                        moveCount = moveCount + 1
                        print (moveCount, "here")
                        pygame.time.wait(20)
                        for event in pygame.event.get():
                            if pygame.K_s == True:
                                s_Pressed = True
                            else:
                                s_Pressed = False
                    elif (moveCount % 20) - 19 == 0:
                        pygame.draw.rect(screen, WHITE, (0, 0, 1000, 1000))
                        pygame.draw.circle (screen, YELLOW, (x+moveX, y+moveY), 125, 0)
                        pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY), 125, 5)
                        pygame.draw.circle (screen, BLACK, (x+moveX+40, y+moveY), 10, 0)
                        pygame.draw.polygon (screen, WHITE, ((x+moveX, y+moveY), (x+moveX-25, y+moveY+150), (x+moveX+25, y+moveY+150)))
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX-22, y+moveY+120), 5)
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX+22, y+moveY+120), 5)                
                        pygame.display.flip()
                        moveY = moveY + 5  
                        moveCount = moveCount + 1
                        print (moveCount, "4th")
                        pygame.time.wait(20)
                        for event in pygame.event.get():
                            if pygame.K_s == True:
                                s_Pressed = True
                            else:
                                s_Pressed = False                  
                    elif (moveCount % 20) - 16 == 0:
                        pygame.draw.rect(screen, WHITE, (0, 0, 1000, 1000))
                        pygame.draw.circle (screen, YELLOW, (x+moveX, y+moveY), 125, 0)
                        pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY), 125, 5)
                        pygame.draw.circle (screen, BLACK, (x+moveX+40, y+moveY), 10, 0)
                        pygame.draw.polygon (screen, WHITE, ((x+moveX, y+moveY), (x+moveX+100, y+moveY+150), (x+moveX-100, y+moveY+150)))
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX+70, y+moveY+100), 5)
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX-70, y+moveY+100), 5)                
                        pygame.display.flip()
                        moveY = moveY + 5 
                        moveCount = moveCount + 1
                        print (moveCount, "4th")
                        pygame.time.wait(20)
                        for event in pygame.event.get():
                            if pygame.K_s == True:
                                s_Pressed = True
                            else:
                                s_Pressed = False                              
                    elif (moveCount % 20) - 17 == 0:
                        pygame.draw.rect(screen, WHITE, (0, 0, 1000, 1000))
                        pygame.draw.circle (screen, YELLOW, (x+moveX, y+moveY), 125, 0)
                        pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY), 125, 5)
                        pygame.draw.circle (screen, BLACK, (x+moveX+40, y+moveY), 10, 0)
                        pygame.draw.polygon (screen, WHITE, ((x+moveX, y+moveY), (x+moveX+75, y+moveY+150), (x+moveX-75, y+moveY+150)))
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX+55, y+moveY+110), 5)
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX-55, y+moveY+110), 5) 
                        pygame.display.flip()
                        moveY = moveY + 5
                        moveCount = moveCount + 1
                        print (moveCount, "4th")
                        pygame.time.wait(20)
                        for event in pygame.event.get():
                            if pygame.K_s == True:
                                s_Pressed = True
                            else:
                                s_Pressed = False           
                    elif (moveCount % 20) - 18 == 0:
                        pygame.draw.rect(screen, WHITE, (0, 0, 1000, 1000))
                        pygame.draw.circle (screen, YELLOW, (x+moveX, y+moveY), 125, 0)
                        pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY), 125, 5)
                        pygame.draw.circle (screen, BLACK, (x+moveX+40, y+moveY), 10, 0)
                        pygame.draw.polygon (screen, WHITE, ((x+moveX, y+moveY), (x+moveX+50, y+moveY+150), (x+moveX-50, y+moveY+150)))
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX+40, y+moveY+115), 5)
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX-40, y+moveY+115), 5)   
                        pygame.display.flip()
                        moveY = moveY + 5
                        moveCount = moveCount + 1
                        print (moveCount, "4th")
                        pygame.time.wait(20)
                        for event in pygame.event.get():
                            if pygame.K_s == True:
                                s_Pressed = True
                            else:
                                s_Pressed = False                            
                    else:
                        pygame.draw.rect(screen, WHITE, (0, 0, 1000, 1000))
                        pygame.draw.circle (screen, YELLOW, (x+moveX, y+moveY), 125, 0)
                        pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY), 125, 5)
                        pygame.draw.circle (screen, BLACK, (x+moveX+50, y+moveY), 10, 0)
                        pygame.draw.polygon (screen, WHITE, ((x+moveX, y+moveY), (x+moveX+125, y+moveY+150), (x+moveX-125, y+moveY+150)))
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX+80, y+moveY+92), 5)
                        pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX-80, y+moveY+92), 5)                
                        pygame.display.flip()
                        moveY = moveY + 5
                        moveCount = moveCount + 1
                        print (moveCount)
                        pygame.time.wait(10)
                        for event in pygame.event.get():
                            if pygame.K_s == True:
                                s_Pressed = True
                            else:
                                s_Pressed = False 
    
                pygame.draw.rect(screen, WHITE, (0, 0, 1000, 1000))
                pygame.draw.circle (screen, YELLOW, (x+moveX, y+moveY), 125, 0)
                pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY), 125, 5)
                pygame.draw.circle (screen, BLACK, (x+moveX+50, y+moveY), 10, 0)
                pygame.draw.polygon (screen, WHITE, ((x+moveX, y+moveY), (x+moveX+125, y+moveY+150), (x+moveX-125, y+moveY+150)))
                pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX+80, y+moveY+92), 5)
                pygame.draw.line (screen, BLACK, (x+moveX, y+moveY), (x+moveX-80, y+moveY+92), 5)                
                pygame.display.flip()
                moveY = moveY + 5
                directionOfOpening = 4
                moveCount = moveCount + 1
                print (moveCount)
                pygame.time.wait(10) 
            elif key[pygame.K_ESCAPE] == True:
                key=pygame.key.get_pressed()
                ESCAPE_Pressed = key[pygame.K_ESCAPE]
                if ESCAPE_Pressed == True:
                    true = False 
                    sys.exit()


print ("Hi")
a = threading.Thread(name = 'foreGround', target = foreGround())
b = threading.Thread(name = 'shootBullet', target = shootBullet())

a.start()
sys.exit()
#b.start()
#moveX = 200
#moveY = 0
#x = 150
#y = 150
#pygame.draw.rect(screen, WHITE, (0, 0, 1000, 1000))
#pygame.draw.arc (screen, YELLOW, (x+moveX, y+moveY, x+100, y+100), 0.698132, 5.58505, 50)
#pygame.draw.circle (screen, BLACK, (x + 60, y + 35), 8, 0)
#pygame.display.flip()

pygame.time.wait(1000)
pygame.quit()