from tkinter import *
from PIL import ImageTk, Image, ImageDraw


def draw_line(draw, start, end, color="red", width=2):
    draw.line([start, end], fill=color, width=width)


def draw_lines():
    global line_iterator, drawn_plan, draw_li
    drawn_plan = plan_file.copy()
    draw_li = ImageDraw.Draw(drawn_plan)

    for i in range(line_iterator+1):
        draw_line(draw_li, list_of_navigation[i][0], list_of_navigation[i][1])

    global warehouse_plan
    warehouse_plan = ImageTk.PhotoImage(drawn_plan.resize(
        (int(plan_width * k), int(plan_height * k))))
    warehouse_label.config(image=warehouse_plan)

    line_iterator += 1


def draw_rectangle(draw, start, end, color="black"):
    x0, y0 = start
    x1, y1 = end

    if x0 > x1:
        x0, x1 = x1, x0
    if y0 > y1:
        y0, y1 = y1, y0

    start = (x0, y0)
    end = (x1, y1)

    draw.rectangle([start, end], fill=color)


def draw_rectangles():
    global palet_iterator, drawn_plan, draw_re

    drawn_palet = palet_file.copy()
    draw_re = ImageDraw.Draw(drawn_palet)

    for i in range(palet_iterator+1):
        if i == palet_iterator:
            draw_rectangle(
                draw_re, list_of_future_placing[i][0], list_of_future_placing[i][1], "red")
        else:
            draw_rectangle(
                draw_re, list_of_future_placing[i][0], list_of_future_placing[i][1], "black")

    global palet
    palet = ImageTk.PhotoImage(drawn_palet)
    palet_label.config(image=palet)

    palet_iterator += 1


def on_button_reached():
    draw_rectangles()


def on_button_packed():
    global line_iterator
    worker_label.place(x=300+line_iterator, y=300+line_iterator)
    draw_lines()


line_iterator = 0
palet_iterator = 0

list_of_navigation = [[(200+line_iterator, 300+line_iterator), (400+line_iterator, 800+line_iterator)],
                      [(400+line_iterator, 800+line_iterator),
                       (400+line_iterator, 400+line_iterator)],
                      [(400+line_iterator, 400+line_iterator), (100+line_iterator, 200+line_iterator)]]
list_of_future_placing = [[(0+line_iterator, 0+line_iterator), (200+line_iterator, 100+line_iterator)],
                          [(200+line_iterator, 100+line_iterator),
                           (300+line_iterator, 400+line_iterator)],
                          [(150+line_iterator, 250+line_iterator), (10+line_iterator, 20+line_iterator)]]
list_of_past_placing = []


root = Tk()
root.title('Warehouse manager')
window_width = 800
window_height = 700
root.geometry(str(window_width) + 'x' + str(window_height))

button_reached = Button(root, text="I am at package",
                        command=on_button_reached)
button_packed = Button(root, text="Package is packed",
                       command=on_button_packed)
button_undo = Button(root, text="Undo")

plan_file = Image.open("plan.png")
plan_width, plan_height = plan_file.size
k = window_height / plan_height

warehouse_plan = ImageTk.PhotoImage(plan_file.resize(
    (int(plan_width * k), int(plan_height * k))))
warehouse_label = Label(image=warehouse_plan,
                        text="Warehouse plan", compound='bottom')

palet_file = Image.open("palet.png")
palet = ImageTk.PhotoImage(palet_file)
palet_label = Label(image=palet, text="Palet layout", compound='bottom')

worker_file = Image.open("worker.png")
worker = ImageTk.PhotoImage(worker_file)
worker_label = Label(image=worker, text="Worker")


warehouse_label.grid(column=0, rowspan=20)
palet_label.grid(row=0, column=1)
button_reached.grid(row=1, column=1)
button_packed.grid(row=2, column=1)
button_undo.grid(row=3, column=1)

root.mainloop()
