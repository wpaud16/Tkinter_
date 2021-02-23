from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog
import tkinter.messagebox as msg
from PIL import Image
import os

root = Tk()
root.title("project")

def add_file():
    global files
    #사용자에게 여려개의 파일을 여는 걸 물어보는 것 filetypes 는 ("초기 이름", "파일이름.확장자")
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요",\
                                        filetypes=(("jpg","*.jpg"),("PNG 파일","*.png"),("모든 파일","*.*")),\
                                        initialdir=r"C:\Users\82109\OneDrive\바탕 화면\Hobby\결혼고발 컷툰") #처음에 C드라이브 안에서 시작함, r로 하면 그대로 읽어옴
    for file in files:
        list_add_frame.insert(END,file)

def del_file(): #지울 땐 뒤에서부터 지워야 함
    print(list_add_frame.curselection())
    # revers =  원래 값에 영향을 줌/ reversed = 영향을 안주고 새로운 값으로 가져옴
    for index in reversed(list_add_frame.curselection()):
        list_add_frame.delete(index)

#저장경로 함수
def save_line_():
    # 폴더 선택창이 뜸
    global folder
    folder = filedialog.askdirectory()
    if folder == None:
        return
    save_line.delete(0,END)
    save_line.insert(0,folder)

def image_merge():
    global images, width, height, max_wid, tot_hei, result_img, y_offset,img, dest_path,\
    idx, progre


    images = [Image.open(x) for x in list_add_frame.get(0, END)]


    width = [x.size[0] for x in images] #가로 크기 저장
    height = [x.size[1] for x in images] #세로 크기 저장

    max_wid = max(width) #제일 큰놈한테 맞춤
    tot_hei = sum(height) #다 더해서 조절

    result_img = Image.new("RGB", (max_wid, tot_hei), (255,255,255)) #(색 형식, 크기(가로,세로), 배경색)
    y_offset = 0 #y 위치

    for idx, img in enumerate(images):
        result_img.paste(img, (0, y_offset))  # 붙쳐넣기, x,y축
        y_offset += img.size[1]  # height 값 만큼 더 해줌

        progre = (idx +1) / len(images) *100 #실제 % 정보임  1을 더하는 이유는 인덱스가 0으로 시작해서!
        var2.set(progre)
        progress.update()


    dest_path = os.path.join(save_line.get(),"ep_2.jpg")
    result_img.save(dest_path)


def start():
    if list_add_frame.size() == 0 or save_line.get() == 0:
        msg.showwarning("경고","파일을 추가하세요 / 경로를 지정하세요")
        return

    image_merge()

#파일 프레임 ( 파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="파일 추가", command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="선택 삭제", command=del_file)
btn_del_file.pack(side="right")

#스크롤 바
list_frame = Frame(root)
list_frame.pack(fill="x", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

#리스트 프레임
list_add_frame = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_add_frame.pack(side="left", fill="both", expand=True)

scrollbar.config(command=list_add_frame.yview)

#저장경로 프레임
label_frame = LabelFrame(root, text="저장경로")
label_frame.pack(fill="both", padx=5, pady=5)

save_line = Entry(label_frame)
save_line.pack(side="left", fill="x", expand=True, padx=5, pady=5)

serch_btn = Button(label_frame, text="찾아보기", width=10, command=save_line_)
serch_btn.pack(side="right", padx=5, pady=5)

#옵션 프레임
option_frame = LabelFrame(root, text="옵션")
option_frame.pack(fill="x", expand=True, padx=5, pady=5)

label_size = Label(option_frame, text="가로넓이", width=10)
label_size.pack(side="left")

size_value = ["원본유지","1024","800","640"]
size_combo = ttk.Combobox(option_frame, width=10, value=size_value, state="readonly")
size_combo.set(size_value[0]) #또는 size_combo.current(0)
size_combo.pack(side="left")


label_width = Label(option_frame, text="간격", width=10)
label_width.pack(side="left")

width_value = ["없음","좁게","보통","넓게"]
width_combo = ttk.Combobox(option_frame, width=10, value=width_value, state="readonly")
width_combo.set(width_value[0])
width_combo.pack(side="left")


label_format = Label(option_frame, text="포멧", width=10)
label_format.pack(side="left")

format_value = ["png","jpg","bmp"]
format_combo = ttk.Combobox(option_frame, width=10, value=format_value, state="readonly")
format_combo.set(format_value[0])
format_combo.pack(side="left")


#진행상황 프레임
progress_frame = LabelFrame(root, text="진행상황")
progress_frame.pack(fill="x", padx=5, pady=5)

var2 = DoubleVar()
progress = ttk.Progressbar(progress_frame, maximum=100, length=100, variable=var2, mode="determinate")
progress.pack(fill="x", padx=5, pady=5)


#실행 프레임

frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

run_close = Button(frame_run,text="닫기", padx=5, pady=5, width=12, command=root.quit)
run_close.pack(side="right", padx=5, pady=5)

run_start = Button(frame_run,text="시작", padx=5, pady=5, width=12, command=start)
run_start.pack(side="right", padx=5, pady=5)


root.resizable(False,False)
root.mainloop()