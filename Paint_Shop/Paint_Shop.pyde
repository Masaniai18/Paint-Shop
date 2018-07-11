def setup():
    size(600,400)
    fill(155,155,155)           # Fill rectangle colors as gray
    rect(0,299,599,100)         # Bottom rectangle
    rect(0,0,75,298)            # Middle left rectangle
    rect(0,0,599,50)            # Top rectangle
    stroke(random(255),random(255),random(255))
                                #        
    rectS = 20                  #
                                #
    fill(255,255,0)             # Fill rectangle yellow
    noStroke()                  # Remove outline
    rect(65,310,rectS,rectS)    # Set rectangle location and size
    fill(255,100,0)             # Fill rectangle orange
    rect(85,310,rectS,rectS)    # Set rectangle location and size
    fill(155,0,155)             # Fill rectangle purple
    rect(105,310,rectS,rectS)   # Set rectangle location and size
    fill(355,0,255)             # Fill rectangle pink
    rect(125,310,rectS,rectS)   # Set rectangle loccation and size
    fill(0,0,255)               # Fill rectangle blue
    rect(65,330,rectS,rectS)    # Set rectangle location and size
    fill(255,0,0)               # Fill rectangle red
    rect(85,330,rectS,rectS)    # Set rectangle location and size
    fill(0,255,0)               # Fill rectangle green
    rect(105,330,rectS,rectS)   # Set rectangle location and size
    fill(0)                     # Fill rectangle black
    rect(125,330,rectS,rectS)   # Set rectangle location and size
    

    
def draw():
    if mousePressed and mouseX > 120:
        if mousePressed and mouseY < 280:
            line(pmouseX,pmouseY,mouseX,mouseY)
        
def mouseClicked():
    if mouseX > 65 or mouseX < 85:         # Set yellow button location
        if mouseY > 310 or mouseY < 330:  
            stroke(255,100,0) 
    elif mouseX > 85 or mouseX < 105:      # Set orange button location
        if mouseY > 310 or mouseY < 330:   
            stroke(155,0,155) 
    elif mouseX > 105 or mouseX < 125:     # Set purple button location
        if mouseY > 310 or mouseY < 330:   
            stroke(255,255,0) 
    elif mouseX > 125 or mouseX < 145:     # Set pink button location
        if mouseY > 310 or mouseY < 330:   
            stroke(355,0,255)
    elif mouseX > 85 or mouseX < 105:      # Set blue button location
        if mouseY > 330 or mouseY < 310:   
            stroke()
    elif mouseX > 85 or mouseX < 105:      # Set red button location
        if mouseY > 330 or mouseY < 310:   
            stroke()
    elif mouseX > 85 or mouseX < 105:      # Set green button location
        if mouseY > 330 or mouseY < 310:   
            stroke()
    elif mouseX > 85 or mouseX < 105:      # Set black button location
        if mouseY > 330 or mouseY < 310:   
            stroke()
        else:
            stroke(random(255),random(255),random(255))
