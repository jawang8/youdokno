Lay1X = 150
Lay2X = 150
Lay3X = 150
Lay4X = 150
Lay5X = 150
Lay6X = 150
Lay7X = 150
Lay8X = 150
Lay9X = 150
Lay10X = 150

Lay1Y = 525
Lay2Y = 500
Lay3Y = 475
Lay4Y = 450
Lay5Y = 425
Lay6Y = 400
Lay7Y = 375
Lay8Y = 350
Lay9Y = 325
Lay10Y = 300

DirL1X = RIGHT


Level = 1
def setup():
    size(300,600)
    rectMode(CENTER)
    noStroke()
    text("Level",20,20)
    text(Level,50,20)

    
def draw():
    global Level
    background(225,225,225)
    if (Level == 1):
        Layone()
        Layonemov()
        Layonem() 
        showLevel()
    if (Level == 2):
        Layone()
        Laytwo()
        Laytwomov()
        Laytwom()
        showLevel()
    if (Level == 3):
        Layone()
        Laytwo()
        Laythr()
        Laythrmov()
        Laythrm()
        showLevel()        
    if (Level == 4):
        Layone()
        Laytwo()
        Laythr()
        Layfou()
        Layfoumov()
        Layfoum()
        showLevel()
    if (Level == 5):
        Layone()
        Laytwo()
        Laythr()
        Layfou()
        Layfiv()
        Layfivmov()
        Layfivm()
        showLevel()
    if (Level == 6):
        Layone()
        Laytwo()
        Laythr()
        Layfou()
        Layfiv()
        Laysix()
        Laysixmov()
        Laysixm()
        showLevel()
    if (Level == 7):
        Layone()
        Laytwo()
        Laythr()
        Layfou()
        Layfiv()
        Laysix()
        Laysev()
        Laysevmov()
        Laysevm()
        showLevel()
    if (Level == 8):
        Layone()
        Laytwo()
        Laythr()
        Layfou()
        Layfiv()
        Laysix()
        Laysev()
        Layeig()
        Layeigmov()
        Layeigm()
        showLevel()
    if (Level == 9):
        Layone()
        Laytwo()
        Laythr()
        Layfou()
        Layfiv()
        Laysix()
        Laysev()
        Layeig()
        Laynin()
        Layninmov()
        Layninm()
        showLevel()
    if (Level == 10):
        Layone()
        Laytwo()
        Laythr()
        Layfou()
        Layfiv()
        Laysix()
        Laysev()
        Layeig()
        Laynin()
        Layten()
        Laytenmov()
        Laytenm()
        showLevel()
    if (Level == 11):
        Layone()
        Laytwo()
        Laythr()
        Layfou()
        Layfiv()
        Laysix()
        Laysev()
        Layeig()
        Laynin()
        Layten()
        fill(100,100,100)
        textSize(50)
        text("Winner",75,250)
    if (Level == 12):
        Level = 1

def mousePressed():
    global Level
    Level = Level + 1

def showLevel():
    textSize(20)
    text("Level",20,30)
    text(Level,70,30)

#level 1

def Layone():
    global Lay1X
    fill(60,100,255)
    rect(Lay1X,Lay1Y,150,25)
    fill(255,0,0)
    rect(Lay1X,Lay1Y,1,25)
    
def Layonemov():
    global Lay1X, DirL1X
    Lay1X = Lay1X + 1
    
    if (Lay1X > 300):
        DirL1X = LEFT
        
    if (Lay1X < 0):
        DirL1X = RIGHT

def Layonem():
    global Lay1X, DirL1X    
    if (DirL1X == LEFT):
        Lay1X = Lay1X - 6
        
    if (DirL1X == RIGHT):
        Lay1X = Lay1X + 4

        
                
#level 2                
                                        
def Laytwo():
    global Lay2X
    fill(60,100,255)
    rect(Lay2X,500,140,25)
    fill(255,0,0)
    rect(Lay2X,Lay2Y,1,25)
    
def Laytwomov():
    global Lay2X, DirL1X
    Lay2X = Lay2X + 1
    
    if (Lay2X > 300):
        DirL1X = LEFT
        
    if (Lay2X < 0):
        DirL1X = RIGHT

def Laytwom():
    global Lay2X, DirL1X    
    if (DirL1X == LEFT):
        Lay2X = Lay2X - 7
        
    if (DirL1X == RIGHT):
        Lay2X = Lay2X + 5
        

#level 3

def Laythr():
    global Lay3X
    fill(60,100,255)
    rect(Lay3X,475,130,25)
    fill(255,0,0)
    rect(Lay3X,Lay3Y,1,25)
    
def Laythrmov():
    global Lay3X, DirL1X
    Lay3X = Lay3X + 1
    
    if (Lay3X > 300):
        DirL1X = LEFT
        
    if (Lay3X < 0):
        DirL1X = RIGHT

def Laythrm():
    global Lay3X, DirL1X    
    if (DirL1X == LEFT):
        Lay3X = Lay3X - 8
        
    if (DirL1X == RIGHT):
        Lay3X = Lay3X + 6
        
#level 4

def Layfou():
    global Lay4X
    fill(60,100,255)
    rect(Lay4X,450,120,25)
    fill(255,0,0)
    rect(Lay4X,Lay4Y,1,25)
    
def Layfoumov():
    global Lay4X, DirL1X
    Lay4X = Lay4X + 1
    
    if (Lay4X > 300):
        DirL1X = LEFT
        
    if (Lay4X < 0):
        DirL1X = RIGHT

def Layfoum():
    global Lay4X, DirL1X    
    if (DirL1X == LEFT):
        Lay4X = Lay4X - 9
        
    if (DirL1X == RIGHT):
        Lay4X = Lay4X + 7
    
#level 5

def Layfiv():
    global Lay5X
    fill(60,100,255)
    rect(Lay5X,425,110,25)
    fill(255,0,0)
    rect(Lay5X,Lay5Y,1,25)
    
def Layfivmov():
    global Lay5X, DirL1X
    Lay5X = Lay5X + 1
    
    if (Lay5X > 300):
        DirL1X = LEFT
        
    if (Lay5X < 0):
        DirL1X = RIGHT

def Layfivm():
    global Lay5X, DirL1X    
    if (DirL1X == LEFT):
        Lay5X = Lay5X - 10
        
    if (DirL1X == RIGHT):
        Lay5X = Lay5X + 8

#level 6

def Laysix():
    global Lay6X
    fill(60,100,255)
    rect(Lay6X,400,100,25)
    fill(255,0,0)
    rect(Lay6X,Lay6Y,1,25)
    
def Laysixmov():
    global Lay6X, DirL1X
    Lay6X = Lay6X + 1
    
    if (Lay6X > 300):
        DirL1X = LEFT
        
    if (Lay6X < 0):
        DirL1X = RIGHT

def Laysixm():
    global Lay6X, DirL1X    
    if (DirL1X == LEFT):
        Lay6X = Lay6X - 11
        
    if (DirL1X == RIGHT):
        Lay6X = Lay6X + 9

#level 7

def Laysev():
    global Lay7X
    fill(60,100,255)
    rect(Lay7X,375,90,25)
    fill(255,0,0)
    rect(Lay7X,Lay7Y,1,25)
    
def Laysevmov():
    global Lay7X, DirL1X
    Lay7X = Lay7X + 1
    
    if (Lay7X > 300):
        DirL1X = LEFT
        
    if (Lay7X < 0):
        DirL1X = RIGHT

def Laysevm():
    global Lay7X, DirL1X    
    if (DirL1X == LEFT):
        Lay7X = Lay7X - 12
        
    if (DirL1X == RIGHT):
        Lay7X = Lay7X + 10   
        
#level 8

def Layeig():
    global Lay8X
    fill(60,100,255)
    rect(Lay8X,350,80,25)
    fill(255,0,0)
    rect(Lay8X,Lay8Y,1,25)
    
def Layeigmov():
    global Lay8X, DirL1X
    Lay8X = Lay8X + 1
    
    if (Lay8X > 300):
        DirL1X = LEFT
        
    if (Lay8X < 0):
        DirL1X = RIGHT

def Layeigm():
    global Lay8X, DirL1X    
    if (DirL1X == LEFT):
        Lay8X = Lay8X - 13
        
    if (DirL1X == RIGHT):
        Lay8X = Lay8X + 11  
        
#level 9

def Laynin():
    global Lay9X
    fill(60,100,255)
    rect(Lay9X,325,70,25)
    fill(255,0,0)
    rect(Lay9X,Lay9Y,1,25)
    
def Layninmov():
    global Lay9X, DirL1X
    Lay9X = Lay9X + 1
    
    if (Lay9X > 300):
        DirL1X = LEFT
        
    if (Lay9X < 0):
        DirL1X = RIGHT

def Layninm():
    global Lay9X, Dir9X    
    if (DirL1X == LEFT):
        Lay9X = Lay9X - 14
        
    if (DirL1X == RIGHT):
        Lay9X = Lay9X + 12
        
#level 10

def Layten():
    global Lay10X
    fill(60,100,255)
    rect(Lay10X,300,60,25)
    fill(255,0,0)
    rect(Lay10X,Lay10Y,1,25)
    
def Laytenmov():
    global Lay10X, DirL1X
    Lay10X = Lay10X + 1
    
    if (Lay10X > 300):
        DirL1X = LEFT
        
    if (Lay10X < 0):
        DirL1X = RIGHT

def Laytenm():
    global Lay10X, DirL1X    
    if (DirL1X == LEFT):
        Lay10X = Lay10X - 15
        
    if (DirL1X == RIGHT):
        Lay10X = Lay10X + 13