from tkinter import*
from tkinter import ttk, messagebox, filedialog
from PIL import Image,ImageTk
import mysql.connector
import os

class Student():
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title('QUẢN LÝ SINH VIÊN')

        # variables
        self.var_mh = StringVar()
        self.var_ma = StringVar()
        self.var_HK = StringVar()
        self.var_NH = StringVar()
        self.var_TC = StringVar()
        self.var_Ma_sv = StringVar()
        self.var_Ten_sv = StringVar()
        self.var_Gioi_tinh = StringVar()
        self.var_Ngay_sinh = StringVar()
        self.var_Email = StringVar()
        self.var_SDT = StringVar()
        self.var_Noi_tam_tru = StringVar()
        self.var_Que_quan = StringVar()
        
        # ảnh ĐHQG
        img = Image.open(r"../Final_project/images/logo_uet.png")
        new_size = (1530,200)
        img_resized = img.resize(new_size, Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(img)
        self.pic1 = Button(self.root, image=self.img, cursor='hand2')
        self.pic1.place(x=0,y=0, width=1530, height=200)
        
        #Frame
        Frame1 = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        Frame1.place(x=0,y=200,width=1530,height=600)
        #trái
        Left_Frame =LabelFrame(Frame1, bd=4, relief=RIDGE, padx=2,text="Đăng ký",font=("times new roman",12,"bold"),fg='blue',bg='white')
        Left_Frame.place(x=0,y=0,width=680,height=580)
        #phải
        Right_Frame =LabelFrame(Frame1, bd=4, relief=RIDGE, padx=2,text="Thông tin sinh viên",font=("times new roman",12,"bold"),fg='blue',bg='white')
        Right_Frame.place(x=680,y=0,width=850,height=580)
        
        #thông tin khóa học
        Course_Info = LabelFrame(Left_Frame, bd=4,relief=RIDGE,padx=2, text="Thông tin Khóa học",font=("times new roman",12,"bold"),fg='blue',bg='white')
        Course_Info.place(x=10,y=30,width= 660, height=200)
        
        Ten_mh = Label(Course_Info,text='Tên môn học:',font=("times new roman",12,"bold"),bg='white')
        Ten_mh.grid(row = 0,column=0,padx=2,sticky=W)
        mh_combo = ttk.Combobox(Course_Info,textvariable=self.var_mh,font=("times new roman",12,"bold"),width=17,state='readonly')
        mh_combo['value'] = ('Tín hiệu hệ thống', 'Xác suất thống kê', 'Cơ sở dữ liệu', 'Lập trình xử lý dữ liệu với python', 'Tiếng anh B1', 'Tiếng anh B2')
        mh_combo.grid(row=0,column=1,padx=2,pady=10)

        Ma_mh = Label(Course_Info,text="Mã môn học:",font=("times new roman",12,"bold"),bg='white')
        Ma_mh.grid(row= 0, column=2,padx=2)
        ma_combo = ttk.Combobox(Course_Info,textvariable=self.var_ma,font=("times new roman",12,"bold"),width=17,state='readonly')
        ma_combo.grid(row=0,column=3,padx=2,pady=10)
        ma_combo['value'] = ('AIT2003','INT2211','AIT2002','MAT1101','FLF1107','ELT203')

        HK = Label(Course_Info,text="Học kỳ:",font=("times new roman",12,"bold"),bg='white')
        HK.grid(row= 2, column=0,padx=2)
        HK_combo = ttk.Combobox(Course_Info,textvariable=self.var_HK,font=("times new roman",12,"bold"),width=17,state='readonly')
        HK_combo.grid(row=2,column=1,padx=2,pady=10)
        HK_combo['value'] = ('Kỳ 1','Kỳ 2')

        Nam_hoc = Label(Course_Info,text="Năm học:",font=("times new roman",12,"bold"),bg='white')
        Nam_hoc.grid(row= 2, column=2,padx=2)
        NH_combo = ttk.Combobox(Course_Info,textvariable=self.var_NH,font=("times new roman",12,"bold"),width=17,state='readonly')
        NH_combo.grid(row=2,column=3,padx=2,pady=10)
        NH_combo['value'] = ('2020-2021','2021-2022','2022-2023','2023-2024','2024-2025')

        TC = Label(Course_Info,text="Số tín chỉ:",font=("times new roman",12,"bold"),bg='white')
        TC.grid(row= 4, column=0,padx=2)
        TC_combo = ttk.Combobox(Course_Info,textvariable=self.var_TC,font=("times new roman",12,"bold"),width=17,state='readonly')
        TC_combo.grid(row=4,column=1,padx=2,pady=10)
        TC_combo['value'] = ('1','2','3','4','5')

        #Thông tin sinh viên
        Student_Info = LabelFrame(Left_Frame, bd=4,relief=RIDGE,padx=2, text="Thông tin sinh viên",font=("times new roman",12,"bold"),fg='blue',bg='white')
        
        Student_Info.place(x=10,y=235,width= 660, height=250)
        Ma_sv = Label(Student_Info, text="Mã sinh viên:", font=("times new roman",12,"bold"),bg='white')
        Ma_sv.grid(row = 0, column=0,padx=2)
        Ma_sv_e = ttk.Entry(Student_Info,textvariable=self.var_Ma_sv, font=("times new roman",12,"bold"),width=17)
        Ma_sv_e.grid(row= 0,column=1,padx=2,pady=10)
        
        Ten_sv = Label(Student_Info,text="Tên sinh viên:",font=("times new roman",12,"bold"),bg='white')
        Ten_sv.grid(row=0,column=2,padx=2)
        Ten_sv_e = ttk.Entry(Student_Info,textvariable=self.var_Ten_sv,font=("times new roman",12,"bold"),width=17)
        Ten_sv_e.grid(row=0,column=3,padx=2,pady=10)
        
        Gioi_tinh = Label(Student_Info,text='Giới tính:', font=("times new roman",12,"bold"),bg='white')
        Gioi_tinh.grid(row = 1, column=0,padx=2)
        Gioi_tinh_e = ttk.Combobox(Student_Info,textvariable=self.var_Gioi_tinh,font=("times new roman",12,"bold"),width=17)
        Gioi_tinh_e.grid(row=1,column=1,padx=2,pady=10)
        Gioi_tinh_e['value']=('Nam','Nữ')
        
        Ngay_sinh = Label(Student_Info, text = "Ngày sinh:",font=("times new roman",12,"bold"),bg='white')
        Ngay_sinh.grid(row=1,column=2,padx=2)
        Ngay_sinh_e = ttk.Entry(Student_Info,textvariable=self.var_Ngay_sinh,font=("times new roman",12,"bold"),width=17)
        Ngay_sinh_e.grid(row=1,column=3,padx=2,pady=10)
        
        Email = Label(Student_Info,text='Email:', font=("times new roman",12,"bold"),bg='white')
        Email.grid(row = 2, column=0,padx=2)
        Email_e = ttk.Entry(Student_Info,textvariable=self.var_Email,font=("times new roman",12,"bold"),width=17)
        Email_e.grid(row=2,column=1,padx=2,pady=10)
        
        SDT = Label(Student_Info,text='SDT:', font=("times new roman",12,"bold"),bg='white')
        SDT.grid(row = 2, column=2,padx=2)
        SDT_e = ttk.Entry(Student_Info,textvariable=self.var_SDT,font=("times new roman",12,"bold"),width=17)
        SDT_e.grid(row=2,column=3,padx=2,pady=10)
        
        Noi_tam_tru = Label(Student_Info,text='Nơi tạm trú:', font=("times new roman",12,"bold"),bg='white')
        Noi_tam_tru.grid(row = 3, column=0,padx=20)
        Noi_tam_tru_e = ttk.Entry(Student_Info,textvariable=self.var_Noi_tam_tru,font=("times new roman",12,"bold"),width=17)
        Noi_tam_tru_e.grid(row=3,column=1,padx=2,pady=10)
        
        Que_quan = Label(Student_Info,text='Quê quán:', font=("times new roman",12,"bold"),bg='white')
        Que_quan.grid(row = 3, column=2,padx=2)
        Que_quan_e = ttk.Entry(Student_Info,textvariable=self.var_Que_quan,font=("times new roman",12,"bold"),width=17)
        Que_quan_e.grid(row=3,column=3,padx=2,pady=10)
        
        #Button
        Button_frame = Frame(Left_Frame,bd=4,relief=RIDGE,padx=2,bg='white')
        Button_frame.place(x=10,y=490,width=660,height=40)
        Add = Button(Button_frame,text="Save",command=self.add_data,font=("times new roman",12,"bold"),width=17,fg='blue',bg='white')
        Add.grid(row=0,column=0,padx=1)
        UPDATE = Button(Button_frame,text="Update",command=self.update_data,font=("times new roman",12,"bold"),width=17,fg='blue',bg='white')
        UPDATE.grid(row=0,column=1,padx=1)
        DEL = Button(Button_frame,text="Delete",command=self.delete_data,font=("times new roman",12,"bold"),width=17,fg='blue',bg='white')
        DEL.grid(row=0,column=2,padx=1)
        RESET = Button(Button_frame,text="Reset",command=self.reset_data,font=("times new roman",12,"bold"),width=17,fg='blue',bg='white')
        RESET.grid(row=0,column=3,padx=1)

        # Tra cứu thông tin sinh viên
        Seach_Frame = LabelFrame(Right_Frame, bd=4,relief=RIDGE,padx=2, text="Tra cứu thông tin sinh viên",font=("times new roman",12,"bold"),fg='blue',bg='white')
        Seach_Frame.place(x=10,y=10,width= 800, height=60)
        Seach_by = Label(Seach_Frame, font=('arial',11,'bold'),text='Seach By:',fg='red',bg='black')
        Seach_by.grid(row=0, column=0, sticky=W,padx=2,pady=5)
        
        self.var_box_search=StringVar()
        txt_seach = ttk.Combobox(Seach_Frame,textvariable=self.var_box_search,state='readonly',font=('arial',12,'bold'),width=18)
        txt_seach['value'] = ('Chọn Option','Mon_hoc','Ma_mon_hoc','Hoc_ki','Nam_hoc','Tin_chi','Ma_sv','Ten_sv','Gioi_tinh','Ngay_sinh','Email','SDT','Noi_tam_tru','Que_quan')
        txt_seach.current(0)
        txt_seach.grid(row=0,column=1,sticky=W,padx=2,pady=5)

        self.var_search=StringVar()
        txt_seach_com = ttk.Entry(Seach_Frame,textvariable=self.var_search,width=22,font=('arial',11,'bold'))
        txt_seach_com.grid(row=0,column=2,padx=5)
        
        pic_seach = Button(Seach_Frame,text='Search',command=self.search_data,font=('arial',11,'bold'),width=17,bg='blue',fg='white')
        pic_seach.grid(row=0,column=3,padx=5)
        
        pic_seachAll = Button(Seach_Frame,text='Show All',command=self.fetch_data,font=('arial',11,'bold'),width=17,bg='blue',fg='white')
        pic_seachAll.grid(row=0,column=4,padx=5)
        
        # ================Student School Bar================
        table_Frame = Frame(Right_Frame,bd=4,relief=RIDGE)
        table_Frame.place(x=10,y=80,width=800,height=470)
        
        scroll_x=ttk.Scrollbar(table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_Frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_Frame,columns=('Mon_hoc','Ma_mon_hoc','Hoc_ki','Nam_hoc','Tin_chi','Ma_sv','Ten_sv','Gioi_tinh','Ngay_sinh','Email','SDT','Noi_tam_tru','Que_quan',),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading('Mon_hoc',text='Môn học')        
        self.student_table.heading('Ma_mon_hoc',text='Mã môn học')        
        self.student_table.heading('Hoc_ki',text='Học kì')        
        self.student_table.heading('Nam_hoc',text='Năm học')        
        self.student_table.heading('Tin_chi',text='Số tín chỉ')        
        self.student_table.heading('Ma_sv',text='Mã sinh viên')        
        self.student_table.heading('Ten_sv',text='Tên sinh viên')        
        self.student_table.heading('Gioi_tinh',text='Giới tính')        
        self.student_table.heading('Ngay_sinh',text='Ngày sinh')        
        self.student_table.heading('Email',text='Email')        
        self.student_table.heading('SDT',text='Số điện thoại')        
        self.student_table.heading('Noi_tam_tru',text='Nơi tạm trú')        
        self.student_table.heading('Que_quan',text='Quê quán')        
        
        self.student_table['show']='headings'
        
        self.student_table.column('Mon_hoc', width=200)
        self.student_table.column('Ma_mon_hoc', width=100)
        self.student_table.column('Hoc_ki', width=100)
        self.student_table.column('Nam_hoc', width=100)
        self.student_table.column('Tin_chi', width=100)
        self.student_table.column('Ma_sv', width=100)
        self.student_table.column('Ten_sv', width=150)
        self.student_table.column('Gioi_tinh', width=100)
        self.student_table.column('Ngay_sinh', width=100)
        self.student_table.column('Email', width=150)
        self.student_table.column('SDT', width=100)
        self.student_table.column('Noi_tam_tru', width=100)
        self.student_table.column('Que_quan', width=100)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind('<ButtonRelease>',self.get_cursor)
        self.fetch_data()
    
    # Thêm dữ liệu
    def add_data(self):
        if (self.var_mh.get()=='' or self.var_Email.get()=='' or self.var_Ma_sv.get()==''):
            messagebox.showerror('Error','All Fields Are required')
        else:
            try:
                connection = mysql.connector.connect(host = 'localhost',username='root',password='Namtran@2004',database='quan_ly_sv')
                my_curen=connection.cursor()
                my_curen.execute('insert into sinh_vien values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                    self.var_mh.get(),
                    self.var_ma.get(),
                    self.var_HK.get(),
                    self.var_NH.get(),
                    self.var_TC.get(),
                    self.var_Ma_sv.get(),
                    self.var_Ten_sv.get(),
                    self.var_Gioi_tinh.get(),
                    self.var_Ngay_sinh.get(),
                    self.var_Email.get(),
                    self.var_SDT.get(),
                    self.var_Noi_tam_tru.get(),
                    self.var_Que_quan.get()
                ))
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showerror('Seccess','Student has been added!',parent = self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root)
    
    # Lấy dữ liệu
    def fetch_data(self):
        connection = mysql.connector.connect(host = 'localhost',username='root',password='Namtran@2004',database='quan_ly_sv')
        my_curen=connection.cursor()
        my_curen.execute('select * from sinh_vien')
        data=my_curen.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert('',END,values=i)
            connection.commit()
        connection.close()
        
    # Lấy cursor
    def get_cursor(self, event=''):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        data=content['values']
        
        self.var_mh.set(data[0])
        self.var_ma.set(data[1]),
        self.var_HK.set(data[2]),
        self.var_NH.set(data[3]),
        self.var_TC.set(data[4]),
        self.var_Ma_sv.set(data[5]),
        self.var_Ten_sv.set(data[6]),
        self.var_Gioi_tinh.set(data[7]),
        self.var_Ngay_sinh.set(data[8]),
        self.var_Email.set(data[9]),
        self.var_SDT.set(data[10]),
        self.var_Noi_tam_tru.set(data[11]),
        self.var_Que_quan.set(data[12])
        
    def update_data(self):
        if (self.var_mh.get()=='' or self.var_Email.get()=='' or self.var_Ma_sv.get()==''):
            messagebox.showerror('Error','All Fields Are required')
        else:
            try:
                update=messagebox.askyesno('Update','Are you sure update this student data',parent=self.root)
                if update>0:
                    connection = mysql.connector.connect(host = 'localhost',username='root',password='Namtran@2004',database='quan_ly_sv')
                    my_curen=connection.cursor()
                    my_curen.execute('update sinh_vien set Mon_hoc=%s, Ma_mon_hoc=%s,Hoc_ki=%s,Nam_hoc=%s,Tin_chi=%s,Ten_sv=%s,Gioi_tinh=%s,Ngay_sinh=%s,Email=%s,SDT=%s,Noi_tam_tru=%s,Que_quan=%s where Ma_sv=%s',(
                        self.var_mh.get(),
                        self.var_ma.get(),
                        self.var_HK.get(),
                        self.var_NH.get(),
                        self.var_TC.get(),
                        self.var_Ten_sv.get(),
                        self.var_Gioi_tinh.get(),
                        self.var_Ngay_sinh.get(),
                        self.var_Email.get(),
                        self.var_SDT.get(),
                        self.var_Noi_tam_tru.get(),
                        self.var_Que_quan.get(),
                        self.var_Ma_sv.get()
                    ))
                else:
                    if not update:
                        return
                connection.commit()
                self.fetch_data()
                connection.close()
                
                messagebox.showinfo('Success','Student successfully updated',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root)        
        
    # Delete
    def delete_data(self):
        if self.var_Ma_sv.get()=='':
            messagebox.showerror('Error','All Fields Are required')
        else:
            try:
                delete=messagebox.askyesno('Delete','Are you sure delete this student')
                if delete>0:
                    connection = mysql.connector.connect(host = 'localhost',username='root',password='Namtran@2004',database='quan_ly_sv')
                    my_curen=connection.cursor()
                    sql='delete from sinh_vien where Ma_sv=%s'
                    value=(self.var_Ma_sv.get(),)
                    my_curen.execute(sql,value)
                else:
                    if not delete:
                        return
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo('Delete','Your student has been Deleted',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root) 
        
    # Reset
    def reset_data(self):
        self.var_mh.set('')
        self.var_ma.set(''),
        self.var_HK.set(''),
        self.var_NH.set(''),
        self.var_TC.set(''),
        self.var_Ma_sv.set(''),
        self.var_Ten_sv.set(''),
        self.var_Gioi_tinh.set(''),
        self.var_Ngay_sinh.set(''),
        self.var_Email.set(''),
        self.var_SDT.set(''),
        self.var_Noi_tam_tru.set(''),
        self.var_Que_quan.set('')
        
    # search data
    def search_data(self):
        if self.var_search.get()=='' or self.var_box_search.get()=='':
            messagebox.showerror('Error','Please select option')
        else:
            try:
                connection = mysql.connector.connect(host = 'localhost',username='root',password='Namtran@2004',database='quan_ly_sv')
                my_curen=connection.cursor()
                my_curen.execute('select * from sinh_vien where '+str(self.var_box_search.get())+" like '%"+str(self.var_search.get())+"%'")
                data=my_curen.fetchall()   
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert('',END,values=i)
                    connection.commit()
                connection.close()             
            except Exception as es:
                messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root)
        
    # open image 
    def open_image(self):
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title='Open Image',filetypes=(('JPG File','*.jpg'),('PNG File','*.png'),('All File','*.*')))
        img=Image.open(fln)
        img_student=img.resize((540,160),Image.ANTIALIAS)
        self.photo_img=ImageTk.PhotoImage(img_student)
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()