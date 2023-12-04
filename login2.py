import cv2
import face_recognition
import tkinter as tk
from tkinter import  messagebox
from tkinter import*
from PIL import ImageTk,Image
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
user_data_path = "data"
if not os.path.exists(user_data_path):
    os.makedirs(user_data_path)


def register_face1():
    username=register_username_entry.get()
    # Kiểm tra xem người dùng đã đăng ký chưa
    if os.path.exists(f"data/{username}.jpg"):
        messagebox.showinfo("Đăng ký", "Tên đăng nhập đã tồn tại. Hãy chọn tên đăng nhập khác.")
        return
    user_path = os.path.join(user_data_path, username)

    # Check if the user directory already exists
    if os.path.exists(user_path):
        messagebox.showerror("Lỗi", "Tên đăng nhập đã tồn tại. Vui lòng chọn tên đăng nhập khác.")
        return


    # Chụp ảnh từ webcam
    capture = cv2.VideoCapture(0)
    ret, frame = capture.read()
    capture.release()

    # Lưu ảnh với tên đăng nhập là tên file
    cv2.imwrite(f"data/{username}.jpg", frame)
    messagebox.showinfo("Đăng ký", "Đăng ký thành công.")
def login_verify1():
    username= login_username_entry.get()
    # Kiểm tra xem tên đăng nhập có tồn tại không
    if not os.path.exists(f"{username}.jpg"):
        messagebox.showinfo("Đăng nhập", "Tên đăng nhập không tồn tại.")
        return

    # Chụp ảnh từ webcam
    capture = cv2.VideoCapture(0)
    ret, frame = capture.read()
    capture.release()

    # Nạp ảnh đã đăng ký và ảnh vừa chụp
    known_image = face_recognition.load_image_file(f"{username}.jpg")
    unknown_image = frame

    # Xác định khuôn mặt trong ảnh
    known_face_encodings = face_recognition.face_encodings(known_image)

    if not known_face_encodings:
        messagebox.showinfo("Đăng nhập", "Không tìm thấy khuôn mặt trong ảnh đã đăng ký.")
        return

    # Chỉ sử dụng khuôn mặt đầu tiên nếu có nhiều khuôn mặt
    known_face_encoding = known_face_encodings[0]

    unknown_face_encodings = face_recognition.face_encodings(unknown_image)

    if not unknown_face_encodings:
        messagebox.showinfo("Đăng nhập", "Không tìm thấy khuôn mặt trong ảnh vừa chụp.")
        return

    unknown_face_encoding = unknown_face_encodings[0]

    # So sánh khuôn mặt
    results = face_recognition.compare_faces([known_face_encoding], unknown_face_encoding)

    if results[0]:
        messagebox.showinfo("Đăng nhập", "Đăng nhập thành công.")
    else:
        messagebox.showinfo("Đăng nhập", "Xác thực không thành công.")

def register_face():
    global screen4
    global  register_username_entry
    screen4=Toplevel(screen3)

    tk.Label(screen4, text="Tên đăng nhập:").pack()
    register_username_entry = Entry(screen4)
    register_username_entry.pack(pady=10)

    Button(screen4, text="Đăng ký", command=register_face1).pack()
def window_log_face():
    global screen3
    screen3 = Toplevel(screen)
    screen3.geometry("1280x720")

    global login_username_entry
    global register_username_entry

    log_label=Label(screen3, text="Tên đăng nhập:")
    log_label.place(x=640,y=340)
    login_username_entry = Entry(screen3)
    login_username_entry.place(x=640,y=360)
    username = login_username_entry
    log1=Button(screen3, text="Đăng nhập", command=login_verify1)
    log1.place(x=640,y=385)
    reg1=Button(screen3,text="Đăng ký",command=register_face)
    reg1.place(x=640,y=415)
def send_registration_email(username, email):
    # Cấu hình thông tin email
    sender_email = "hhhhai1012@gmail.com"  # Thay thế bằng địa chỉ email của bạn
    sender_password = "orhgdylbyzxsghiu"  # Thay thế bằng mật khẩu email của bạn

    # Tạo đối tượng MIMEMultipart để xây dựng email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = "Đăng ký thành công"

    # Nội dung email
    body = f"Chào mừng bạn, {username}! Bạn đã đăng ký thành công."
    msg.attach(MIMEText(body, 'plain'))

    # Gửi email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email, msg.as_string())

def login_verify():
    global login_username_entry, login_password_entry

    username = login_username_entry.get()
    password = login_password_entry.get()

    user_path = os.path.join(user_data_path, username)
    if username not in os.listdir(user_data_path) or not os.path.isfile(os.path.join(user_path, "password.txt")):
        messagebox.showerror("Lỗi", "Tên đăng nhập không tồn tại. Đăng nhập thất bại.")
    else:
        with open(os.path.join(user_path, "password.txt"), "r") as f:
            stored_password = f.read().strip()

        if password == stored_password:
            messagebox.showinfo("Thông báo", "Đăng nhập thành công.")
        else:
            messagebox.showerror("Lỗi", "Mật khẩu không đúng. Đăng nhập thất bại.")
def register():
    global register_username_entry, register_password_entry, register_email_entry

    username = register_username_entry.get()
    password = register_password_entry.get()
    email = register_email_entry.get()

    user_path = os.path.join(user_data_path, username)
    if os.path.exists(f"data/{username}.jpg"):
        messagebox.showinfo("Đăng ký", "Tên đăng nhập đã tồn tại. Hãy chọn tên đăng nhập khác.")
        return

    # Check if the user directory already exists
    if os.path.exists(user_path):
        messagebox.showerror("Lỗi", "Tên đăng nhập đã tồn tại. Vui lòng chọn tên đăng nhập khác.")
    else:
        # Create the user directory and save registration information
        os.makedirs(user_path)
        with open(os.path.join(user_path, "password.txt"), "w") as f:
            f.write(password)

        # Gửi email thông báo đăng ký thành công
        send_registration_email(username, email)

        messagebox.showinfo("Thông báo", "Đăng ký thành công")
def window_register():
    global screen1
    global register_username_entry
    global register_password_entry
    global register_email_entry
    screen1 = Toplevel(screen)
    Label(screen1, text="Username * ").pack()
    register_username_entry = tk.Entry(screen1)
    register_username_entry.pack(pady=10)
    Label(screen1, text="").pack()
    Label(screen1, text="Password * ").pack()
    register_password_entry = tk.Entry(screen1, show="*")
    register_password_entry.pack(pady=10)
    Label(screen1, text="").pack()
    Label(screen1, text="email *").pack()
    register_email_entry = tk.Entry(screen1)
    register_email_entry.pack(pady=10)

    Button(screen1, text="Register", width=10, height=1, command=register).pack()
def window_log_normal():
    global login_username_entry
    global login_password_entry
    global screen2
    screen2 = Toplevel(screen)

    Label(screen2, text="Tên đăng nhập:").pack()
    login_username_entry = Entry(screen2)
    login_username_entry.pack(pady=10)
    Label(screen2,text="Mật khẩu:").pack()
    login_password_entry=Entry(screen2)
    login_password_entry.pack(pady=10)

    Button(screen2, text="Login", width=10, height=1, command=login_verify).pack()
    Button(screen2,text="Register",width=10,height=1,command=window_register).pack()

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("1280x720")
    screen.title("GAMELOL")
    bg=ImageTk.PhotoImage(file="bg1.webp")
    bg_image=Label(screen,image=bg).place(x=0,y=0,relwidth=1,relheight=1)
    login1_but=Button(text="Log by username and password",height="2",width="30",command=window_log_normal)
    login1_but.place(x=350,y=550)
    login2_but=Button(text="log by face-id",height="2",width="30",command=window_log_face)
    login2_but.place(x=700,y=550)
    screen.mainloop()
main_screen()