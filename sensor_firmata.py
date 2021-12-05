import datetime
from pyfirmata import Arduino, util

filename = "text.txt" #execute in file dir jaatziimee settings

board = Arduino("COM11")
it = util.Iterator(board) # divas rindas lai sanemtu no arduino
it.start() # divas rindas lai sanemtu no arduino

d10 = board.get_pin("s:10:o")
d10.write(1)
button = board.get_pin("d:7:i")

a0 = board.get_pin("a:0:i") #analog, o pin, input
a0.read()

button_state = True
autoPumpStateWriteOn = True
autoPumpStateWriteOff = True

while 1:


    board.pass_time(.1)
    b = button.read()
    print(b)

    if b == False:
        d10.write(1)
        button_state  = not button_state
        print("pogas statuss " + str(button_state))
        board.pass_time(1)

        if (button_state):            
            with open(filename, mode="a") as f:
                f.write("Suknis automatiska rezimaa ")
                t = datetime.datetime.now()
                f.write(str(t) + "\n")  
        else:
            with open(filename, mode="a") as f:
                f.write("Suknis ieslegts manuaali ")
                t = datetime.datetime.now()
                f.write(str(t) + "\n")    
    
    
    a = a0.read()
    a = round(a * 100)
    print(a)

    

    if (button_state):
        if a > 80:
            d10.write(1)
            if autoPumpStateWriteOn:
                with open(filename, mode="a") as f:
                    f.write("Suknis ieslegts ")
                    t = datetime.datetime.now()
                    f.write(str(t) + "\n")
                autoPumpStateWriteOn = False
                autoPumpStateWriteOff = True

        else:
            d10.write(0)
            if autoPumpStateWriteOff:
                with open(filename, mode="a") as f:
                    f.write("Suknis izslegts ")
                    t = datetime.datetime.now()
                    f.write(str(t) + "\n")
                autoPumpStateWriteOff = False
                autoPumpStateWriteOn = True


# for i in dir(board):
#     print(i)