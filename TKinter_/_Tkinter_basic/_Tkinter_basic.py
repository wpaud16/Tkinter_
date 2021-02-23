from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg

root = Tk()

# 제목
root.title("연습")

#사이즈 조정 가로*세로 + x위치 + y위치 위치는 선택사항
# root.geometry("640x600+300+100")

#창 크기 변경 불가 x축(넓이), y축(높이)으로 변경
root.resizable(True,True)

#버튼 생성
button1 = Button(root, text="버튼1").pack()
# button1.pack()

# 버튼 x,y 크기 조절 (여백)
button2 = Button(root, padx=10, pady=5, text="버튼2")
button2.pack()

#버튼 정해진 크기를 설정 (고정)
button3 = Button(root, width=5, height=4, text="버튼3")
button3.pack()

# 이미지를 설정할 수 있음
# photo = PhotoImage(file="주소")
# button4 = Button(root, image = photo)

label1 = Label(root, text="label")
label1.pack()

#버튼을 눌렀을 때 라벨 택스트 내용 변환
def change():
    label1.config(text = "see you") #image 도 가능

button5 = Button(root, text="바뀌는 버튼" , command=change)
button5.pack()

#입력받는 창 생성
text1 = Text(root, width=30, height=5)
text1.pack()
#palceholder 생성
text1.insert(END, "글자를 입력하시오")

#한줄로 입력 받기 위해! enter 가 안 먹음
entry = Entry (root, width =30)
entry.pack()
#placeholder 생성
entry.insert(0, "한줄만")

def buttontext():
    # get 에서 1번째 줄, 0번째 열에서부터 END까지 가져와라는 말
    print(text1.get("1.0",END))
    print(entry.get())
    #내용 삭제
    text1.delete("1.0",END)
    #0번 째에 집어넣었으니 0부터 지운다는 뜻 텍스트(text)는 delete("1.0",END) 이렇게 써야 함
    entry.delete(0,END)

button6 = Button(root, text="텍스트 내용 가져오는 버튼", command=buttontext)
button6.pack()



#리스트 박스 생성 selectmode 는 single 도 있음, 리스트를 몇개 선택할 수 있냐 차이, 높이는 몇개를 보여주냐 차이 0이면 다 보여줌
listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0,"사과")
listbox.insert(1,"딸기")
listbox.insert(2,"배")
listbox.insert(END,"수박") #이렇게 아예 END 로하는 게 나음
listbox.pack()
#몇개가 들어있는지 확인
print(listbox.size())
#항목 확인 0브터 2번째까지 출력
print(listbox.get(0,2))
#선택된 항목 출력, 인덱스 값을 나온다 함수로 만들어서 사용
print(listbox.curselection())

#체크박스
chkvar = IntVar() #chkvar 에 int형으로 저장한다 만약 2개 이상이면 다른 var를 선언해야 함
check = Checkbutton(root, text="오늘하루 보지 않기", variable=chkvar)
#자동 선택 처리
check.select()
check.pack()

def checkbutton():
    print(chkvar.get()) #0이면 체크 안 됐음, 1이면 체크 돼 있음 이래서 int형으로 저장

button6 = Button(root, text="checkbutton", command=checkbutton)
button6.pack()

#라디오 버튼
#하나의 var를 사용 만약 value 가 문자면 StringVar() 해야 함
radio_var = IntVar()
#value는 get을 했을 때 출력되는 값이다. 뮨자, 숫자 다 가능 ,
radio = Radiobutton(root, text="라디오", value=1, variable=radio_var)
mp3 = Radiobutton(root, text="mp3", value=2, variable=radio_var)
handphone = Radiobutton(root, text="핸드폰", value=3, variable=radio_var)
radio.pack()
mp3.pack()
handphone.pack()

#콤보 박스 ttk import 해야 함
value = [str(i)+'일' for i in range(1,32)] #1~31 일까지 출력
#readonly 는 보기에 있는 애만 선택가능
combo = ttk.Combobox(root, height=5, value=value , state = "readonly")
#초기 설정
combo.set("결제일")
combo.pack()

#progressbar == 게이지바 indeterminate 는 결정되지 않은 애는 반복운동하는 애임
progress = ttk.Progressbar(root, maximum=100, mode="indeterminate") #반대는 determinate
progress.start(10) #10ms 마다 참
progress.pack()

var2 = DoubleVar()
progress2 = ttk.Progressbar(root, maximum=100, length=100, variable=var2, mode="determinate") #반대는 determinate
progress2.start(10) #10ms 마다 참
progress2.pack()

#메뉴바
def creat_new():
    print('새파일을 만듭니다')

menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
#add_command 는 하위항목을 생성하는 것
menu_file.add_command(label="new file", command=creat_new)
#disable 은 선택 불가하게 만드는 것
menu_file.add_command(label="new window", state="disable")
#구분선
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit())

#큰 menu 안에 내가 만든 menu_file 이 들어감. (파일, 미리보기) 이런것 처럼 큰 보기를 만듦
menu.add_cascade(label="file", menu=menu_file)

#메뉴 라디오 생성 가능
menu_radio = Menu(menu, tearoff=0)
menu_radio.add_radiobutton(label="python")
menu_radio.add_radiobutton(label="java")
menu_radio.add_radiobutton(label="c++")
menu.add_cascade(label='언어', menu=menu_radio)

root.config(menu=menu)

#메시지 박스
def info():
    msg.showinfo("알림","정상적으로 예매완료")

def warn():
    msg.showwarning("경고","매진됐습니다")

def error():
    msg.showerror("에러","결제 오류")

def cancel():
    msg.showinfo("확인/취소","정말 예매 하시겠습니까?")

def yesnocancel():
    msg.askyesnocancel("예 / 아니요 / 취소","정말 예매 하시겠습니까?")

Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()
Button(root, command=cancel, text="확인/취소").pack()
Button(root, command=yesnocancel, text="예 / 아니오 / 취소").pack() #예 = 1, 아니오 = 0

#스크롤바
frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
#스크롤을 오른쪽에 배치, 스크롤을 y로 꽉 채움 fill=both 는 좌우로 꽉 채움
scrollbar.pack(side="right", fill="y")

#set 이 없으면 스크롤이 계속 올라감
listbox = Listbox(frame, selectmode="extended", height=10 ,yscrollcommand=scrollbar.set)
for i in range(1,32):
    listbox.insert(END, str(i)+'일')
listbox.pack(side='left')

#mapping 하는 거임
scrollbar.config(command=listbox.yview)

#그리드 크기를 조절하려면, width, height 로 조절 
grid_button0 = Button(root, text="0")
grid_button1 = Button(root, text="1")
grid_button2 = Button(root, text="2")
grid_button3 = Button(root, text="3")

#sticky N,E,W,S 동서남북 으로 확장 혹은 붙침/ 버튼간의 간격 조절
grid_button0.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3)
grid_button1.grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady=3)
grid_button2.grid(row=0, column=2, sticky=N+E+W+S, padx=3, pady=3)
grid_button3.grid(row=0, column=3, sticky=N+E+W+S, padx=3, pady=3)

root.mainloop()