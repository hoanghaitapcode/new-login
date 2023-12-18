import cv2
import face_recognition
import tkinter as tk
from tkinter import messagebox, Toplevel, Label, Entry, Button
from PIL import ImageTk, Image
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from validate_email_address import validate_email
import tkinter.font as tkfont
from pygame import *





class FaceRecognitionApp:
    def __init__(self):
        self.user_data_path = "data"
        if not os.path.exists(self.user_data_path):
            os.makedirs(self.user_data_path)

        self.screen = tk.Tk()
        self.screen.geometry("1280x720")
        self.screen.title("US88")

    def register_face1(self):
        username = self.register_username_entry.get()
        if os.path.exists(f"data/{username}.jpg"):
            messagebox.showinfo("Đăng ký", "Tên đăng nhập đã tồn tại. Hãy chọn tên đăng nhập khác.")
            return
        user_path = os.path.join(self.user_data_path, username)

        if os.path.exists(user_path):
            messagebox.showerror("Lỗi", "Tên đăng nhập đã tồn tại. Vui lòng chọn tên đăng nhập khác.")
            return

        capture = cv2.VideoCapture(0)
        while True:
            ret, frame = capture.read()
            cv2.imshow('Press space to capture', frame)
            if cv2.waitKey(1) & 0xFF == ord(' '):
                break

        capture.release()

        cv2.imwrite(f"data/{username}.jpg", frame)
        messagebox.showinfo("Đăng ký", "Đăng ký thành công.")
        self.screen4.destroy()

    def createEntryWithImage(root, image_path, toado1, toado2):
        entry_frame = tk.Frame(root, width=720, height=360)
        entry_frame.pack()

        custom_font = tkfont.Font("", 12, "normal", foreground='White')

        entry = tk.Entry(entry_frame, width=720, borderwidth=0, highlightthickness=0, font=custom_font)
        entry.configure(fg='white')

        # Create Label to display the image
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(entry_frame, image=photo)
        label.image = photo  # Keep a reference to the image

        # Create Entry widget
        entry = tk.Entry(entry_frame, bg="#2c3e50")

        # Set the position of Label and Entry in the frame
        label.place(x=toado1, y=toado2)
        entry.place(x=toado1 + 35, y=toado2 + 12)

        return entry_frame, entry

    def login_verify1(self):
        username = self.login_username_entry.get()
        if not os.path.exists(f"data/{username}.jpg"):
            messagebox.showinfo("Đăng nhập", "Tên đăng nhập không tồn tại.")
            return

        capture = cv2.VideoCapture(0)
        while True:
            ret, frame = capture.read()
            cv2.imshow('Press space to capture', frame)
            if cv2.waitKey(1) & 0xFF == ord(' '):
                break

        capture.release()

        known_image = face_recognition.load_image_file(f"data/{username}.jpg")
        unknown_image = frame

        known_face_encodings = face_recognition.face_encodings(known_image)

        if not known_face_encodings:
            messagebox.showinfo("Đăng nhập", "Không tìm thấy khuôn mặt trong ảnh đã đăng ký.")
            return

        known_face_encoding = known_face_encodings[0]

        unknown_face_encodings = face_recognition.face_encodings(unknown_image)

        if not unknown_face_encodings:
            messagebox.showinfo("Đăng nhập", "Không tìm thấy khuôn mặt trong ảnh vừa chụp.")
            return

        unknown_face_encoding = unknown_face_encodings[0]

        results = face_recognition.compare_faces([known_face_encoding], unknown_face_encoding)

        if results[0]:
            messagebox.showinfo("Đăng nhập", "Đăng nhập thành công.")
        else:
            messagebox.showinfo("Đăng nhập", "Đăng nhập không thành công.")

    def register(self):
        self.screen4 = Toplevel(self.screen)
        self.screen4.title("Đăng Ký")
        self.screen4.geometry("300x250")

        self.register_username_label = Label(self.screen4, text="Tên đăng nhập * ")
        self.register_username_label.pack()
        self.register_username_entry = Entry(self.screen4)
        self.register_username_entry.pack()

        self.register_face_button = Button(self.screen4, text="Chụp ảnh khuôn mặt", command=self.register_face1)
        self.register_face_button.pack()

    def login_verify(self):
        username = self.login_username_entry.get()
        if not os.path.exists(f"data/{username}.jpg"):
            messagebox.showinfo("Đăng nhập", "Tên đăng nhập không tồn tại.")
            return

        capture = cv2.VideoCapture(0)
        while True:
            ret, frame = capture.read()
            cv2.imshow('Press space to capture', frame)
            if cv2.waitKey(1) & 0xFF == ord(' '):
                break

        capture.release()

        known_image = face_recognition.load_image_file(f"data/{username}.jpg")
        unknown_image = frame

        known_face_encodings = face_recognition.face_encodings(known_image)

        if not known_face_encodings:
            messagebox.showinfo("Đăng nhập", "Không tìm thấy khuôn mặt trong ảnh đã đăng ký.")
            return

        known_face_encoding = known_face_encodings[0]

        unknown_face_encodings = face_recognition.face_encodings(unknown_image)

        if not unknown_face_encodings:
            messagebox.showinfo("Đăng nhập", "Không tìm thấy khuôn mặt trong ảnh vừa chụp.")
            return

        unknown_face_encoding = unknown_face_encodings[0]

        results = face_recognition.compare_faces([known_face_encoding], unknown_face_encoding)

        if results[0]:
            messagebox.showinfo("Đăng nhập", "Đăng nhập thành công.")
        else:
            messagebox.showinfo("Đăng nhập", "Đăng nhập không thành công.")

    def main_screen(self):
        self.screen1 = Toplevel(self.screen)
        self.screen1.title("US88")
        self.screen1.geometry("300x250")

        self.login_button = Button(self.screen1, text="Đăng nhập", command=self.login)
        self.login_button.pack()

        self.register_button = Button(self.screen1, text="Đăng ký", command=self.register)
        self.register_button.pack()

    def login(self):
        self.screen2 = Toplevel(self.screen)
        self.screen2.title("Đăng Nhập")
        self.screen2.geometry("300x250")

        self.login_username_label = Label(self.screen2, text="Tên đăng nhập * ")
        self.login_username_label.pack()
        self.login_username_entry = Entry(self.screen2)
        self.login_username_entry.pack()

        self.login_face_button = Button(self.screen2, text="Chụp ảnh khuôn mặt", command=self.login_verify1)
        self.login_face_button.pack()

    def send_email(self):
        email = self.email_entry.get()
        if not validate_email(email):
            messagebox.showinfo("Lỗi", "Địa chỉ email không hợp lệ.")
            return

        message = MIMEMultipart()
        message["From"] = "your_email@gmail.com"
        message["To"] = email
        message["Subject"] = "Subject"

        message.attach(MIMEText("This is the email content"))

        try:
            smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
            smtpObj.starttls()
            smtpObj.login("your_email@gmail.com", "your_password")
            smtpObj.sendmail("your_email@gmail.com", email, message.as_string())
            smtpObj.quit()
            messagebox.showinfo("Thông báo", "Email đã được gửi.")
        except:
            messagebox.showinfo("Lỗi", "Không thể gửi email. Vui lòng thử lại sau.")

    def forgot_password(self):
        self.screen3 = Toplevel(self.screen)
        self.screen3.title("Quên Mật Khẩu")
        self.screen3.geometry("300x250")

        self.email_label = Label(self.screen3, text="Địa chỉ email * ")
        self.email_label.pack()
        self.email_entry = Entry(self.screen3)
        self.email_entry.pack()

        self.send_email_button = Button(self.screen3, text="Gửi Email", command=self.send_email)
        self.send_email_button.pack()

    def menu_screen(self):
        self.screen6 = Toplevel(self.screen)
        self.screen6.title("Menu")
        self.screen6.geometry("300x250")

        self.logout_button = Button
if __name__ == "__main__":
    app = FaceRecognitionApp()
    app.main_screen()
