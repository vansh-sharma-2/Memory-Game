import pygame , random

pygame.init()

screen=pygame.display.set_mode((1000,600))

bg=pygame.image.load("assets\\background.png")

font=pygame.font.Font("freesansbold.ttf",32)
text=font.render("Memory Game",True,(0,0,0))
textObj=text.get_rect()
textObj.center=(500,25)
fps=60
fpsClock=pygame.time.Clock()
Size=82

image_cache={}

def get_image(src):
    if src not in image_cache:
        image_cache[src]=pygame.transform.scale(pygame.image.load(src),(Size,Size))
    return image_cache[src]

class tile:
    size=Size
    def __init__(self,type):
        self.type=type
    
    def load(self):
        self.src="assets\\"+self.type+".png"
        return get_image(self.src)

book=tile("book")
crown=tile("crown")
egg=tile("egg")
heart=tile("heart")
hat=tile("hat")
key=tile("key")
potion=tile("potion")
sword=tile("sword")
treasure=tile("treasure")
unknown=tile("unknown")
book.load(),crown.load(),egg.load(),heart.load(),hat.load(),key.load(),potion.load(),sword.load(),treasure.load(),unknown.load()

tile_types=[book,crown,egg,heart,hat,key,potion,sword,treasure]

mainarea_x,mainarea_y=100,88

x_data=[]
visible_data=[]

screen.fill((158,250,255))
screen.blit(text,textObj)
screen.blit(bg,(mainarea_x,mainarea_y))

def updateTiles(*arg):
    for j in range(4):
            for i in range(8):
                if (i==arg[0] and j==arg[1]) or (i==arg[2] and j==arg[3]):
                    val=x_data[j][i]
                else:
                    val=visible_data[j][i]
                screen.blit(val.load(),(mainarea_x+35+(i*10)+(Size*i),mainarea_y+34+(j*9)+(Size*j)))

for j in range(4):
        temp=[]
        temp1=[]
        for i in range(8):
            val=unknown
            screen.blit(val.load(),(mainarea_x+35+(i*10)+(Size*i),mainarea_y+34+(j*9)+(Size*j)))
            temp.append("")
            temp1.append(unknown)
        x_data.append(temp)
        visible_data.append(temp1)

list=[]
indexes=[]
for i in range(32):
    list.append("")
    indexes.append(i)
while len(indexes)>0:
    temp=random.choice(tile_types)
    t1=random.choice(indexes)
    list[t1]=temp
    indexes.remove(t1)
    t2=random.choice(indexes)
    list[t2]=temp
    indexes.remove(t2)
for i in range(4):
    for j in range(8):
        x_data[i][j]=list.pop(0)

def get_x(x):
    x1Values=[]
    for i in range(8):
        x1Values.append(mainarea_x+35+(i*10)+(Size*i))
    x2Values=[]
    for i in range(8):
        x2Values.append(mainarea_x+35+Size+(i*10)+(Size*i))
    for i in range(8):
        if x>x1Values[i] and x<x2Values[i]:
            return i
    return None
    

def get_y(y):
    y1Values=[]
    for i in range(4):
        y1Values.append(mainarea_y+34+(i*9)+(Size*i))
    y2Values=[]
    for i in range(4):
        y2Values.append(mainarea_y+34+Size+(i*9)+(Size*i))
    for i in range(4):
        if y>y1Values[i] and y<y2Values[i]:
            return i
    return None

run=True
mouse_press=False
revealed=[]
timer=0
t1=[[0,0],[0,0]]
matched_count=0
total_pairs=16
win_font=pygame.font.Font("freesansbold.ttf",64)

while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False
    pygame.display.update()
    if timer>0:
        updateTiles(t1[0][0],t1[0][1],t1[1][0],t1[1][1])
        timer-=1
        fpsClock.tick(fps)
        continue
    if pygame.mouse.get_pressed()[0]:
        mouse_press=True
    x,y=get_x(pygame.mouse.get_pos()[0]),get_y(pygame.mouse.get_pos()[1])

    if not(pygame.mouse.get_pressed()[0]) and x!=None and y!=None and mouse_press==True:
        if visible_data[y][x]!=unknown:
            mouse_press=False
        elif len(revealed)<2:
            if len(revealed)==0 or revealed[0]!=[x,y]:
                revealed.append([x,y])
            mouse_press=False

    if len(revealed)==0:
        updateTiles(-1,-1,-1,-1)
    elif len(revealed)==1:
        updateTiles(revealed[0][0],revealed[0][1],-1,-1)
    elif len(revealed)==2:
        updateTiles(revealed[0][0],revealed[0][1],revealed[1][0],revealed[1][1])
        if x_data[revealed[0][1]][revealed[0][0]]==x_data[revealed[1][1]][revealed[1][0]]:
            visible_data[revealed[0][1]][revealed[0][0]],visible_data[revealed[1][1]][revealed[1][0]]=x_data[revealed[1][1]][revealed[1][0]],x_data[revealed[1][1]][revealed[1][0]]
            matched_count+=1
        else:
            timer=25
        t1=[[revealed[0][0],revealed[0][1]],[revealed[1][0],revealed[1][1]]]
        revealed.clear()
    if matched_count==total_pairs:
        win_text=win_font.render("You Win!",True,(0,180,0))
        win_rect=win_text.get_rect()
        win_rect.center=(500,300)
        screen.blit(win_text,win_rect)
        pygame.display.update()
        pygame.time.wait(3000)
        run=False
    fpsClock.tick(fps)
pygame.quit()