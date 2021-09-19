# Basic tkinter template
from tkinter import *

root=Tk()
root.title("Identity Card")
root.geometry("300x400")



root.window
root.geometry("20x20")

root.configure(bg="white")
canvas=Canvas(root,width=400,height=250)
canvas.create_image(0,0,anchor=NW)
canvas.create_rectangle(0, 0, 400, 45, fill="#F6091E")


label_heading = canvas.create_text(200,20, font=('Times', '24', 'bold italic') ,text="Driving License", fill = "white")
label_id_tag = canvas.create_text(25,60, font=('Times', '14', 'bold') ,text="ID : 19827198349")
label_name_tag = canvas.create_text(30,100, font=('Times', '12', 'bold') ,text="Name : Ishaan Kamti")
label_dob_tag = canvas.create_text(52,120, font=('Times', '12', 'bold') ,text="Date of birth : 27 June 2008")
label_pin_tag = canvas.create_text(32,140, font=('Times', '12', 'bold') ,text="Pin no. : 451478")
label_address_tag = canvas.create_text(36,160, font=('Times', '12', 'bold') ,text="Address : Ranchi,Jharkhand,India")
label_vehicle_type_tag = canvas.create_text(155,180, font=('Times', '12', 'bold') ,text="Authorisation to drive the following vehicles : Two Four")

#button1.configure(width = 20 , activebackground = "#9EC6EE", relief= FLAT)
button1_window = canvas.create_window(200, 235, anchor=CENTER, window=button1)
label_id_window = canvas.create_window(80, 60, anchor=CENTER, window=label_id)
label_name_window = canvas.create_window(100, 100, anchor=CENTER, window=label_name)
label_dob_window = canvas.create_window(140, 120, anchor=CENTER, window=label_dob)
label_pin_window = canvas.create_window(85, 140, anchor=CENTER, window=label_pin)
label_address_window = canvas.create_window(130, 160, anchor=CENTER, window=label_address)
label_vehicle_no_window = canvas.create_window(335, 180, anchor=CENTER, window=label_vehicle_type)
canvas.pack()


def mycardDetails():
       label_id_window=19827198349
       print(type(label_id_window))
label_name_window="Ishaan Kamti"
print(type(label_name_window))
label_dob_window=27 June 2008
print(type(label_dob_window))
label_pin_window=451478
print(type(label_pin_window))
label_address_window=Ranchi,Jharkhand,India
print(type(label_address_window))
label_vehicle_no_window= Two Four
print(type(label_vehicle_no_window))
    
button1 = button(root, text="Show my ID Card",command=myCardDetails)# Define the function

  



      
      
root.mainloop()



# tkinter basic template end statement
