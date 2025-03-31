import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter.messagebox as msg

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("ماشین حساب انیمیشن دار")
        self.root.geometry("350x500")
        self.root.resizable(False, False)
        
        # تنظیم تم تاریک
        self.style = ttk.Style(theme='morph')
        
        # متغیرهای محاسباتی
        self.current_expression = ""
        self.display_var = ttk.StringVar()
        
        # ایجاد رابط کاربری
        self.create_widgets()
        self.bind_events()
    
    def create_widgets(self):
        # فیلد نمایش نتیجه
        self.display = ttk.Entry(
            self.root,
            textvariable=self.display_var,
            font=('Arial', 24, 'bold'),
            justify=RIGHT,
            bootstyle=SECONDARY
        )
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)
        
        # دکمه‌های ماشین حساب
        buttons = [
            ('C', 1, 0), ('±', 1, 1), ('%', 1, 2), ('÷', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('×', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('=', 5, 2)
        ]
        
        for (text, row, col) in buttons:
            btn = ttk.Button(
                self.root,
                text=text,
                style='TButton',
                command=lambda t=text: self.on_button_click(t)
            )
            btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
            
            # انیمیشن‌ها
            btn.bind("<Enter>", lambda e, b=btn: self.on_enter(e, b))
            btn.bind("<Leave>", lambda e, b=btn: self.on_leave(e, b))
            btn.bind("<Button-1>", lambda e, b=btn: self.on_press(e, b))
        
        # تنظیم سایز ردیف‌ها و ستون‌ها
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
    
    def bind_events(self):
        # کلیدهای صفحه کلید
        self.root.bind('<Return>', lambda e: self.calculate())
        self.root.bind('<Escape>', lambda e: self.clear())
    
    def on_button_click(self, text):
        if text == 'C':
            self.clear()
        elif text == '=':
            self.calculate()
        else:
            self.current_expression += str(text)
            self.display_var.set(self.current_expression)
    
    def calculate(self):
        try:
            result = eval(self.current_expression.replace('×', '*').replace('÷', '/'))
            self.display_var.set(result)
            self.current_expression = str(result)
        except:
            msg.showerror("خطا", "عبارت وارد شده نامعتبر است")
            self.clear()
    
    def clear(self):
        self.current_expression = ""
        self.display_var.set("")
    
    def on_enter(self, event, button):
        button.configure(bootstyle=(INFO, OUTLINE))
    
    def on_leave(self, event, button):
        button.configure(bootstyle=PRIMARY)
    
    def on_press(self, event, button):
        button.configure(bootstyle=SUCCESS)
        self.root.after(150, lambda: button.configure(bootstyle=PRIMARY))

if __name__ == "__main__":
    print("این محیط از برنامه‌های گرافیکی پشتیبانی نمی‌کند")
    print("برای اجرای این ماشین حساب، لطفاً کد را در محیطی با قابلیت نمایش گرافیکی اجرا کنید")
    print("محتویات فایل calculator.py:")
    with open(__file__, 'r', encoding='utf-8') as f:
        print(f.read())
