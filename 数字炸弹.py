import turtle
import random
import time

s = turtle.Screen()
t = turtle.Pen()

s.setup(800, 800)

def ng(x, y):
    if y >= -350:
        t.penup()
        t.goto(x, y)
        t.pendown()
    elif y < -350:
        t.penup()
        t.goto(x + 300, y + 750)

def game():
    bomb = random.randint(1, 99)
    # print(bomb)
    start = 0
    end = 100
    y = 320
    t.clear()
    ng(-350, 350)
    t.write("游戏过程中可输入quit退出游戏", font=("Arial", 15))
    ng(-350, y)
    y -= 30
    while True:
        people = s.textinput('请输入', '请输入{}到{}之间的数:'.format(start, end))
        if people:
            try:
                people = int(people)
                if people > bomb and people > start and people < end:
                    t.write(f'你输入了{people}，大了', font=("Arial", 15))
                    end = people
                    ng(-350, y)
                    y -= 30
                elif people < bomb and people > start and people < end:
                    t.write(f'你输入了{people}，小了', font=("Arial", 15))
                    start = people
                    ng(-350, y)
                    y -= 30
                elif people == bomb:
                    t.write(f'你输入了{people}，BOOM!你输了', font=("Arial", 15))
                    ng(-350, y)
                    y -= 30
                    break
                else:
                    t.write('请输入符合标准的数字', font=("Arial", 15))
                    ng(-350, y)
                    y -= 30
                    continue
                t.write('等待电脑了输入{}到{}之间的数:'.format(start, end), font=("Arial", 15))
                ng(-350, y)
                y -= 30
                time.sleep(1)
                com = random.randint(start, end)
                t.write('电脑输入了：{}'.format(com), font=("Arial", 15))
                ng(-350, y)
                y -= 30
                if com > bomb:
                    t.write('大了', font=("Arial", 15))
                    end = com
                    ng(-350, y)
                    y -= 30
                elif com < bomb:
                    t.write('小了', font=("Arial", 15))
                    start = com
                    ng(-350, y)
                    y -= 30
                else:
                    t.write('BOOM!!!你赢了！', font=("Arial", 15))
                    ng(-350, y)
                    y -= 30
                    break
            except:        
                if people == 'quit':
                    quit()
                else:
                    t.write('请重新输入', font=("Arial", 15))
                    ng(-350, y)
                    y -= 30
                    continue
        else:
            t.write('请重新输入', font=("Arial", 15))
            ng(-350, y)
            y -= 30
    t.write('按下R键重新开始游戏，按下Q键退出', font=("Arial", 15))

if __name__ == '__main__':
    while True:
        game()
        s.onkeypress(game, 'r')
        s.onkeypress(quit, 'q')
        s.listen()
        turtle.done()
