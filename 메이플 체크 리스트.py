#!/usr/bin/env python
# coding: utf-8

# In[16]:


import os
notebook_path = os.getcwd()
print(notebook_path)


# In[17]:


import tkinter as tk
from tkinter import messagebox
import tkinter.font as font

def toggle_task(event=None):
    # 토글 기능을 수행하는 함수입니다.
    selected_index = listbox.curselection()
    if selected_index:
        # 선택한 아이템의 내용을 가져옵니다.
        item_status = listbox.get(selected_index)
        if "(완료)" in item_status:
            # 이미 "(완료)" 표시가 있는 경우, 표시를 제거합니다.
            item_status = item_status.replace(" (완료)", "")
        else:
            # "(완료)" 표시가 없는 경우, 표시를 추가합니다.
            item_status += " (완료)"
        # 기존 아이템을 삭제하고 업데이트된 아이템을 삽입합니다.
        listbox.delete(selected_index)
        listbox.insert(selected_index, item_status)

def add_task(event=None):
    # 추가 버튼이 클릭되거나 엔터 키가 눌렸을 때 호출되는 함수입니다.
    task = entry.get()
    if task:
        # 입력된 내용을 리스트 박스에 추가합니다.
        listbox.insert(tk.END, task)
        # 입력 필드를 지웁니다.
        entry.delete(0, tk.END)

def delete_task(event=None):
    # 삭제 버튼이 클릭되거나 마우스 우클릭 이벤트가 발생했을 때 호출되는 함수입니다.
    selected_index = listbox.curselection()
    if selected_index:
        # 선택된 아이템을 삭제합니다.
        listbox.delete(selected_index)

def save_tasks():
    # 저장 버튼이 클릭되었을 때 호출되는 함수입니다.
    tasks = []
    for i in range(listbox.size()):
        # 리스트 박스의 모든 아이템을 가져와서 tasks 리스트에 추가합니다.
        tasks.append(listbox.get(i))
    # tasks 리스트의 내용을 파일에 저장합니다.
    with open("MapleTask.txt", "w") as file:
        file.write("\n".join(tasks))
    # 저장 완료 메시지 박스를 표시합니다.
    messagebox.showinfo("알림", "저장되었습니다.")

def load_tasks():
    # 프로그램 실행 시 저장된 내용을 불러오는 함수입니다.
    try:
        with open("MapleTask.txt", "r") as file:
            # 파일에서 내용을 읽어와서 개별 줄로 분리합니다.
            tasks = file.read().splitlines()
        for task in tasks:
            # 읽어온 각 줄을 리스트 박스에 추가합니다.
            listbox.insert(tk.END, task)
    except FileNotFoundError:
        # 파일이 없는 경우, 아무 작업도 수행하지 않습니다.
        pass

def delete_all_tasks():
    # 전체 삭제 버튼이 클릭되었을 때 호출되는 함수입니다.
    # 경고 메시지 박스를 표시하고 "네" 버튼을 누르면 전체를 삭제합니다.
    answer = messagebox.askquestion("경고", "정말로 전부 삭제하시겠습니까?")
    if answer == "yes":
        # 리스트 박스의 모든 아이템을 삭제합니다.
        listbox.delete(0, tk.END)

def manual_tasks():
    # 설명서 버튼을 클릭하면 호출되는 함수입니다.
    messagebox.showinfo("설명서", "이 프로그램은 메이플 숙제를 관리하는 프로그램입니다.\n\n"
                                  "기능 설명:\n"
                                  "- 추가: '추가' 버튼을 클릭 or Enter\n"
                                  "- 완료: 더블 클릭 or Space\n"
                                  "- 삭제: 우클릭 '삭제' 버튼을 클릭 or Ctrl\n"
                                  "- 전부삭제: 우클릭 '전부 삭제' 버튼 or del\n"
                                  "- 전부해제: 우클릭 '전부 해제' 버튼을 클릭\n"
                                  "- 저장: 숙제 목록이 파일에 저장\n"
                                  "\n이 프로그램은 메이플 유저들의 숙제 관리를 돕기 위해 만들어졌습니다. 즐거운 메이플 라이프 되세요!")
    
def popup_menu(event):
    # 마우스 우클릭 시 팝업 메뉴를 표시하는 함수입니다.
    popup.post(event.x_root, event.y_root)

def on_enter(event):
    # 엔터 키 이벤트를 처리하는 함수입니다.
    add_task()

def clear_completed_tasks():
    # 전부 해제 기능을 수행하는 함수입니다.
    for i in range(listbox.size()):
        # 리스트 박스의 모든 아이템을 가져옵니다.
        item_status = listbox.get(i)
        if "(완료)" in item_status:
            # "(완료)" 표시가 있는 아이템의 경우, 표시를 제거합니다.
            item_status = item_status.replace(" (완료)", "")
            # 아이템을 업데이트합니다.
            listbox.delete(i)
            listbox.insert(i, item_status)

def handle_key_press(event):
    # 키 이벤트를 처리하는 함수입니다.
    if event.keysym == "space":
        toggle_task()
    elif event.keysym == "Delete":
        delete_all_tasks()

    # Ctrl 키를 눌렀을 때 선택된 작업을 삭제합니다.
    if event.keysym == "Control_L" or event.keysym == "Control_R":
        delete_task()

window = tk.Tk()
window.title("메이플 숙제 리스트")
window.geometry("400x500")  # 윈도우의 초기 크기를 설정합니다.

#글자 스타일을 설정합니다.
annotation_font = font.Font(family="Arial", size=12, weight="bold")

listbox = tk.Listbox(window, font=("Arial", 12))
listbox.grid(row=0, column=0, sticky="nsew")

entry = tk.Entry(window, font=("Arial", 12))
entry.grid(row=1, column=0, pady=10)
entry.bind("<Return>", add_task)  # 엔터 키 이벤트를 바인딩합니다.

button_frame = tk.Frame(window)
button_frame.grid(row=2, column=0, pady=10)

manual_button = tk.Button(
    button_frame,
    text="설명서",
    font=("Arial", 12),
    command=manual_tasks
)
manual_button.pack(side=tk.LEFT, padx = 10)

add_button = tk.Button(
    button_frame,
    text="추가",
    font=("Arial", 12),
    command=add_task
)
add_button.pack(side=tk.LEFT, padx = 10)

# delete_button = tk.Button(
#     button_frame,
#     text="삭제",
#     font=("Arial", 12),
#     command=delete_task
# )
# delete_button.pack(side=tk.LEFT)

save_button = tk.Button(
    button_frame,
    text="저장",
    font=("Arial", 12),
    command=save_tasks
)
save_button.pack(side=tk.LEFT, padx = 10)

# delete_all_button = tk.Button(
#     button_frame,
#     text="전부 삭제",
#     font=("Arial", 12),
#     command=delete_all_tasks
# )
# delete_all_button.pack(side=tk.LEFT)

# clear_completed_button = tk.Button(
#     button_frame,
#     text="전부 해제",
#     font=("Arial", 12),
#     command=clear_completed_tasks
# )
# clear_completed_button.pack(side=tk.LEFT)

listbox.bind("<Double-Button-1>", toggle_task)
entry.bind("<Double-Button-1>", toggle_task)  # 입력 필드에 더블 클릭 이벤트를 바인딩합니다.

# 마우스 우클릭 메뉴를 생성합니다.
popup = tk.Menu(window, tearoff=0)
popup.add_command(label="삭제", command=delete_task)
popup.add_command(label="전부 삭제", command=delete_all_tasks)  # 팝업 메뉴에 전체 삭제 기능 추가
popup.add_command(label="전부 해제", command=clear_completed_tasks)  # 팝업 메뉴에 전부 해제 기능 추가
listbox.bind("<Button-3>", popup_menu)  # 리스트 박스에 마우스 우클릭 이벤트를 바인딩합니다.

load_tasks()

window.bind("<KeyPress>", handle_key_press)  # 키 이벤트를 바인딩합니다.

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

window.mainloop()


# In[ ]:




