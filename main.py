from pynput import keyboard
import os

def on_press(key):
    try:
        # 處理按鍵顯示
        try:
            input_word = key.char
        except AttributeError:
            input_word = str(key).replace("Key.", "◀︎")
            input_word = input_word+"▶︎"
        print(input_word)
        # 寫入檔案
        with open("record", "a") as f:
            f.write(input_word)
    except Exception as e:
        print(f"Error: {e}")
        return False
def on_release(key):
    if key == keyboard.Key.esc:
        return False

try:
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
except KeyboardInterrupt:
    print("Exiting...")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Listener stopped.")