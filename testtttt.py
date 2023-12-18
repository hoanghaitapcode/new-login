from PIL import Image,ImageTk
import tkinter as tk


def createEntryWithImage(root, image_path):
    frame = tk.Frame(root)

    # Tạo Label để hiển thị hình ảnh
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(frame, image=photo)
    label.image = photo  # Giữ tham chiếu đến ảnh

    # Tạo Entry widget
    entry = tk.Entry(frame)

    # Đặt vị trí của Label và Entry trong frame
    label.pack(side="left")
    entry.pack(side="left")

    return frame, entry


# Tạo cửa sổ giao diện
root = tk.Tk()

# Tạo Entry widget với hình ảnh
entry_frame, entry_widget = createEntryWithImage(root, "D:/pythonProject1/1x/username.png")
entry_frame.pack()

# Chạy vòng lặp chính của ứng dụng
root.mainloop()