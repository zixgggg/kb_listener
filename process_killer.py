import subprocess
import sys
import tkinter
def kill_process(name, root, label, entry):
    try:
        if sys.platform.startswith('win'):
            result = subprocess.run(
                ["taskkill", "/f", "/im", name],
                capture_output=True, text=True, check=True
            )
            msg = result.stdout
            label.config(text=msg)
            entry.config(state='disabled')
            root.after(3000, root.destroy)
        else:
            result = subprocess.run(
                ["pkill", "-f", name],
                capture_output=True, text=True, check=True
            )
            msg = result.stdout
            label.config(text=msg)
            entry.config(state='disabled')
            root.after(1000, root.destroy)
    except subprocess.CalledProcessError as e:
        msg = e.stderr or e.stdout or str(e)
        label.config(text=msg)
        entry.config(state='normal')

def on_submit(entry, label, root):
    name = entry.get().strip()
    if name:
        kill_process(name, root, label, entry)

root = tkinter.Tk()
root.title("Process Killer")

tkinter.Label(root, text="請輸入要關閉的進程名稱:").pack()
entry = tkinter.Entry(root)
entry.pack()
label = tkinter.Label(root, text="")
label.pack()

submit_btn = tkinter.Button(root, text="關閉進程", command=lambda: on_submit(entry, label, root))
submit_btn.pack()
submit_btn2=tkinter.Button(root,text="close kb_listener.exe",command=lambda: kill_process("kb_listener.exe",root,label,entry))
submit_btn2.pack()
entry.focus()
root.mainloop()