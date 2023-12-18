from PIL import Image,ImageTk
import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk


def createEntryWithImage(root, image_path,toado1,toado2):
    entry_frame = tk.Frame(root, width=720, height=360)
    entry_frame.pack()

    custom_font=tkfont.Font("",12,"normal",foreground='White')

    entry = tk.Entry(entry_frame, width=720, borderwidth=0, highlightthickness=0,font=custom_font)
    entry.configure(fg='white')

    # Tạo Label để hiển thị hình ảnh
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(entry_frame, image=photo)
    label.image = photo  # Giữ tham chiếu đến ảnh

    # Tạo Entry widget
    entry = tk.Entry(entry_frame,bg="#2c3e50")

    # Đặt vị trí của Label và Entry trong frame
    label.place(x=toado1,y=toado2)
    entry.place(x=toado1+35,y=toado2+12)

    return entry_frame, entry


# Tạo cửa sổ giao diện
root = tk.Tk()
# Tạo Entry widget với hình ảnh
toado1=10
toado2=20
entry_frame,entry = createEntryWithImage(root, "D:/pythonProject1/1x/newpass.png",toado1,toado2)
entry_frame.pack()

# Chạy vòng lặp chính của ứng dụng
root.mainloop()