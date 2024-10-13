import tkinter as tk
import random
import time
import math  # 导入 math 模块

# 创建主窗口
window = tk.Tk()
window.title("Lucky pot")

# 选项列表
options = ["0u0",
           "77",
           "Louise",
           "0318",
           "1011"]

# 创建一个 Canvas 画布来显示转盘
canvas = tk.Canvas(window, width=300, height=300)
canvas.pack()

# 计算角度
angle = 360 / len(options)

# 绘制转盘
start_angle = 0
for option in options:
    canvas.create_arc((10, 10, 290, 290), start=start_angle, extent=angle, fill="white", outline="black")
    x = 150 + 120 * math.cos(math.radians(start_angle + angle / 2))  # 使用 math.cos 和 math.radians
    y = 150 - 120 * math.sin(math.radians(start_angle + angle / 2))  # 使用 math.sin 和 math.radians
    canvas.create_text(x, y, text=option, anchor=tk.CENTER)
    start_angle += angle

# 显示结果的标签
result_label = tk.Label(window, text="點擊開始", font=("Arial", 18))
result_label.pack(pady=20)

# 旋转转盘函数
def spin_wheel():
    rotations = random.randint(5, 10) * 360  # 随机选择旋转的圈数
    selected_angle = random.randint(0, 360)
    total_rotation = rotations + selected_angle
    duration = 2  # 动画持续时间，秒
    steps = 100  # 动画的帧数

    for i in range(steps):
        angle_now = total_rotation * (i + 1) / steps
        canvas.delete("all")  # 清除画布内容

        # 重新绘制旋转后的转盘
        start_angle = angle_now
        for option in options:
            canvas.create_arc((10, 10, 290, 290), start=start_angle, extent=angle, fill="white", outline="black")
            x = 150 + 120 * math.cos(math.radians(start_angle + angle / 2))  # 使用 math.cos 和 math.radians
            y = 150 - 120 * math.sin(math.radians(start_angle + angle / 2))  # 使用 math.sin 和 math.radians
            canvas.create_text(x, y, text=option, anchor=tk.CENTER)
            start_angle += angle

        window.update()
        time.sleep(duration / steps)

    result_index = int((360 - selected_angle) / angle) % len(options)
    result_label.config(text=f"結果: {options[result_index]}")

# 创建按钮
spin_button = tk.Button(window, text="開始", command=spin_wheel, font=("Arial", 18))
spin_button.pack(pady=20)

# 运行主循环
window.mainloop()

# 等待用户输入，防止窗口关闭
input("按 Enter 键退出程序...")
