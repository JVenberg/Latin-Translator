import subprocess
import re
import unicodedata
from Tkinter import Label, Tk, N, S, W, E, END
import ScrolledText

WIDTH = 1000
HEIGHT = 500
PADDING = 5

def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

def focus():
	input_box.focus_set()
	
def click_up(event):
    event.widget.config(bg = "#F44336")
    root.update()

def select_all(event):
	event.widget.tag_add("sel","1.0","end")

def shift_press(event):
	root.focus_set()

def return_press(event):
	root.focus_set()
	translate()

def click_down(event):
    event.widget.config(bg = "#B71C1C")
    translate()
    root.update()

def translate():
	inpt = input_box.get(1.0, END)
	# inpt = unicode(inpt, "utf-8")
	inpt = strip_accents(inpt)
	inpt = re.sub(r'([^\s\w]|_)+', '', inpt)
	lines = str(inpt).splitlines()


	translation = ""
	for line in lines:
		p = subprocess.Popen(["./words",line], stdout=subprocess.PIPE, cwd="./www")
		(output, err) = p.communicate()
		translation += output

	output_box.delete("1.0", END)
	output_box.insert(END, translation)

root = Tk()
input_label = Label(root, text="Input",height=1,width=10,font=(None,20),bg="#F44336",fg="white")
input_box = ScrolledText.ScrolledText(root,height=5)
output_label = Label(root, text="Output",height=1,width=10,font=(None,20),bg="#F44336",fg="white")
output_box = ScrolledText.ScrolledText(root)
submit_button = Label(root, text="Submit",height=1,width=10,font=(None,20),bg="#F44336",fg="white")

input_label.grid(row=0,column=0,rowspan=1,columnspan=1,sticky=N+S+W+E,padx=PADDING,pady=PADDING)
input_box.grid(row=1,column=0,rowspan=2,columnspan=3,sticky=N+S+W+E,padx=PADDING,pady=PADDING)

output_label.grid(row=3,column=0,rowspan=1,columnspan=1,sticky=N+S+W+E,padx=PADDING,pady=PADDING)
output_box.grid(row=4,column=0,rowspan=2,columnspan=3,sticky=N+S+W+E,padx=PADDING,pady=PADDING)
submit_button.grid(row=5, column=3,sticky=N+S+W+E,padx=PADDING,pady=PADDING)
submit_button.bind("<Button-1>", click_down)
submit_button.bind("<ButtonRelease-1>", click_up)		

for x in range(1,root.grid_size()[0] - 1):
    root.grid_columnconfigure(x, weight=1,minsize=20)


root.grid_rowconfigure(0, weight=0,minsize=5)
root.grid_rowconfigure(1, weight=0,minsize=10)
root.grid_rowconfigure(2, weight=0,minsize=10)
root.grid_rowconfigure(3, weight=0,minsize=5)
root.grid_rowconfigure(4, weight=1,minsize=10)
root.grid_rowconfigure(5, weight=0,minsize=10)

input_box.bind("<Command-Return>", return_press)
output_box.bind("<Command-Return>", return_press)
root.bind("<Command-Return>", return_press)
input_box.bind("<Command-a>", select_all)
output_box.bind("<Command-a>", select_all)

root.title("Latin Translator")
root.geometry(str(WIDTH)+"x"+str(HEIGHT))
root.minsize(str(WIDTH),str(HEIGHT))
root.configure(background='#757575')
root.after(500, focus)
root.mainloop()

