# implementation of card game - Memory

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random
global guesses

# helper function to initialize globals
def init():
    global turn, paired, exposed, numbers, turned1, turned2, turned3, guesses
    turn = 0
    guesses = 0
    turned1 = 17
    turned2 = 17
    turned3 = 17
    paired = []
    exposed = []
    numbers = []
    for i in range(16):
        exposed.append(False)
        numbers.append(i % 8)
        paired.append(False)
    random.shuffle(numbers)
        
# define event handlers
def mouseclick(pos):
    global turn, turned1, turned2, turned3, exposed, guesses
    x = 0
    a = 0
    for test_pos in range(16):
        x = test_pos * 50
        a += 10
        if exposed[test_pos] == False:
            check = x + 10 + a
            if pos[0] > check and pos[0] <= check+50:
                if pos[1] < 110 and pos[1] > 10:
                   if turn <= 2:
                        turn += 1
                        exposed[test_pos] = True
                        if turn == 2:
                            turned2 = test_pos
                            guesses += 1
                        elif turn == 1:
                            turned1 = test_pos
                        elif turn == 3:
                            turned3 = test_pos
    l.set_text("Moves = " + str(guesses))   
    
# cards are logically 50x100 pixels in size
def draw(canvas):
    global exposed, turn, turned1, turned2, turned3
    x = 0
    a = 0
    for i in range(16):
       x = i * 50
       a += 10
       if exposed[i]== False and paired[i] == False:
          canvas.draw_polyline([(10 + x + a, 10),
                                (10 + x + a, 110),
                                (60 + x + a, 110),
                                (60 + x + a,10),
                                (10 + x + a,10)], 6, "Red")
       elif exposed[i] == True and paired[i] == False:
          canvas.draw_text(str(numbers[i]), (25 + x  + a, 60), 40, "Red")
          if turn == 3:
              if paired[turned2] == False:
                    exposed[turned2] = False
                    exposed[turned1] = False
                    exposed[turned3] = True
                    turn = 1
                    turned1 = turned3
                    turned3 = 18
          elif turn == 2:
                if numbers[turned2] == numbers[turned1]:
                    paired[turned2] = True
                    paired[turned1] = True
                    print "Found the pair!!!"
                    turn = 0
                    turned1 = 17
                    turned2 = 18
                    
       elif exposed[i] == True and paired[i] == True:
          canvas.draw_text(str(numbers[i]), (25 + x + a, 60), 40, "Red")

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 1000, 110)
frame.add_button("Restart", init)
l=frame.add_label("Moves = 0")


# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()
