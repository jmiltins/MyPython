import datetime
filename = "text.txt" #execute in file dir jaatziimee settings

with open(filename, mode="a") as f:
    #f.readlines(): # lasa visu failu
    #f.readline() # lasa pa rindinai
    f.write("velreiz raksti" + "\n")
    
    t = datetime.datetime.now()
    f.write(str(t) + "\n")