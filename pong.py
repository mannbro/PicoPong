from machine import ADC,Pin,I2C
from ssd1306 import SSD1306_I2C
import math, random, time, framebuf

#Constants
DISPLAY_WIDTH=128
DISPLAY_HEIGHT=64
PADDLE_HEIGHT=20

#Pin configurations
controller1=ADC(26)
controller2=ADC(27)
startButton = Pin(22, Pin.IN)
buzzer = Pin(15, Pin.OUT)
buzzer.value(0)

#Screen initialization
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(DISPLAY_WIDTH, DISPLAY_HEIGHT, i2c)

def init():
    mainMenu()

def mainMenu():
    #Prepare Main Menu Screen 
    startScreenBuffer=bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x80\x0f\xfc\x00\x00\x07\xf8\x00\x00\x3f\x80\x00\x00\xfc\x3b\xc7\xf8\x0f\xff\xc0\x00\x3f\xff\x00\x00\xff\xf0\x00\x07\xfe\x20\x6c\x08\x0f\xff\xe0\x00\xff\xff\x80\x01\xff\xf8\x00\x1f\xfe\x40\x10\x08\x0f\xff\xf0\x01\xff\xff\xe0\x03\xff\xfc\x00\x3f\xfe\x20\x11\x08\x0f\xff\xf8\x03\xff\xff\xf0\x07\xff\xfe\x00\x7f\xfe\x20\x92\x08\x0f\xff\xf8\x07\xfe\x3f\xf8\x07\xf0\xfe\x00\xff\xfe\x30\x7c\x10\x0f\xc0\xfc\x0f\xf0\x07\xf8\x07\xe0\x3f\x01\xff\x02\x18\x7c\x30\x0f\xc0\xfc\x0f\xe0\x01\xfc\x07\xc0\x3f\x03\xfc\x00\x0f\xef\xc0\x0f\xc0\x7c\x1f\xc0\x00\xfc\x0f\xc0\x3f\x03\xf8\x00\x08\x82\x60\x0f\xc0\x7c\x1f\x80\x00\x7e\x0f\xc0\x3f\x07\xf0\x00\x11\x82\x30\x0f\xc0\xfc\x1f\x80\x00\x7e\x0f\xc0\x3f\x07\xe0\x00\x13\xc7\x90\x0f\xc0\xf8\x3f\x00\x00\x3e\x0f\xc0\x3f\x07\xe0\x00\x16\x38\xd0\x0f\xc3\xf8\x3f\x00\x00\x3e\x0f\xc0\x3f\x0f\xc0\x00\x38\x10\x78\x0f\xff\xf8\x3f\x00\x00\x3e\x0f\xc0\x3f\x0f\xc0\x00\x48\x10\x2c\x0f\xff\xf0\x3f\x00\x00\x3f\x0f\xc0\x3f\x0f\xc1\xfe\x48\x10\x24\x0f\xff\xe0\x3f\x00\x00\x3e\x0f\xc0\x3f\x0f\xc1\xfe\xc8\x38\x24\x0f\xff\xc0\x3f\x00\x00\x3e\x0f\xc0\x3f\x0f\xc1\xfe\x48\x38\x64\x0f\xff\x00\x1f\x80\x00\x3e\x0f\xc0\x3f\x07\xe1\xfe\x5f\xc7\xe4\x0f\xc0\x00\x1f\x80\x00\x7e\x0f\xc0\x3f\x07\xe1\xfe\x77\x83\x98\x0f\xc0\x00\x1f\xc0\x00\xfe\x0f\xc0\x3f\x07\xf0\x3e\x23\x03\x08\x0f\xc0\x00\x0f\xc0\x01\xfc\x0f\xc0\x3f\x03\xf0\x3e\x21\x02\x08\x0f\xc0\x00\x0f\xf0\x03\xfc\x0f\xc0\x3f\x03\xf8\x3e\x30\x82\x10\x0f\xc0\x00\x07\xfc\x0f\xf8\x0f\xc0\x3f\x01\xfc\x3e\x10\xce\x10\x0f\xc0\x00\x03\xff\xff\xf0\x0f\xc0\x3f\x01\xff\xbe\x0d\xfe\x60\x0f\xc0\x00\x01\xff\xff\xe0\x0f\xc0\x3f\x00\xff\xfe\x07\x83\xc0\x0f\xc0\x00\x00\xff\xff\xc0\x0f\xc0\x3f\x00\x7f\xfe\x01\x83\x00\x0f\xc0\x00\x00\x3f\xff\x80\x0f\xc0\x3f\x00\x3f\xfe\x00\xfc\x00\x0f\xc0\x00\x00\x0f\xfc\x00\x0f\xc0\x3f\x00\x0f\xfe\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
    fb=framebuf.FrameBuffer(startScreenBuffer, 128, 31, framebuf.MONO_HLSB)

    cnt=10
    toggle=False

    #Main Menu Loop
    while True:

        #Blink start message every second
        if(cnt==10):
            cnt=0
            oled.fill(0)
            
            #Display logo
            oled.blit(fb, 0, 10)
            if(toggle):
                oled.text("PRESS START", 20, 53)
            oled.show()
            toggle=not toggle

        cnt+=1

        #If pressed, start the game
        if startButton.value()==True:
            startGame()
            
        time.sleep_ms(100)

def startGame():
    global player1
    global player2
    
    #Initialize player objects
    player1={"controller": controller1, "paddlePos": 0, "score": 0, "playerNumber": 1}
    player2={"controller": controller2, "paddlePos": 0, "score": 0, "playerNumber": 2}

    #Initialize the ball
    initBall()
    
    #Start the game
    gameLoop()

def initBall():
    global ball

    #Initialize the ball at beginning of game and after scoring
    ball={"xPos": int(DISPLAY_WIDTH/2),"yPos": int(DISPLAY_HEIGHT/2),"xDir": 1 if random.random()>0.5 else -1,"yDir": random.random()*4-2}

def paddleCollition(playerNo):
    #Define player and scorer
    if playerNo==1:
        player=player1
        scorer=player2
    else:
        player=player2
        scorer=player1

    #Collition with paddle?
    if ball["yPos"]>=player["paddlePos"] and ball["yPos"]<=player["paddlePos"]+PADDLE_HEIGHT:

        #Bounce back (reverse x direction of the ball)
        ball["xDir"]=0-ball["xDir"]
        
        #Adjust the y direction based on where the ball hits the paddle
        #The further to the edge, the bigger change of direction
        yDirModifier=(ball["yPos"]-(PADDLE_HEIGHT/2)-player["paddlePos"])/5
        ball["yDir"]=ball["yDir"]+yDirModifier
        return True
    else:
        #SCORE!!!
        scorer["score"]+=1

        #Game over?
        if scorer["score"]==9:
            #Show GAME OVER screen
            oled.fill(0)
            
            oled.text("GAME OVER!", 24, 12)
            
            oled.text("PLAYER "+str(scorer["playerNumber"])+" WINS!", 8, 28)
            
            oled.text(str(player1["score"]), 53, 44)
            oled.text("-", 63, 44)
            oled.text(str(player2["score"]), 73, 44)
            
            oled.show()
            
            #Wait 3 seconds
            time.sleep(3)
            
            #Reset the game
            mainMenu()
        else:
            #Show SCORE screen
            oled.fill(0)
            
            oled.text("PLAYER "+str(scorer["playerNumber"])+" SCORES!", 0, 20)
            
            oled.text(str(player1["score"]), 53, 36)
            oled.text("-", 63, 36)
            oled.text(str(player2["score"]), 73, 36)
            
            oled.show()
            
            #Wait 1 second
            time.sleep(1)
            
            #Reset the ball and resume the game
            initBall()
        return False

def gameLoop():
    while True:
        #Read Potentiometer positions
        player1["paddlePos"]=int((player1["controller"].read_u16()/1024)-(PADDLE_HEIGHT/2))
        player2["paddlePos"]=int((player2["controller"].read_u16()/1024)-(PADDLE_HEIGHT/2))

        buzz=False

        #If ball at left edge
        if ball["xPos"]<1:
            #Check if collition with Player 1 paddle
            if paddleCollition(1)==True:
                buzz=True
        #If ball at right edge
        if ball["xPos"]>DISPLAY_WIDTH-1:
            #Check if collition with Player 2 paddle
            if paddleCollition(2)==True:
                buzz=True
    
        #Bounce (reverse y direction) if reaching top or bottom
        if ball["yPos"]>DISPLAY_HEIGHT-1 or ball["yPos"]<1:
            ball["yDir"]=0-ball["yDir"]
            buzz=True

        #Update ball position with current direction
        ball["xPos"]+=ball["xDir"]
        ball["yPos"]+=ball["yDir"]
        
        
        if buzz==True:
            buzzer.value(1)
        #Reset OLED
        oled.fill(0)
        
        #Draw top and bottom edges
        oled.hline(0, 0, DISPLAY_WIDTH, 1)
        oled.hline(0, DISPLAY_HEIGHT-1, DISPLAY_WIDTH, 1)
        
        #Draw Current Scores
        oled.text(str(player1["score"]), 53, 3)
        oled.text("-", 63, 3)
        oled.text(str(player2["score"]), 73, 3)

        #Draw ball
        oled.pixel(int(ball["xPos"]),int(ball["yPos"]),1)
        
        #Draw paddles
        oled.vline(0, player1["paddlePos"], PADDLE_HEIGHT, 1)
        oled.vline(127, player2["paddlePos"], PADDLE_HEIGHT, 1)

        #Display everything that's been drawn
        oled.show()
        buzzer.value(0)
#Initialize
init()
