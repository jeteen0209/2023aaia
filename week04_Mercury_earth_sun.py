def setup():
    size(500,500)
    background(0)
    
def draw():
    background(0)
    for i in range(frameCount):
        a, a2 = i/36.0, i/36.0*365/88
        stroke(255)
        line(250+200*cos(a), 250+200*sin(a), 250+79*cos(a2), 250+79*sin(a2))
    
    fill(255, 33, 33)
    ellipse(250,250, 80,80) 
    a, a2 = frameCount/36.0, frameCount/36.0*365/88
    
    fill(64, 85, 211)
    ellipse(250+200*cos(a), 250+200*sin(a), 10, 10)
    
    fill(252, 253, 255)
    ellipse(250+79*cos(a2), 250+79*sin(a2), 10, 10) 