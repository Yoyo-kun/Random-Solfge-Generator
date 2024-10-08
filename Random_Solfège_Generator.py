import tkinter as tk
import pygame
import random
import os
import sys

# 初始化pygame
pygame.mixer.init()

def resource_path(relative_path):
    """ 获取资源文件的路径，兼容打包和未打包状态 """
    try:
        # PyInstaller 创建临时文件夹并存储文件
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# 设置每个唱名对应的颜色和音频文件 (钢琴声音)
note_colors = {
    1: 'red',
    2: 'orange',
    3: 'yellow',
    4: 'green',
    5: 'blue',
    6: 'indigo',
    7: 'violet'
}

note_sounds = {
    1: resource_path('Solfège/piano_C4.wav'),
    2: resource_path('Solfège/piano_D4.wav'),
    3: resource_path('Solfège/piano_E4.wav'),
    4: resource_path('Solfège/piano_F4.wav'),
    5: resource_path('Solfège/piano_G4.wav'),
    6: resource_path('Solfège/piano_A4.wav'),
    7: resource_path('Solfège/piano_B4.wav')
}

# 播放指定的唱名声音
def play_sound(note):
    sound_file = note_sounds.get(note)
    if sound_file:
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()

# Fisher-Yates洗牌算法，生成一个更随机的顺序
def fisher_yates_shuffle(lst):
    for i in range(len(lst) - 1, 0, -1):
        j = random.randint(0, i)
        lst[i], lst[j] = lst[j], lst[i]
    return lst

# 随机生成唱名或显示错误信息
def generate_random_notes():
    # 清除之前的结果
    for widget in result_frame.winfo_children():
        widget.destroy()

    notes_input = entry.get()  # 获取用户输入的唱名
    try:
        notes = list(set(map(int, notes_input.split())))

        # 检查是否所有数字都在 1 到 7 之间
        if all(1 <= note <= 7 for note in notes):
            # 固定生成 140 个唱名
            total_count = 140

            # 保证每个唱名出现相同频率，使用Fisher-Yates算法
            full_list = notes * (total_count // len(notes)) + notes[:total_count % len(notes)]
            random_notes = fisher_yates_shuffle(full_list)

            display_random_notes(random_notes)
        else:
            display_error("错误！请输入仅包含 1 到 7 之间的数字。")
    except ValueError:
        display_error("错误！请输入有效的数字，并用空格隔开。")

# 显示随机生成的唱名 (按钮形式)
def display_random_notes(random_notes):
    for i, note in enumerate(random_notes):
        button = tk.Button(result_frame, text=str(note), bg=note_colors[note], width=5, height=2,
                           font=("Arial", 16), command=lambda n=note: play_sound(n))
        button.grid(row=i // 20, column=i % 20, padx=5, pady=5)  # 每行20个键

# 显示错误信息在随机唱名区域
def display_error(message):
    error_label = tk.Label(result_frame, text=message, fg="red", font=("Arial", 14))
    error_label.grid(row=0, column=0, columnspan=15, pady=10)

# 点击钢琴按钮，播放相应的唱名声音
def on_piano_button_click(note):
    play_sound(note)

# 创建GUI
root = tk.Tk()
root.title("唱名生成器")

# 调整窗口大小
root.geometry("1000x800")

# 钢琴区域 (位于顶部)
piano_frame = tk.Frame(root)
piano_frame.pack(pady=10)

for note in range(1, 8):
    button = tk.Button(piano_frame, text=str(note), bg=note_colors[note], width=10, height=4,
                       font=("Arial", 16), command=lambda n=note: on_piano_button_click(n))
    button.grid(row=0, column=note - 1, padx=5, pady=5)

# 输入框和标签
label_entry = tk.Label(root, text="请输入练习的唱名(1-7，用空格隔开):", font=("Arial", 16))
label_entry.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 16), width=30)
entry.pack(pady=5)

# 生成按钮
button_generate = tk.Button(root, text="生成随机唱名", command=generate_random_notes, font=("Arial", 16), width=20)
button_generate.pack(pady=10)

# 显示随机唱名或错误信息的区域 (按钮形式)
result_frame = tk.Frame(root)
result_frame.pack(pady=20)

# 运行主循环
root.mainloop()
