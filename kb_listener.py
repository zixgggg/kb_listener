from pynput import keyboard
import os
import tkinter
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
        with open("record", "a",encoding="utf-8") as f:
            f.write(input_word)
    except Exception as e:
        print(f"Error: {e}")
        return False
try:
    root = tkinter.Tk()
    word = tkinter.Label(root, text="kb_listener is running")
    word.pack()
    root.after(1000, root.destroy)
    root.title("kb_listener")
    root.mainloop()
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
except KeyboardInterrupt:
    print("Exiting...")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Listener stopped.")