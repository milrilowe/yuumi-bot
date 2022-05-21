import socket
from pynput.keyboard import Key, Listener as KeyboardListener
from pynput.mouse import Controller, Listener as MouseListener


HEADER = 2
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "184.190.147.184"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

mouse = Controller()



def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


chars = ["Q", "W", "E", "R", "A", "S", "V", "D", "F", "M"]

def on_press(key):
    x, y = mouse.position

    try:
        if key.char in chars:
            print(f"{key.char}{x},{y}")
            send(f"{key.char}{x},{y}")
    except AttributeError as err:
        if key == Key.caps_lock:
            # mouse_listener.stop()
            keyboard_listener.stop()
        else:
            print(err)

def on_move(x, y):
    send(f"?{x},{y}")

# Keyboard Listener
keyboard_listener = KeyboardListener(on_press=on_press)

# Mouse Listener
mouse_listener = MouseListener(on_move=on_move)

keyboard_listener.start()
mouse_listener.start()
keyboard_listener.join()
mouse_listener.join()

send(DISCONNECT_MESSAGE)