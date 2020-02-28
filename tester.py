from gui import *

root = Tk()
mainWindow = Window(root)


counter =0
def countercahnge():
	global test
	global counter
	counter+=1
	test.labelh.config(text=str(counter))

test = addLabel(root,"hello",1,1)
test.labelh.config(text="bye")



root.mainloop()