''' Captcha generator project created by NIKHIL PATIL'''
import string
import random
from tkinter import *
from PIL import ImageTk, Image
from captcha.image import ImageCaptcha

''' Defining the method createimage() which will create and generate
    captcha image based on randomly generated strings. This captcha image
    is then incorporated into the GUI window which we have created'''

def createimage(flag = 0) :
    global random_strings
    global image_label
    global image_display
    global entry
    global verify_label

    ''' The below if block works only when we clicks the Reload button in the GUI 
        It basically removes the label (if visible) which shows the whether the entered string 
        is correct or incorrect'''
    if flag == 1 :
        verify_label.grid_forget()

    #Removing the contents from entry box
    entry.delete(0,END)

    #Generating random string for captcha
    random_strings = ''.join(random.choices(string.ascii_letters + string.digits , k = 6))

    #creating a captcha image
    image_captcha = ImageCaptcha(width = 250 , height = 100)
    image_generated = image_captcha.generate(random_strings)
    image_display = ImageTk.PhotoImage(Image.open(image_generated))

    #Removing previous image if present and displaying new one
    image_label.grid_forget()
    image_label = Label(root, image = image_display)
    image_label.grid(row = 1, column = 0, columnspan= 2, padx = 10)


''' Here we are defining the method check() 
    which will check whether the string entered by the user matches the randomly generated 
    string . If there is match then "verified" will pops up on the window
    otherwise , "Incorrect" will pops up on the window and new captcha image is generated for the user 
    to try again'''

def check(x,y) :
    #using global variables which we have created above
    global verify_label
    verify_label.grid_forget()

    if x.lower() == y.lower() :
        verify_label = Label(master = root,
                             text = "VERIFICATION DONE",
                             font = 'Arial 15',
                             bg = '#ffe75c',
                             fg = '#00a806' )
        verify_label.grid(row = 0, column = 0, columnspan= 2, pady = 10)

    else :
        verify_label = Label(master = root,
                             text = "INCORRECT",
                             font = 'Arial 15',
                             bg = '#ffe75c',
                             fg = '#fa0800')
        verify_label.grid(row = 0, column = 0, columnspan = 2, pady = 10)
        createimage()

if __name__ == '__main__' :
    #initializing tkinter GUI by creating a root widget
    root = Tk()
    root.title('Verify Here')
    root.configure(background='#ffe75c')

   #intializing the variable to be defined later
    verify_label = Label(root)
    image_label = Label(root)

    #Defining input box in the window
    entry = Entry(root, width = 10, borderwidth = 5,font = 'Arial 15', justify = 'center')
    entry.grid(row = 2, column = 0 )

    #creating an image for the first time
    createimage()

    #adding reload button and its image in GUI window
    reload_img = ImageTk.PhotoImage(Image.open('refresh.png').resize((32,32), Image.ANTIALIAS))
    reload_button = Button(image = reload_img,command = lambda : createimage(1))
    reload_button.grid(row = 2, column = 1, pady = 10)

    #defining the submit button
    submit_button = Button(root, text = 'Submit', font = 'Arial 10', command =lambda : check(entry.get(),random_strings ))
    submit_button.grid(row= 3, column = 0, columnspan= 2, pady = 10)

    root.mainloop()