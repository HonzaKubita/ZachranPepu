import time
import pygame
import os
from pygame.locals import *
from pygame import mixer

version = "Alpha 1.2"

pygame.init()

appdataloc = os.getenv('APPDATA')
appdataloc.replace('\\', '//')
print (appdataloc)
gamefilepath = appdataloc + '/ZachranPepu/gamedata.txt'
print(gamefilepath)
folder = appdataloc + '/ZachranPepu'

if not os.path.exists(folder):
  os.makedirs(folder)
  o = open(gamefilepath, "w+")
  o.close()

screen_width = 501
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Zachran PEPU!')
pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
programIcon = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/milk.png')
pygame.display.set_icon(programIcon)

#Variables

pos = pygame.mouse.get_pos()
clicked = False
clickedback = False
lvl1completed = False
lvl2completed = False
lvl3completed = False
lvl4completed = False
lvl5completed = False
lvl6completed = False
lvl7completed = False
lvl8completed = False
lvl9completed = False
Score = 0
BLACK = (0,0,0)
cursoronButton = False
counttux = 0
pointed = False
achievement1 = False
achievement2 = False
achievement3 = False
achievement4 = False
Scorelvl1 = 0
Scorelvl2 = 0
Scorelvl3 = 0
Scorelvl4 = 0
Scorelvl5 = 0
Scorelvl6 = 0
Scorelvl7 = 0
Scorelvl8 = 0
Scorelvl9 = 0
exitedlvl = True
muted = False

f = open(gamefilepath, "r+") #datafile operations - hearts
if f.mode == "r+":
  datafile = f.read()
  print("Reading")
  print(datafile)
  if "0hearts" in datafile:
    print("0hearts")
    zivoty = 0
  elif "1hearts" in datafile:
    print("1Heart")
    zivoty = 1
  elif "2hearts" in datafile:
    print("2Hearts")
    zivoty = 2
  elif "3hearts" in datafile:
    #nice
    print("3Hearts")
    zivoty = 3
  else:
    zivoty = 3
f.close()

f = open(gamefilepath, "r+") #datafile operations - achievements
if f.mode == "r+":
  datafile = f.read()
  print("Reading")
  print(datafile)
  if "achievement1 == True" in datafile:
    print("dataachievement1 = True")
    dataachievement1 = True
  else:
    dataachievement1 = False
    print("dataachievement1 = False")

  if "achievement2 == True" in datafile:
    print("dataachievement2 = True")
    dataachievement2 = True
  else:
    dataachievement2 = False
    print("dataachievement2 = False") 
f.close()


def clip(surf,x,y,x_size,y_size):
    handle_surf = surf.copy()
    clipR = pygame.Rect(x,y,x_size,y_size)
    handle_surf.set_clip(clipR)
    image = surf.subsurface(handle_surf.get_clip())
    return image.copy()

class Font():
  def __init__(self, path):
    self.spacing = 1
    self.character_order = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','.','-',',',':','+','\'','!','?','0','1','2','3','4','5','6','7','8','9','(',')','/','_','=','\\','[',']','*','"','<','>',';']
    font_img = pygame.image.load(path).convert()
    current_char_width = 0
    self.characters = {}
    character_count = 0
    for x in range(font_img.get_width()):
      c = font_img.get_at((x, 0))
      if c[0] == 127:
        char_img = clip(font_img, x - current_char_width, 0, current_char_width, font_img.get_height())
        self.characters[self.character_order[character_count]] = char_img.copy()
        character_count += 1
        current_char_width = 0
      else:
        current_char_width += 1
    self.space_width = self.characters['A'].get_width()

  def render(self, surf, text, loc):
    x_offset = 0
    for char in text:
      if char != ' ':
        surf.blit(self.characters[char], (loc[0] + x_offset, loc[1]))
        x_offset += self.characters[char].get_width() + self.spacing
      else:
        x_offset += self.space_width + self.spacing

# Init ------------------------------------------------------- #

# my_font.render(screen, 'Hello World!', (20, 20))
# my_big_font.render(screen, 'Hello World!', (20, 40))


#load images
bg1_img = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/bg0.png')
playbutton0 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/playbutton_0.png')
playbutton1 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/playbutton_1.png')
quitbutton0 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/quitbutton_0.png')
quitbutton1 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/quitbutton_1.png')
lvlsel0_1 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/lvlsel0_0.png')
lvlsel0_2 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/lvlsel0_1.png')
lvlsel0_3 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/lvlsel0_2.png')
lvlsel0_4 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/lvlsel0_3.png')
lvlsel0_5 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/lvlsel0_4.png')
lvlsel0_6 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/lvlsel0_5.png')
lvlsel0_7 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/lvlsel0_6.png')
lvlsel0_8 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/lvlsel0_7.png')
lvlsel0_9 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/lvlsel0_8.png')

lvlsel1_1 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/lvlsel1_0.png')
lvlsel1_2 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/lvlsel1_1.png')
lvlsel1_3 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/lvlsel1_2.png')
lvlsel1_4 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/lvlsel1_3.png')
lvlsel1_5 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/lvlsel1_4.png')
lvlsel1_6 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/lvlsel1_5.png')
lvlsel1_7 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/lvlsel1_6.png')
lvlsel1_8 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/lvlsel1_7.png')
lvlsel1_9 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/lvlsel1_8.png')
my_font = Font('C:/Program Files (x86)/ZachranPepu/Hra/font_system/small_font.png')
my_big_font = Font('C:/Program Files (x86)/ZachranPepu/Hra/font_system/large_font.png')
logo = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/logo.png')
heart = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/heart.png')
creditsbutton0 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/creditsbutton0.png')
creditsbutton1 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/creditsbutton1.png')
names = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/names.png')
backbutton0 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/backbutton0.png')
backbutton1 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/backbutton1.png')
odpocet3 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/odpocet_3.png')
odpocet2 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/odpocet_2.png')
odpocet1 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/odpocet_1.png')
checkmark = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/checkmark.png')
downline1 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/downline1.png')
downline0 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/downline0.png')
linuxpicture = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/Linux_mascot_1.png')
cursorimg = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/cursorimg.png')
cursor2img = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/cursor2img.png')
bubbletux = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/bubbletux.png')
bubbletux2 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/bubbletux2.png')
achievementbutton0 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/achievementbutton0.png')
achievementbutton1 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/achievementbutton1.png')
pepa1 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/pepa1.png')
pepadeadimg = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/pepadeadimg.png')
milk = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/milk.png')
resetbutton0 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/resetbutton0.png')
resetbutton1 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/resetbutton1.png')
soundOff =  pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/SoundOff.png')
soundOn =  pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/SoundOn.png')

achievement1img = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/achievement1.png')
achievement1blackimg = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/achievement1black.png')
achievement2img = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/achievement2.png')
achievement2blackimg = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/achievement2black.png')


question1 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/question1.png')
question2 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/question2.png')
question3 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/question3.png')
question4 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/question4.png')
question5 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/question5.png')
question6 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/question6.png')
question7 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/question7.png')
question8 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/question8.png')
question9 = pygame.image.load('C:/Program Files (x86)/ZachranPepu/Hra/images/question9.png')

#load sounds and music
pygame.mixer.music.load('C:/Program Files (x86)/ZachranPepu/Hra/music/menusmusic.wav')
pepaisdead = mixer.Sound('C:/Program Files (x86)/ZachranPepu/Hra/sounds/pepaisdead.wav')
playbuttonSound = mixer.Sound('C:/Program Files (x86)/ZachranPepu/Hra/sounds/playbutton.wav')
resetbuttonSound = mixer.Sound('C:/Program Files (x86)/ZachranPepu/Hra/sounds/resetbutton.wav')
lvlselButton = mixer.Sound('C:/Program Files (x86)/ZachranPepu/Hra/sounds/lvlselSoundMouse.wav')

pygame.mixer.music.play(-1)

#buttons def

def achievementscalc():
  global dataachievement1
  global achievement1
  global achievement2
  global achievement3
  global achievement4
  if lvl1completed == True and lvl2completed == True and lvl3completed == True and lvl4completed == True and lvl5completed == True and lvl6completed == True and lvl7completed == True and lvl8completed == True and lvl9completed == True or dataachievement1 == True:
    achievement1 = True
    if dataachievement1 == False:
      f = open(gamefilepath, "a") # write down player completed achievement
      if f.mode == "a":
        f.write('achievement1 == True')
        print("Writing")
        print(datafile)
      dataachievement1 = True
      f.close()
if dataachievement2 == True:
  achievement2 = True
else:
  achievement2 = False

def playbutton():
  if pos[0] > 153 and pos[0] < 153 + 195:
    if pos[1] > 355 and pos[1] < 355 + 65:
      #print("OnButton")
      screen.blit(playbutton1, (153,355))
      if event.type == pygame.MOUSEBUTTONDOWN:
        playbuttonSound.play()
        return True
    else:
      #print("OutOfButton")
      screen.blit(playbutton0, (153,355))
  else:
    #print("OutOfButton")
    screen.blit(playbutton0, (153,355))

def quitbutton():
  if pos[0] > 453 and pos[0] < 453 + 39:
    if pos[1] > 10 and pos[1] < 10 + 13:
      #print("OnButton")
      screen.blit(quitbutton1, (453,10))
      if event.type == pygame.MOUSEBUTTONDOWN:
        return True
    else:
      #print("OutOfButton")
      screen.blit(quitbutton0, (453,10))
  else:
    #print("OutOfButton")

    screen.blit(quitbutton0, (453,10))

def creditsbutton():
  if pos[0] > 440 and pos[0] < 440 + 43:
    if pos[1] > 463 and pos[1] < 463 + 13:
      #print("OnButton")
      screen.blit(creditsbutton1, (440,463))
      if event.type == pygame.MOUSEBUTTONDOWN:
        playbuttonSound.play()
        return True
    else:
      #print("OutOfButton")
      screen.blit(creditsbutton0, (440,463))
  else:
    #print("OutOfButton")
    screen.blit(creditsbutton0, (440,463))

def soundbutton():
  global muted
  if muted:
    screen.blit(soundOff, (20,20))
  else:
    screen.blit(soundOn, (20,20))
  if pos[0] > 20 and pos[0] < 20 + 15:
    if pos[1] > 20 and pos[1] < 20 + 17:
      #print("OnButton")
      if event.type == pygame.MOUSEBUTTONDOWN:
        if muted:
          pygame.mixer.music.play(-1)
          playbuttonSound.play()
          muted = False
        else:
          pygame.mixer.music.stop()
          playbuttonSound.play()
          muted = True
        time.sleep(0.2)

def resetbutton():
  global gamefilepath
  if pos[0] > 440 and pos[0] < 440 + 43:
    if pos[1] > 443 and pos[1] < 443 + 13:
      #print("OnButton")
      screen.blit(resetbutton1, (440,443))
      if event.type == pygame.MOUSEBUTTONDOWN:
        resetbuttonSound.play()
        os.remove(gamefilepath)
        print("deleted")
        time.sleep(0.1)
        f = open(gamefilepath, "w+")
        f.close()
        time.sleep(0.1)
    else:
      #print("OutOfButton")
      screen.blit(resetbutton0, (440,443))
  else:
    #print("OutOfButton")
    screen.blit(resetbutton0, (440,443))

def clickachievements():
  if pos[0] > 127.5 and pos[0] < 127.5 + 245:
    if pos[1] > 425 and pos[1] < 425 + 65:
      #print("OnButton")
      screen.blit(achievementbutton1, (127.5,425))
      if event.type == pygame.MOUSEBUTTONDOWN:
        playbuttonSound.play()
        return True
    else:
      #print("OutOfButton")
      screen.blit(achievementbutton0, (127.5,425))
  else:
    #print("OutOfButton")
    screen.blit(achievementbutton0, (127.5,425))

def levelsmenudraw():
  global Scorelvl1
  global Scorelvl2
  global Scorelvl3
  global Scorelvl4
  global Scorelvl5
  global Scorelvl6
  global Scorelvl7
  global Scorelvl8
  global Scorelvl9
  pygame.draw.rect(screen, BLACK,(0,25,500,30))
  my_big_font.render(screen, 'Score:', (120, 30))
  Scorestr = int(Scorelvl1) + int(Scorelvl2) + int(Scorelvl3) + int(Scorelvl4) + int(Scorelvl5) + int(Scorelvl6) + int(Scorelvl7) + int(Scorelvl8) + int(Scorelvl9)
  my_big_font.render(screen, str(Scorestr), (170, 30))

  my_big_font.render(screen, 'LEVELS', (10, 30))

  screen.blit(lvlsel0_1, (50, 75))
  screen.blit(lvlsel0_2, (200, 75))
  screen.blit(lvlsel0_3, (350, 75))
  screen.blit(lvlsel0_4, (50, 225))
  screen.blit(lvlsel0_5, (200, 225))
  screen.blit(lvlsel0_6, (350, 225))
  screen.blit(lvlsel0_7, (50, 375))
  screen.blit(lvlsel0_8, (200, 375))
  screen.blit(lvlsel0_9, (350, 375))

def levelselect():
  if pos[0] > 50 and pos[0] < 50 + 100:
    if pos[1] > 75 and pos[1] < 75 + 100:
      screen.blit(lvlsel1_1, (50,75))
      if event.type == pygame.MOUSEBUTTONDOWN: # level1
        print("clicked-lvl1")
        return 1
    else:
      screen.blit(lvlsel0_1, (50,75))
  else:
    screen.blit(lvlsel0_1, (50,75))

  if pos[0] > 200 and pos[0] < 200 + 100:
    if pos[1] > 75 and pos[1] < 75 + 100:
      screen.blit(lvlsel1_2, (200,75))
      if event.type == pygame.MOUSEBUTTONDOWN: #level2
        print("clicked-lvl2")
        return 2
    else:
      screen.blit(lvlsel0_2, (200,75))
  else:
    screen.blit(lvlsel0_2, (200,75))

  if pos[0] > 350 and pos[0] < 350 + 100:
    if pos[1] > 75 and pos[1] < 75 + 100:
      screen.blit(lvlsel1_3, (350,75))
      if event.type == pygame.MOUSEBUTTONDOWN: #levle3
        print("clicked-lvl3")
        return 3
    else:
      screen.blit(lvlsel0_3, (350,75))
  else:
    screen.blit(lvlsel0_3, (350,75))
  
  if pos[0] > 50 and pos[0] < 50 + 100:
    if pos[1] > 225 and pos[1] < 225 + 100:
      screen.blit(lvlsel1_4, (50,225))
      if event.type == pygame.MOUSEBUTTONDOWN: #level4
        print("clicked-lvl4")
        return 4
    else:
      screen.blit(lvlsel0_4, (50,225))
  else:
    screen.blit(lvlsel0_4, (50,225))

  if pos[0] > 200 and pos[0] < 200 + 100:
    if pos[1] > 225 and pos[1] < 225 + 100:
      screen.blit(lvlsel1_5, (200,225))
      if event.type == pygame.MOUSEBUTTONDOWN: #level5
        print("clicked-lvl5")
        return 5
    else:
      screen.blit(lvlsel0_5, (200,225))
  else:
    screen.blit(lvlsel0_5, (200,225))

  if pos[0] > 350 and pos[0] < 350 + 100:
    if pos[1] > 225 and pos[1] < 225 + 100:
      screen.blit(lvlsel1_6, (350,225))
      if event.type == pygame.MOUSEBUTTONDOWN: #level6
        print("clicked-lvl6")
        return 6
    else:
      screen.blit(lvlsel0_6, (350,225))
  else:
    screen.blit(lvlsel0_6, (350,225))
  
  if pos[0] > 50 and pos[0] < 50 + 100:
    if pos[1] > 375 and pos[1] < 375 + 100:
      screen.blit(lvlsel1_7, (50,375))
      if event.type == pygame.MOUSEBUTTONDOWN: #level7
        print("clicked-lvl7")
        return 7
    else:
      screen.blit(lvlsel0_7, (50,375))
  else:
    screen.blit(lvlsel0_7, (50,375))
  
  if pos[0] > 200 and pos[0] < 200 + 100:
    if pos[1] > 375 and pos[1] < 375 + 100:
      screen.blit(lvlsel1_8, (200,375))
      if event.type == pygame.MOUSEBUTTONDOWN: #level8
        print("clicked-lvl7")
        return 8
    else:
      screen.blit(lvlsel0_8, (200,375))
  else:
    screen.blit(lvlsel0_8, (200,375))

  if pos[0] > 350 and pos[0] < 350 + 100:
    if pos[1] > 375 and pos[1] < 375 + 100:
      screen.blit(lvlsel1_9, (350,375))
      if event.type == pygame.MOUSEBUTTONDOWN: #level9
        print("clicked-lvl9")
        return 9
    else:
      screen.blit(lvlsel0_9, (350,375))
  else:
    screen.blit(lvlsel0_9, (350,375))
  
def checkmarks():

  if lvl1completed:
    screen.blit(checkmark, (140, 75)) # +90
  if lvl2completed:
    screen.blit(checkmark, (290, 75)) # +90
  if lvl3completed:
    screen.blit(checkmark, (440, 75)) # +90
  if lvl4completed:
    screen.blit(checkmark, (140, 225)) # +90
  if lvl5completed:
    screen.blit(checkmark, (290, 225)) # +90
  if lvl6completed:
    screen.blit(checkmark, (440, 225)) # +90
  if lvl7completed:
    screen.blit(checkmark, (140, 375)) # +90
  if lvl8completed:
    screen.blit(checkmark, (290, 375)) # +90
  if lvl9completed:
    screen.blit(checkmark, (440, 375)) # +90

def odpocet():
  screen.blit(bg1_img, (0, 0))
  pygame.display.update()
  time.sleep(1)
  screen.blit(bg1_img, (0, 0))
  screen.blit(odpocet3, (239,237))
  pygame.display.update()
  time.sleep(1)
  screen.blit(bg1_img, (0, 0))
  screen.blit(odpocet2, (239,237))
  pygame.display.update()
  time.sleep(1)
  screen.blit(bg1_img, (0, 0))
  screen.blit(odpocet1, (239,237))
  pygame.display.update()
  time.sleep(1)

def answersbuttons():
  if pos[0] > 10 and pos[0] < 10 + 450: #back button i guess
    if pos[1] > 160 and pos[1] < 160 + 13:
      #print("OnButton")
      screen.blit(downline1, (10,180))
      if event.type == pygame.MOUSEBUTTONDOWN:
        playbuttonSound.play()
        return 1
        print("clickedback")
    else:
      #print("OutOfButton")
      screen.blit(downline0, (10,180))
  else:
    #print("OutOfButton")
    screen.blit(downline0, (10,180))

def linuxtux():
  global dataachievement2
  global counttux
  global pointed
  if pos[0] > 0 and pos[0] < 20: #easteregg
    if pos[1] > 450 and pos[1] < 500:
      #print("OnButton")
      if counttux >= 20 and counttux < 25:
        screen.blit(linuxpicture, (-40,450))
        screen.blit(bubbletux2, (35,380))
      elif counttux >= 25:
        if dataachievement2 == False:
          f = open(gamefilepath, "a") # write down player completed achievement
          if f.mode == "a":
            f.write('achievement2 == True')
            print("Writing")
            print(datafile)
            dataachievement2 = True
          f.close()
        time.sleep(4)
        pygame.quit()
      else:
        screen.blit(bubbletux, (-10,390))
        screen.blit(linuxpicture, (-40,450))
      if pointed == False:
        counttux = counttux + 1
        pointed = True
    else:
      #print("OutOfButton")
      screen.blit(linuxpicture, (-40,450))
      pointed = False
  else:
    #print("OutOfButton")
    screen.blit(linuxpicture, (-40,450))
    pointed = False

def cursor():
  xcur = pos[0]
  ycur = pos[1]
  if xcur > 500 or xcur < 0:
    xcur = 0
  if ycur > 500 or ycur < 0:
    ycur = 0
  screen.blit(cursor2img, (xcur, ycur))

def heartsdraw():
  global zivoty
  if zivoty == 1:
    screen.blit(heart, (310, 20))
  if zivoty == 2:
    screen.blit(heart, (310, 20))
    screen.blit(heart, (340, 20))
  if zivoty == 3:
    screen.blit(heart, (310, 20))
    screen.blit(heart, (340, 20))
    screen.blit(heart, (370, 20))

#//////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////
#Pokud tohle ctes tak se mi hrabes v codu a to se mi nelibi. Takze sup sup pric tohle neni nic pro tebe.


# my_big_font.render(screen, 'Hello World!', (20, 40))

def level1(): #lvl 1
  odpocet()
  global muted
  global exitedlvl
  global Scorelvl1
  global zivoty
  answering = True
  wasdead = False
  timestart = time.time()
  right = "A"
  while answering:
    
    for event in pygame.event.get():
      pos = pygame.mouse.get_pos()
    if event.type == pygame.QUIT:
      pygame.quit()

    screen.blit(bg1_img, (0, 0))
    screen.blit(question1, (10, 50))

    if pos[0] > 10 and pos[0] < 10 + 450: # A
      if pos[1] > 104 and pos[1] < 114 + 39:
        #print("OnButton")
        screen.blit(downline1, (10,160))
        if event.type == pygame.MOUSEBUTTONDOWN:
          playbuttonSound.play()
          print("A")
          answer = "A"
          answering = False
          time.sleep(0.2)
    
    if pos[0] > 10 and pos[0] < 10 + 450: # B
      if pos[1] > 165 and pos[1] < 175 + 13:
        #print("OnButton")
        screen.blit(downline1, (10,195))
        if event.type == pygame.MOUSEBUTTONDOWN:
          playbuttonSound.play()
          print("B")
          answer = "B"
          answering = False
          time.sleep(0.2)

    if pos[0] > 10 and pos[0] < 10 + 450: # C
      if pos[1] > 200 and pos[1] < 210 + 13:
        #print("OnButton")
        screen.blit(downline1, (10,230))
        if event.type == pygame.MOUSEBUTTONDOWN:
          playbuttonSound.play()
          print("C")
          answer = "C"
          answering = False
          time.sleep(0.2)

    screen.blit(cursor2img, (pos[0], pos[1]))

    pygame.display.update()
    timeend = time.time()
    timeneeded = timeend - timestart
    if timeneeded > 15:
      answering = False
      dead = True
      wasdead = True
      pepaisdead.play()
      pygame.mixer.music.stop()
      
      while dead == True:

        for event in pygame.event.get():
          pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
          pygame.quit()

        screen.blit(bg1_img, (0, 0))
        screen.blit(pepadeadimg, (181, 20))

        if pos[0] > 10 and pos[0] < 10 + 39: #back button i guess
          if pos[1] > 10 and pos[1] < 10 + 13:
            #print("OnButton")
            screen.blit(backbutton1, (10,10))
            if event.type == pygame.MOUSEBUTTONDOWN:
              playbuttonSound.play()
              dead = False
              time.sleep(0.2)
          else:
            #print("OutOfButton")
            screen.blit(backbutton0, (10,10))
        else:
          #print("OutOfButton")
          screen.blit(backbutton0, (10,10))

        screen.blit(cursor2img, (pos[0], pos[1]))
        pygame.display.update()
      pygame.mixer.music.play(-1)
      zivoty = zivoty - 1
  if wasdead == False:
    if answer == right:
      print("Right Answer")
      Scorelvl1 = (100 / timeneeded) * 100
      return True
    else:
      print("Wrong Answer")
      dead = True
      pepaisdead.play()
      pygame.mixer.music.stop()
      while dead == True:

        for event in pygame.event.get():
          pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
          pygame.quit()

        screen.blit(bg1_img, (0, 0))
        screen.blit(pepadeadimg, (181, 20))

        if pos[0] > 10 and pos[0] < 10 + 39: #back button i guess
          if pos[1] > 10 and pos[1] < 10 + 13:
            #print("OnButton")
            screen.blit(backbutton1, (10,10))
            if event.type == pygame.MOUSEBUTTONDOWN:
              playbuttonSound.play()
              dead = False
              time.sleep(0.2)
          else:
            #print("OutOfButton")
            screen.blit(backbutton0, (10,10))
        else:
          #print("OutOfButton")
          screen.blit(backbutton0, (10,10))

        screen.blit(cursor2img, (pos[0], pos[1]))
        pygame.display.update()
      if muted == False:
        pygame.mixer.music.play(-1)
      zivoty = zivoty - 1
      menu = True
      return False
  exitedlvl = True

time.sleep(0.2)

def level2(): #lvl 2
  odpocet()
  global muted
  global exitedlvl
  global Scorelvl2
  global zivoty
  answering = True
  wasdead = False
  timestart = time.time()
  right = "A"
  while answering:
    
    for event in pygame.event.get():
      pos = pygame.mouse.get_pos()
    if event.type == pygame.QUIT:
      pygame.quit()

    screen.blit(bg1_img, (0, 0))
    screen.blit(question2, (10, 50))

    if pos[0] > 10 and pos[0] < 10 + 450: # A
      if pos[1] > 87 and pos[1] < 97 + 25:
        #print("OnButton")
        screen.blit(downline1, (10,117))
        if event.type == pygame.MOUSEBUTTONDOWN:
          playbuttonSound.play()
          print("A")
          answer = "A"
          answering = False
          time.sleep(0.2)
    
    if pos[0] > 10 and pos[0] < 10 + 450: # B
      if pos[1] > 121 and pos[1] < 121 + 29:
        #print("OnButton")
        screen.blit(downline1, (10,151))
        if event.type == pygame.MOUSEBUTTONDOWN:
          playbuttonSound.play()
          print("B")
          answer = "B"
          answering = False
          time.sleep(0.2)

    if pos[0] > 10 and pos[0] < 10 + 450: # C
      if pos[1] > 155 and pos[1] < 155 + 29:
        #print("OnButton")
        screen.blit(downline1, (10,185))
        if event.type == pygame.MOUSEBUTTONDOWN:
          playbuttonSound.play()
          print("C")
          answer = "C"
          answering = False
          time.sleep(0.2)

    screen.blit(cursor2img, (pos[0], pos[1]))

    pygame.display.update()
    timeend = time.time()
    timeneeded = timeend - timestart
    if timeneeded > 15:
      answering = False
      dead = True
      wasdead = True
      pepaisdead.play()
      pygame.mixer.music.stop()
      while dead == True:

        for event in pygame.event.get():
          pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
          pygame.quit()

        screen.blit(bg1_img, (0, 0))
        screen.blit(pepadeadimg, (181, 20))

        if pos[0] > 10 and pos[0] < 10 + 39: #back button i guess
          if pos[1] > 10 and pos[1] < 10 + 13:
            #print("OnButton")
            screen.blit(backbutton1, (10,10))
            if event.type == pygame.MOUSEBUTTONDOWN:
              playbuttonSound.play()
              dead = False
              time.sleep(0.2)
          else:
            #print("OutOfButton")
            screen.blit(backbutton0, (10,10))
        else:
          #print("OutOfButton")
          screen.blit(backbutton0, (10,10))

        screen.blit(cursor2img, (pos[0], pos[1]))
        pygame.display.update()
      pygame.mixer.music.play(-1)
      zivoty = zivoty - 1
  if wasdead == False:
    if answer == right:
      print("Right Answer")
      Scorelvl2 = (100 / timeneeded) * 100
      return True
    else:
      print("Wrong Answer")
      dead = True
      pepaisdead.play()
      pygame.mixer.music.stop()
      while dead == True:

        for event in pygame.event.get():
          pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
          pygame.quit()

        screen.blit(bg1_img, (0, 0))
        screen.blit(pepadeadimg, (181, 20))

        if pos[0] > 10 and pos[0] < 10 + 39: #back button i guess
          if pos[1] > 10 and pos[1] < 10 + 13:
            #print("OnButton")
            screen.blit(backbutton1, (10,10))
            if event.type == pygame.MOUSEBUTTONDOWN:
              playbuttonSound.play()
              dead = False
              time.sleep(0.2)
          else:
            #print("OutOfButton")
            screen.blit(backbutton0, (10,10))
        else:
          #print("OutOfButton")
          screen.blit(backbutton0, (10,10))

        screen.blit(cursor2img, (pos[0], pos[1]))
        pygame.display.update()
      if muted == False:
        pygame.mixer.music.play(-1)
      zivoty = zivoty - 1
      menu = True
      return False
  exitedlvl = True

time.sleep(0.2)
def level3():
  odpocet()
  global muted
  global exitedlvl
  global Scorelvl3
  global zivoty
  answering = True
  wasdead = False
  timestart = time.time()
  right = "B"
  while answering:
    
    for event in pygame.event.get():
      pos = pygame.mouse.get_pos()
    if event.type == pygame.QUIT:
      pygame.quit()

    screen.blit(bg1_img, (0, 0))
    screen.blit(question3, (10, 42.5))

    if pos[0] > 10 and pos[0] < 10 + 450: # A
      if pos[1] > 87 and pos[1] < 97 + 25:
        #print("OnButton")
        screen.blit(downline1, (10,117))
        if event.type == pygame.MOUSEBUTTONDOWN:
          playbuttonSound.play()
          print("A")
          answer = "A"
          answering = False
          time.sleep(0.2)
    
    if pos[0] > 10 and pos[0] < 10 + 450: # B
      if pos[1] > 121 and pos[1] < 121 + 29:
        #print("OnButton")
        screen.blit(downline1, (10,151))
        if event.type == pygame.MOUSEBUTTONDOWN:
          playbuttonSound.play()
          print("B")
          answer = "B"
          answering = False
          time.sleep(0.2)

    if pos[0] > 10 and pos[0] < 10 + 450: # C
      if pos[1] > 155 and pos[1] < 155 + 29:
        #print("OnButton")
        screen.blit(downline1, (10,185))
        if event.type == pygame.MOUSEBUTTONDOWN:
          playbuttonSound.play()
          print("C")
          answer = "C"
          answering = False
          time.sleep(0.2)

    screen.blit(cursor2img, (pos[0], pos[1]))

    pygame.display.update()
    timeend = time.time()
    timeneeded = timeend - timestart
    if timeneeded > 15:
      answering = False
      dead = True
      wasdead = True
      pepaisdead.play()
      pygame.mixer.music.stop()
      while dead == True:

        for event in pygame.event.get():
          pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
          pygame.quit()

        screen.blit(bg1_img, (0, 0))
        screen.blit(pepadeadimg, (181, 20))

        if pos[0] > 10 and pos[0] < 10 + 39: #back button i guess
          if pos[1] > 10 and pos[1] < 10 + 13:
            #print("OnButton")
            screen.blit(backbutton1, (10,10))
            if event.type == pygame.MOUSEBUTTONDOWN:
              playbuttonSound.play()
              dead = False
              time.sleep(0.2)
          else:
            #print("OutOfButton")
            screen.blit(backbutton0, (10,10))
        else:
          #print("OutOfButton")
          screen.blit(backbutton0, (10,10))

        screen.blit(cursor2img, (pos[0], pos[1]))
        pygame.display.update()
      pygame.mixer.music.play(-1)
      zivoty = zivoty - 1
  if wasdead == False:
    if answer == right:
      print("Right Answer")
      Scorelvl3 = (100 / timeneeded) * 100
      return True
    else:
      print("Wrong Answer")
      dead = True
      pepaisdead.play()
      pygame.mixer.music.stop()
      while dead == True:

        for event in pygame.event.get():
          pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
          pygame.quit()

        screen.blit(bg1_img, (0, 0))
        screen.blit(pepadeadimg, (181, 20))

        if pos[0] > 10 and pos[0] < 10 + 39: #back button i guess
          if pos[1] > 10 and pos[1] < 10 + 13:
            #print("OnButton")
            screen.blit(backbutton1, (10,10))
            if event.type == pygame.MOUSEBUTTONDOWN:
              playbuttonSound.play()
              dead = False
              time.sleep(0.2)
          else:
            #print("OutOfButton")
            screen.blit(backbutton0, (10,10))
        else:
          #print("OutOfButton")
          screen.blit(backbutton0, (10,10))

        screen.blit(cursor2img, (pos[0], pos[1]))
        pygame.display.update()
      if muted == False:
        pygame.mixer.music.play(-1)
      zivoty = zivoty - 1
      menu = True
      return False
  exitedlvl = True
def level4():
  odpocet()
  global muted
  global exitedlvl
  global Scorelvl4
  global zivoty
  answering = True
  wasdead = False
  timestart = time.time()
  right = "C"
  while answering:
    
    for event in pygame.event.get():
      pos = pygame.mouse.get_pos()
    if event.type == pygame.QUIT:
      pygame.quit()

    screen.blit(bg1_img, (0, 0))
    screen.blit(question4, (10, 40))

    if pos[0] > 10 and pos[0] < 10 + 450: # A
      if pos[1] > 87 and pos[1] < 97 + 25:
        #print("OnButton")
        screen.blit(downline1, (10,117))
        if event.type == pygame.MOUSEBUTTONDOWN:
          playbuttonSound.play()
          print("A")
          answer = "A"
          answering = False
          time.sleep(0.2)
    
    if pos[0] > 10 and pos[0] < 10 + 450: # B
      if pos[1] > 121 and pos[1] < 121 + 29:
        #print("OnButton")
        screen.blit(downline1, (10,151))
        if event.type == pygame.MOUSEBUTTONDOWN:
          playbuttonSound.play()
          print("B")
          answer = "B"
          answering = False
          time.sleep(0.2)

    if pos[0] > 10 and pos[0] < 10 + 450: # C
      if pos[1] > 155 and pos[1] < 155 + 29:
        #print("OnButton")
        screen.blit(downline1, (10,185))
        if event.type == pygame.MOUSEBUTTONDOWN:
          playbuttonSound.play()
          print("C")
          answer = "C"
          answering = False
          time.sleep(0.2)

    screen.blit(cursor2img, (pos[0], pos[1]))

    pygame.display.update()
    timeend = time.time()
    timeneeded = timeend - timestart
    if timeneeded > 15:
      answering = False
      dead = True
      wasdead = True
      pepaisdead.play()
      pygame.mixer.music.stop()
      while dead == True:

        for event in pygame.event.get():
          pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
          pygame.quit()

        screen.blit(bg1_img, (0, 0))
        screen.blit(pepadeadimg, (181, 20))

        if pos[0] > 10 and pos[0] < 10 + 39: #back button i guess
          if pos[1] > 10 and pos[1] < 10 + 13:
            #print("OnButton")
            screen.blit(backbutton1, (10,10))
            if event.type == pygame.MOUSEBUTTONDOWN:
              playbuttonSound.play()
              dead = False
              time.sleep(0.2)
          else:
            #print("OutOfButton")
            screen.blit(backbutton0, (10,10))
        else:
          #print("OutOfButton")
          screen.blit(backbutton0, (10,10))

        screen.blit(cursor2img, (pos[0], pos[1]))
        pygame.display.update()
      pygame.mixer.music.play(-1)
      zivoty = zivoty - 1
  if wasdead == False:
    if answer == right:
      print("Right Answer")
      Scorelvl4 = (100 / timeneeded) * 100
      return True
    else:
      print("Wrong Answer")
      dead = True
      pepaisdead.play()
      pygame.mixer.music.stop()
      while dead == True:

        for event in pygame.event.get():
          pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
          pygame.quit()

        screen.blit(bg1_img, (0, 0))
        screen.blit(pepadeadimg, (181, 20))

        if pos[0] > 10 and pos[0] < 10 + 39: #back button i guess
          if pos[1] > 10 and pos[1] < 10 + 13:
            #print("OnButton")
            screen.blit(backbutton1, (10,10))
            if event.type == pygame.MOUSEBUTTONDOWN:
              playbuttonSound.play()
              dead = False
              time.sleep(0.2)
          else:
            #print("OutOfButton")
            screen.blit(backbutton0, (10,10))
        else:
          #print("OutOfButton")
          screen.blit(backbutton0, (10,10))

        screen.blit(cursor2img, (pos[0], pos[1]))
        pygame.display.update()
      if muted == False:
        pygame.mixer.music.play(-1)
      zivoty = zivoty - 1
      menu = True
      return False
  exitedlvl = True
def level5():
  odpocet()
  global muted
  global exitedlvl
  global Scorelvl5
  global zivoty
  answering = True
  wasdead = False
  timestart = time.time()
  right = "B"
  while answering:
     
    for event in pygame.event.get():
      pos = pygame.mouse.get_pos()
    if event.type == pygame.QUIT:
      pygame.quit()

    screen.blit(bg1_img, (0, 0))
    screen.blit(question5, (10, 40))

    if pos[0] > 10 and pos[0] < 10 + 450: # A
      if pos[1] > 87 and pos[1] < 97 + 29:
        #print("OnButton")
        screen.blit(downline1, (10, 117))
        if event.type == pygame.MOUSEBUTTONDOWN:
          playbuttonSound.play()
          print("A")
          answer = "A"
          answering = False
          time.sleep(0.2)
    
    if pos[0] > 10 and pos[0] < 10 + 450: # B
      if pos[1] > 121 and pos[1] < 121 + 29:
        #print("OnButton")
        screen.blit(downline1, (10,151))
        if event.type == pygame.MOUSEBUTTONDOWN:
          playbuttonSound.play()
          print("B")
          answer = "B"
          answering = False
          time.sleep(0.2)

    if pos[0] > 10 and pos[0] < 10 + 450: # C
      if pos[1] > 155 and pos[1] < 155 + 68:
        #print("OnButton")
        screen.blit(downline1, (10, 220))
        if event.type == pygame.MOUSEBUTTONDOWN:
          playbuttonSound.play()
          print("C")
          answer = "C"
          answering = False
          time.sleep(0.2)

    screen.blit(cursor2img, (pos[0], pos[1]))

    pygame.display.update()
    timeend = time.time()
    timeneeded = timeend - timestart
    if timeneeded > 15:
      answering = False
      dead = True
      wasdead = True
      while dead == True:

        for event in pygame.event.get():
          pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
          pygame.quit()

        screen.blit(bg1_img, (0, 0))
        screen.blit(pepadeadimg, (181, 20))

        if pos[0] > 10 and pos[0] < 10 + 39: #back button i guess
          if pos[1] > 10 and pos[1] < 10 + 13:
            #print("OnButton")
            screen.blit(backbutton1, (10,10))
            if event.type == pygame.MOUSEBUTTONDOWN:
              playbuttonSound.play()
              dead = False
              time.sleep(0.2)
          else:
            #print("OutOfButton")
            screen.blit(backbutton0, (10,10))
        else:
          #print("OutOfButton")
          screen.blit(backbutton0, (10,10))

        screen.blit(cursor2img, (pos[0], pos[1]))
        pygame.display.update()
      pygame.mixer.music.play(-1)
      zivoty = zivoty - 1
  if wasdead == False:
    if answer == right:
      print("Right Answer")
      Scorelvl5 = (100 / timeneeded) * 100
      return True
    else:
      print("Wrong Answer")
      dead = True
      pepaisdead.play()
      pygame.mixer.music.stop()
      while dead == True:

        for event in pygame.event.get():
          pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
          pygame.quit()

        screen.blit(bg1_img, (0, 0))
        screen.blit(pepadeadimg, (181, 20))

        if pos[0] > 10 and pos[0] < 10 + 39: #back button i guess
          if pos[1] > 10 and pos[1] < 10 + 13:
            #print("OnButton")
            screen.blit(backbutton1, (10,10))
            if event.type == pygame.MOUSEBUTTONDOWN:
              playbuttonSound.play()
              dead = False
              time.sleep(0.2)
          else:
            #print("OutOfButton")
            screen.blit(backbutton0, (10,10))
        else:
          #print("OutOfButton")
          screen.blit(backbutton0, (10,10))

        screen.blit(cursor2img, (pos[0], pos[1]))
        pygame.display.update()
      if muted == False:
        pygame.mixer.music.play(-1)
      zivoty = zivoty - 1
      menu = True
      return False
  exitedlvl = True
def level6():
  odpocet()
  global muted
  global exitedlvl
  global Scorelvl6
  global zivoty
  answering = True
  wasdead = False
  timestart = time.time()
  right = "B"
  while answering:
     
    for event in pygame.event.get():
      pos = pygame.mouse.get_pos()
    if event.type == pygame.QUIT:
      pygame.quit()

    screen.blit(bg1_img, (0, 0))
    screen.blit(question6, (10, 40))

    if pos[0] > 10 and pos[0] < 10 + 450: # A
      if pos[1] > 87 and pos[1] < 97 + 25:
        #print("OnButton")
        screen.blit(downline1, (10, 117))
        if event.type == pygame.MOUSEBUTTONDOWN:
          playbuttonSound.play()
          print("A")
          answer = "A"
          answering = False
          time.sleep(0.2)
    
    if pos[0] > 10 and pos[0] < 10 + 450: # B
      if pos[1] > 121 and pos[1] < 121 + 29:
        #print("OnButton")
        screen.blit(downline1, (10,151))
        if event.type == pygame.MOUSEBUTTONDOWN:
          playbuttonSound.play()
          print("B")
          answer = "B"
          answering = False
          time.sleep(0.2)

    if pos[0] > 10 and pos[0] < 10 + 450: # C
      if pos[1] > 155 and pos[1] < 155 + 29:
        #print("OnButton")
        screen.blit(downline1, (10,185))
        if event.type == pygame.MOUSEBUTTONDOWN:
          playbuttonSound.play()
          print("C")
          answer = "C"
          answering = False
          time.sleep(0.2)

    screen.blit(cursor2img, (pos[0], pos[1]))

    pygame.display.update()
    timeend = time.time()
    timeneeded = timeend - timestart
    if timeneeded > 15:
      answering = False
      dead = True
      wasdead = True
      pepaisdead.play()
      pygame.mixer.music.stop()
      while dead == True:

        for event in pygame.event.get():
          pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
          pygame.quit()

        screen.blit(bg1_img, (0, 0))
        screen.blit(pepadeadimg, (181, 20))

        if pos[0] > 10 and pos[0] < 10 + 39: #back button i guess
          if pos[1] > 10 and pos[1] < 10 + 13:
            #print("OnButton")
            screen.blit(backbutton1, (10,10))
            if event.type == pygame.MOUSEBUTTONDOWN:
              playbuttonSound.play()
              dead = False
              time.sleep(0.2)
          else:
            #print("OutOfButton")
            screen.blit(backbutton0, (10,10))
        else:
          #print("OutOfButton")
          screen.blit(backbutton0, (10,10))

        screen.blit(cursor2img, (pos[0], pos[1]))
        pygame.display.update()
      pygame.mixer.music.play(-1)
      zivoty = zivoty - 1
  if wasdead == False:
    if answer == right:
      print("Right Answer")
      Scorelvl6 = (100 / timeneeded) * 100
      return True
    else:
      print("Wrong Answer")
      dead = True
      pepaisdead.play()
      pygame.mixer.music.stop()
      while dead == True:

        for event in pygame.event.get():
          pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
          pygame.quit()

        screen.blit(bg1_img, (0, 0))
        screen.blit(pepadeadimg, (181, 20))

        if pos[0] > 10 and pos[0] < 10 + 39: #back button i guess
          if pos[1] > 10 and pos[1] < 10 + 13:
            #print("OnButton")
            screen.blit(backbutton1, (10,10))
            if event.type == pygame.MOUSEBUTTONDOWN:
              playbuttonSound.play()
              dead = False
              time.sleep(0.2)
          else:
            #print("OutOfButton")
            screen.blit(backbutton0, (10,10))
        else:
          #print("OutOfButton")
          screen.blit(backbutton0, (10,10))

        screen.blit(cursor2img, (pos[0], pos[1]))
        pygame.display.update()
      if muted == False:
        pygame.mixer.music.play(-1)
      zivoty = zivoty - 1
      menu = True
      return False
  exitedlvl = True
def level7():
  odpocet()
  global muted
  global exitedlvl
  global Scorelvl7
  global zivoty
  answering = True
  wasdead = False
  timestart = time.time()
  right = "B"
  while answering:
     
    for event in pygame.event.get():
      pos = pygame.mouse.get_pos()
    if event.type == pygame.QUIT:
      pygame.quit()

    screen.blit(bg1_img, (0, 0))
    screen.blit(question7, (10, 40))

    if pos[0] > 10 and pos[0] < 10 + 450: # A
      if pos[1] > 88 and pos[1] < 98 + 25:
        #print("OnButton")
        screen.blit(downline1, (10,118))
        if event.type == pygame.MOUSEBUTTONDOWN:
          playbuttonSound.play()
          print("A")
          answer = "A"
          answering = False
          time.sleep(0.2)
    
    if pos[0] > 10 and pos[0] < 10 + 450: # B
      if pos[1] > 124 and pos[1] < 124 + 29:
        #print("OnButton")
        screen.blit(downline1, (10,154))
        if event.type == pygame.MOUSEBUTTONDOWN:
          playbuttonSound.play()
          print("B")
          answer = "B"
          answering = False
          time.sleep(0.2)

    if pos[0] > 10 and pos[0] < 10 + 450: # C
      if pos[1] > 170 and pos[1] < 160 + 29:
        #print("OnButton")
        screen.blit(downline1, (10,190))
        if event.type == pygame.MOUSEBUTTONDOWN:
          playbuttonSound.play()
          print("C")
          answer = "C"
          answering = False
          time.sleep(0.2)

    screen.blit(cursor2img, (pos[0], pos[1]))

    pygame.display.update()
    timeend = time.time()
    timeneeded = timeend - timestart
    if timeneeded > 10:
      answering = False
      dead = True
      wasdead = True
      pepaisdead.play()
      pygame.mixer.music.stop()
      while dead == True:

        for event in pygame.event.get():
          pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
          pygame.quit()

        screen.blit(bg1_img, (0, 0))
        screen.blit(pepadeadimg, (181, 20))

        if pos[0] > 10 and pos[0] < 10 + 39: #back button i guess
          if pos[1] > 10 and pos[1] < 10 + 13:
            #print("OnButton")
            screen.blit(backbutton1, (10,10))
            if event.type == pygame.MOUSEBUTTONDOWN:
              playbuttonSound.play()
              dead = False
              time.sleep(0.2)
          else:
            #print("OutOfButton")
            screen.blit(backbutton0, (10,10))
        else:
          #print("OutOfButton")
          screen.blit(backbutton0, (10,10))

        screen.blit(cursor2img, (pos[0], pos[1]))
        pygame.display.update()
      pygame.mixer.music.play(-1)
      zivoty = zivoty - 1
  if wasdead == False:
    if answer == right:
      print("Right Answer")
      Scorelvl7 = (100 / timeneeded) * 100
      return True
    else:
      print("Wrong Answer")
      dead = True
      pepaisdead.play()
      pygame.mixer.music.stop()
      while dead == True:

        for event in pygame.event.get():
          pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
          pygame.quit()

        screen.blit(bg1_img, (0, 0))
        screen.blit(pepadeadimg, (181, 20))

        if pos[0] > 10 and pos[0] < 10 + 39: #back button i guess
          if pos[1] > 10 and pos[1] < 10 + 13:
            #print("OnButton")
            screen.blit(backbutton1, (10,10))
            if event.type == pygame.MOUSEBUTTONDOWN:
              playbuttonSound.play()
              dead = False
              time.sleep(0.2)
          else:
            #print("OutOfButton")
            screen.blit(backbutton0, (10,10))
        else:
          #print("OutOfButton")
          screen.blit(backbutton0, (10,10))

        screen.blit(cursor2img, (pos[0], pos[1]))
        pygame.display.update()
      if muted == False:
        pygame.mixer.music.play(-1)
      zivoty = zivoty - 1
      menu = True
      return False
  exitedlvl = True
def level8():
  odpocet()
  global muted
  global exitedlvl
  global Scorelvl8
  global zivoty
  global exitedlvl
  answering = True
  wasdead = False
  timestart = time.time()
  right = "B"
  while answering:
    
    for event in pygame.event.get():
      pos = pygame.mouse.get_pos()
    if event.type == pygame.QUIT:
      pygame.quit()

    screen.blit(bg1_img, (0, 0))
    screen.blit(question8, (10, 40))

    if pos[0] > 10 and pos[0] < 10 + 450: # A
      if pos[1] > 82 and pos[1] < 92 + 25:
        #print("OnButton")
        screen.blit(downline1, (10,112))
        if event.type == pygame.MOUSEBUTTONDOWN:
          playbuttonSound.play()
          print("A")
          answer = "A"
          answering = False
          time.sleep(0.2)
    
    if pos[0] > 10 and pos[0] < 10 + 450: # B
      if pos[1] > 119 and pos[1] < 119 + 29:
        #print("OnButton")
        screen.blit(downline1, (10,149))
        if event.type == pygame.MOUSEBUTTONDOWN:
          playbuttonSound.play()
          print("B")
          answer = "B"
          answering = False
          time.sleep(0.2)

    if pos[0] > 10 and pos[0] < 10 + 450: # C
      if pos[1] > 155 and pos[1] < 155 + 29:
        #print("OnButton")
        screen.blit(downline1, (10,185))
        if event.type == pygame.MOUSEBUTTONDOWN:
          playbuttonSound.play()
          print("C")
          answer = "C"
          answering = False
          time.sleep(0.2)

    screen.blit(cursor2img, (pos[0], pos[1]))

    pygame.display.update()
    timeend = time.time()
    timeneeded = timeend - timestart
    if timeneeded > 15:
      answering = False
      dead = True
      wasdead = True
      pepaisdead.play()
      pygame.mixer.music.stop()
      while dead == True:

        for event in pygame.event.get():
          pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
          pygame.quit()

        screen.blit(bg1_img, (0, 0))
        screen.blit(pepadeadimg, (181, 20))

        if pos[0] > 10 and pos[0] < 10 + 39: #back button i guess
          if pos[1] > 10 and pos[1] < 10 + 13:
            #print("OnButton")
            screen.blit(backbutton1, (10,10))
            if event.type == pygame.MOUSEBUTTONDOWN:
              playbuttonSound.play()
              dead = False
              time.sleep(0.2)
          else:
            #print("OutOfButton")
            screen.blit(backbutton0, (10,10))
        else:
          #print("OutOfButton")
          screen.blit(backbutton0, (10,10))

        screen.blit(cursor2img, (pos[0], pos[1]))
        pygame.display.update()
      pygame.mixer.music.play(-1)
      zivoty = zivoty - 1
  if wasdead == False:
    if answer == right:
      print("Right Answer")
      Scorelvl8 = (100 / timeneeded) * 100
      return True
    else:
      print("Wrong Answer")
      dead = True
      pepaisdead.play()
      pygame.mixer.music.stop()
      while dead == True:

        for event in pygame.event.get():
          pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
          pygame.quit()

        screen.blit(bg1_img, (0, 0))
        screen.blit(pepadeadimg, (181, 20))

        if pos[0] > 10 and pos[0] < 10 + 39: #back button i guess
          if pos[1] > 10 and pos[1] < 10 + 13:
            #print("OnButton")
            screen.blit(backbutton1, (10,10))
            if event.type == pygame.MOUSEBUTTONDOWN:
              playbuttonSound.play()
              dead = False
              time.sleep(0.2)
          else:
            #print("OutOfButton")
            screen.blit(backbutton0, (10,10))
        else:
          #print("OutOfButton")
          screen.blit(backbutton0, (10,10))

        screen.blit(cursor2img, (pos[0], pos[1]))
        pygame.display.update()
      if muted == False:
        pygame.mixer.music.play(-1)
      zivoty = zivoty - 1
      menu = True
      return False
  exitedlvl = True
def level9():
  odpocet()
  global muted
  global exitedlvl
  global Scorelvl9
  global zivoty
  answering = True
  wasdead = False
  timestart = time.time()
  right = "B"
  while answering:
    
    for event in pygame.event.get():
      pos = pygame.mouse.get_pos()
    if event.type == pygame.QUIT:
      pygame.quit()

    screen.blit(bg1_img, (0, 0))
    screen.blit(question9, (10, 50))

    if pos[0] > 10 and pos[0] < 10 + 450: # A
      if pos[1] > 87 and pos[1] < 97 + 25:
        #print("OnButton")
        screen.blit(downline1, (10,127))
        if event.type == pygame.MOUSEBUTTONDOWN:
          playbuttonSound.play()
          print("A")
          answer = "A"
          answering = False
          time.sleep(0.2)
    
    if pos[0] > 10 and pos[0] < 10 + 450: # B
      if pos[1] > 121 and pos[1] < 121 + 29:
        #print("OnButton")
        screen.blit(downline1, (10,161))
        if event.type == pygame.MOUSEBUTTONDOWN:
          playbuttonSound.play()
          print("B")
          answer = "B"
          answering = False
          time.sleep(0.2)

    if pos[0] > 10 and pos[0] < 10 + 450: # C
      if pos[1] > 155 and pos[1] < 155 + 29:
        #print("OnButton")
        screen.blit(downline1, (10,195))
        if event.type == pygame.MOUSEBUTTONDOWN:
          playbuttonSound.play()
          print("C")
          answer = "C"
          answering = False
          time.sleep(0.2)

    screen.blit(cursor2img, (pos[0], pos[1]))

    pygame.display.update()
    timeend = time.time()
    timeneeded = timeend - timestart
    if timeneeded > 15:
      answering = False
      dead = True
      wasdead = True
      pepaisdead.play()
      pygame.mixer.music.stop()
      while dead == True:

        for event in pygame.event.get():
          pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
          pygame.quit()

        screen.blit(bg1_img, (0, 0))
        screen.blit(pepadeadimg, (181, 20))

        if pos[0] > 10 and pos[0] < 10 + 39: #back button i guess
          if pos[1] > 10 and pos[1] < 10 + 13:
            #print("OnButton")
            screen.blit(backbutton1, (10,10))
            if event.type == pygame.MOUSEBUTTONDOWN:
              playbuttonSound.play()
              dead = False
              time.sleep(0.2)
          else:
            #print("OutOfButton")
            screen.blit(backbutton0, (10,10))
        else:
          #print("OutOfButton")
          screen.blit(backbutton0, (10,10))

        screen.blit(cursor2img, (pos[0], pos[1]))
        pygame.display.update()
      pygame.mixer.music.play(-1)
      zivoty = zivoty - 1
  if wasdead == False:
    if answer == right:
      print("Right Answer")
      Scorelvl9 = (100 / timeneeded) * 100
      return True
    else:
      print("Wrong Answer")
      dead = True
      pepaisdead.play()
      pygame.mixer.music.stop()
      while dead == True:

        for event in pygame.event.get():
          pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
          pygame.quit()

        screen.blit(bg1_img, (0, 0))
        screen.blit(pepadeadimg, (181, 20))

        if pos[0] > 10 and pos[0] < 10 + 39: #back button i guess
          if pos[1] > 10 and pos[1] < 10 + 13:
            #print("OnButton")
            screen.blit(backbutton1, (10,10))
            if event.type == pygame.MOUSEBUTTONDOWN:
              playbuttonSound.play()
              dead = False
              time.sleep(0.2)
          else:
            #print("OutOfButton")
            screen.blit(backbutton0, (10,10))
        else:
          #print("OutOfButton")
          screen.blit(backbutton0, (10,10))

        screen.blit(cursor2img, (pos[0], pos[1]))
        pygame.display.update()
      if muted == False:
        pygame.mixer.music.play(-1)
      zivoty = zivoty - 1
      menu = True
      return False
  exitedlvl = True

def levelSave():
  global lvl1completed
  global lvl2completed
  global lvl3completed
  global lvl4completed
  global lvl5completed
  global lvl6completed
  global lvl7completed
  global lvl8completed
  global lvl9completed

  f = open(gamefilepath, "a") # write down player completed level or load already completed level
  f2 = open(gamefilepath, "r")

  datafile = f2.read()

  if lvl1completed == True:
    if lvl1completed == True and "level1completed" in datafile:
      print("Alreadysaved")
    else:
      f.write('level1completed')
  elif "level1completed" in datafile:
    lvl1completed = True

  if lvl2completed == True:
    if lvl2completed == True and "level2completed" in datafile:
      print("Alreadysaved")
    else:
      f.write('level2completed')
  elif "level2completed" in datafile:
    lvl2completed = True

  if lvl3completed == True:
    if lvl3completed == True and "level3completed" in datafile:
      print("Alreadysaved")
    else:
      f.write('level3completed')
  elif "level3completed" in datafile:
    lvl3completed = True

  if lvl4completed == True:
    if lvl4completed == True and "level4completed" in datafile:
      print("Alreadysaved")
    else:
      f.write('level4completed')

  elif "level3completed" in datafile:
    lvl3completed = True
  if lvl5completed == True:
    if lvl5completed == True and "level5completed" in datafile:
      print("Alreadysaved")
    else:
      f.write('level5completed')
  elif "level5completed" in datafile:
    lvl5completed = True

  if lvl6completed == True:
    if lvl6completed == True and "level6completed" in datafile:
      print("Alreadysaved")
    else:
      f.write('level6completed')
  elif "level6completed" in datafile:
    lvl6completed = True

  if lvl7completed == True:
    if lvl7completed == True and "level7completed" in datafile:
     print("Alreadysaved")
    else:
     f.write('level7completed')
  elif "level7completed" in datafile:
    lvl7completed = True

  if lvl8completed == True:
    if lvl8completed == True and "level8completed" in datafile:
      print("Alreadysaved")
    else:
     f.write('level8completed')
  elif "level8completed" in datafile:
    lvl8completed = True

  if lvl9completed == True:
    if lvl9completed == True and "level9completed" in datafile:
     print("Alreadysaved")
    else:
      f.write('level9completed')
  elif "level9completed" in datafile:
    lvl9completed = True

  f.close()
  f2.close()

def completedlevelsAct():
  global lvl1completed
  global lvl2completed
  global lvl3completed
  global lvl4completed
  global lvl5completed
  global lvl6completed
  global lvl7completed
  global lvl8completed
  global lvl9completed

  f = open(gamefilepath, "a") # write down player completed level or load already completed level
  f2 = open(gamefilepath, "r")

  datafile = f2.read()

  if "level1completed" in datafile:
    lvl1completed = True
  else:
    lvl1completed = False

  if "level2completed" in datafile:
    lvl2completed = True
  else:
    lvl2completed = False

  if "level3completed" in datafile:
    lvl3completed = True
  else:
    lvl3completed = False

  if "level4completed" in datafile:
    lvl4completed = True
  else:
    lvl4completed = False

  if "level5completed" in datafile:
    lvl5completed = True
  else:
    lvl5completed = False

  if "level6completed" in datafile:
    lvl6completed = True
  else:
    lvl6completed = False

  if "level7completed" in datafile:
    lvl7completed = True
  else:
    lvl7completed = False

  if "level8completed" in datafile:
    lvl8completed = True
  else:
    lvl8completed = False

  if "level9completed" in datafile:
    lvl9completed = True
  else:
    lvl9completed = False

  f.close
  f2.close

def heartsSave():
  global zivoty

  f = open(gamefilepath, "a") # write down player hearts status
  f2 = open(gamefilepath, "r")

  if zivoty == 0 and not "0Hearts" in datafile:
    f.write('0Hearts')
  if zivoty == 1 and not "1Hearts" in datafile:
    f.write('1Hearts')
  if zivoty == 2 and not "2Hearts" in datafile:
    f.write('2Hearts')
  elif not "3Hearts" in datafile:
    f.write('3Hearts')

  f.close()
  f2.close()

def heartsLoad():
  global zivoty

  f = open(gamefilepath, "r+") #datafile operations - hearts
  if f.mode == "r+":
    datafile = f.read()
    print("Reading")
    print(datafile)
    if "0Hearts" in datafile:
      print("0hearts")
      zivoty = 0
    elif "1Hearts" in datafile:
      print("1Heart")
      zivoty = 1
    elif "2Hearts" in datafile:
      print("2Hearts")
      zivoty = 2
    elif "3Hearts" in datafile:
      #nice
      print("3Hearts")
      zivoty = 3
    else:
      zivoty = 3
  f.close()

def achievementsload():
  global achievement1
  global achievement2

  f = open(gamefilepath, "a") # write down player hearts status
  f2 = open(gamefilepath, "r")
  datafile = f2.read()

  if "achievement1 == True" in datafile:
    achievement1 = True
  else:
    achievement1 = False

  if "achievement2 == True" in datafile:
    achievement2 = True
  else:
    achievement2 = False

  f.close()
  f2.close()

#//////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////

levelselection = False
menu = True
clickcredits = False
menurun = True
clickachievementsbutton = False

while menurun:

  if clickcredits == True: #///////////////////////////////////////////////////// CREDITS
    menu = False
    levelselection = False
    achievementslist = False
    for event in pygame.event.get():
      pos = pygame.mouse.get_pos()
      if event.type == pygame.QUIT:
        pygame.quit()

    screen.blit(bg1_img, (0,0))
    screen.blit(names, (121,20))

    linuxtux()

    quitbutton()

    clickedquit = quitbutton()

    pygame.draw.rect(screen, BLACK,(439,469,500,439))
    my_big_font.render(screen, version, (440,470))

    if clickedquit == True: 
      pygame.quit()

    if pos[0] > 10 and pos[0] < 10 + 39: #back button i guess
      if pos[1] > 10 and pos[1] < 10 + 13:
        #print("OnButton")
        screen.blit(backbutton1, (10,10))
        if event.type == pygame.MOUSEBUTTONDOWN:
          playbuttonSound.play()
          clickcredits = False
          menu = True
          print("clickedback")
      else:
        #print("OutOfButton")
        screen.blit(backbutton0, (10,10))
    else:
      #print("OutOfButton")
      screen.blit(backbutton0, (10,10))

    cursor()

    pygame.display.update()

  if clickachievementsbutton == True: #///////////////////////////////////////////////////// ACHIEVEMENTS
    if menu:
      achievementsload()
      time.sleep(0.2)

    levelselection == False
    menu = False
    clickcredits = False

    for event in pygame.event.get():
      pos = pygame.mouse.get_pos()
    if event.type == pygame.QUIT:
      pygame.quit()

    screen.blit(bg1_img, (0, 0))

    if pos[0] > 10 and pos[0] < 10 + 39: # universal back button i guess
      if pos[1] > 10 and pos[1] < 10 + 13:
        #print("OnButton")
        screen.blit(backbutton1, (10,10))
        if event.type == pygame.MOUSEBUTTONDOWN:
          playbuttonSound.play()
          levelselection = False
          menu = True
          print("clickedback")
      else:
        #print("OutOfButton")
        screen.blit(backbutton0, (10,10))
    else:
      #print("OutOfButton")
      screen.blit(backbutton0, (10,10))

    achievementscalc()

    if achievement1 == True:
      screen.blit(achievement1img, (152.2,100))
    else:
      screen.blit(achievement1blackimg, (152.2,100))
    
    if achievement2 == True:
      screen.blit(achievement2img, (152.2,200))
    else:
      screen.blit(achievement2blackimg, (152.2,200))

    cursor()

    pygame.display.update()

  if levelselection == True: #///////////////////////////////////////////////////// LEVELSELECTION
    if menu:
      completedlevelsAct()
      heartsLoad()
      time.sleep(0.2)
    clickcredits = False
    achievementslist = False
    menu = False

    for event in pygame.event.get():
      pos = pygame.mouse.get_pos()
    if event.type == pygame.QUIT:
      pygame.quit()

    screen.blit(bg1_img, (0, 0))

    levelsmenudraw()

    levelselected = levelselect()

    if zivoty >= 1:
      if levelselected == 1:
        lvlselButton.play()
        time.sleep(0.1)
        lvl1completed = level1()
        exitedlvl = True
        #level1()
      elif levelselected == 2:
        lvlselButton.play()
        time.sleep(0.1)
        lvl2completed = level2()
        exitedlvl = True
        #level2()
      elif levelselected == 3:
        lvlselButton.play()
        time.sleep(0.1)
        lvl3completed = level3()
        exitedlvl = True
        #level3()
      elif levelselected == 4:
        lvlselButton.play()
        time.sleep(0.1)
        lvl4completed = level4()
        exitedlvl = True
        #level4()
      elif levelselected == 5:   # level selection
        lvlselButton.play()
        time.sleep(0.1)
        lvl5completed = level5()
        exitedlvl = True
        #level5()
      elif levelselected == 6:
        lvlselButton.play()
        time.sleep(0.1)
        lvl6completed = level6()
        exitedlvl = True
        #level6()
      elif levelselected == 7:
        lvlselButton.play()
        time.sleep(0.1)
        lvl7completed = level7()
        exitedlvl = True
        #level7()
      elif levelselected == 8:
        lvlselButton.play()
        time.sleep(0.1)
        lvl8completed = level8()
        exitedlvl = True
        #level8()
      elif levelselected == 9:
        lvlselButton.play()
        time.sleep(0.1)
        lvl9completed = level9()
        exitedlvl = True
        #level9()

      if exitedlvl:
        levelSave()
        heartsSave()
        heartsLoad()
        exitedlvl = False
        print("Saved")

    heartsdraw()

    checkmarks()

    if pos[0] > 10 and pos[0] < 10 + 39: # universal back button i guess
      if pos[1] > 10 and pos[1] < 10 + 13:
        #print("OnButton")
        screen.blit(backbutton1, (10,10))
        if event.type == pygame.MOUSEBUTTONDOWN:
          playbuttonSound.play()
          levelselection = False
          menu = True
          print("clickedback")
      else:
        #print("OutOfButton")
        screen.blit(backbutton0, (10,10))
    else:
      #print("OutOfButton")
      screen.blit(backbutton0, (10,10))

    cursor()

    pygame.display.update()

  if menu == True: #//////////////////////////////////////////////////////////// MENU
    levelselection = False
    clickcredits = False
    achievementslist = False
    for event in pygame.event.get():
      pos = pygame.mouse.get_pos()
      if event.type == pygame.QUIT:
       pygame.quit() 

    achievementscalc()

    screen.blit(bg1_img, (0, 0))

    screen.blit(logo, (38.5, 100))

    screen.blit(pepa1, (120, 30))

    clickcredits = creditsbutton()

    clickachievementsbutton = clickachievements()

    resetbutton()

    soundbutton()

    levelselection = playbutton()

    clickedquit= quitbutton()

    if clickedquit == True:
      pygame.quit()

    cursor()
    pygame.display.update()

pygame.display.update()
playbuttonSound.play()
time.sleep(0.25)

pygame.quit()