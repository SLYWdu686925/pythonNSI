import turtle 
rtut = 0  
n = 30

rtut=int(input("Quelle valeur pour right turtl"))
n = int(input("Combien de tré voulez vous ?"))


pen = turtle.Turtle() 
  
for i in range(n): 
    
    
    pen.forward(i * 10) 
  
    
    
    pen.right(rtut) 
  
turtle.done() 