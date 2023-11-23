import tkinter as tk
import tkinter.messagebox
from collections import Counter
import random


class Game():
    def __init__(self):
        self.x=615  #棋子x坐标
        self.y=520  #棋子y坐标
        self.chess=[]
        self.mark=[]
        self.count = 0
        self.solution = []
        self.guess = []
        self.result = [0, 0]
        self.x_mark=860 #标记的x坐标
        self.y_mark=530
        self.mark_count=0
        self.role=0  #四个判断标记点的行数
        self.canvas=0
        self.window=0
        self.answer=[]
        self.colume=0
        self.x2=645
        self.correct_chess_picture=[]
        self.a=[]
        self.mode=0



    def mastermind(self):
        '''游戏主函数'''
        result = [0, 0]
        dict_solution = Counter(self.solution)
        dict_guess = Counter(self.guess)
        for i in range(len(self.solution)):
            if self.guess[i] == self.solution[i]:
                result[0] += 1
                dict_solution[self.solution[i]] -= 1
                dict_guess[self.guess[i]] -= 1
        for j in range(len(self.solution)):
            if self.guess[j] in self.solution and dict_solution[self.guess[j]] > 0 and dict_guess[self.guess[j]] > 0:
                result[1] += 1
                dict_solution[self.guess[j]] -= 1
                dict_guess[self.guess[j]] -= 1
        print('猜中', result[0], '次，', '伪猜中', result[1], '次')
        self.result = result


    def create_window(self):
        '''创建窗口'''
        self.window = tk.Tk()
        self.window.title('Mastermind')
        self.window.geometry('1920x1080')


    def create_canvas(self):
        '''创建画布'''
        self.bg = tk.PhotoImage(file='bg.png')
        self.canvas = tk.Canvas(self.window,width=1920, height=1080,bg='brown')  # 创建画布
        self.canvas.place(x=0, y=0)  # 放置画布
        self.bg1 = self.canvas.create_image(0, 0, anchor='nw', image=self.bg)
        self.background = tk.PhotoImage(file='board.png')  # 导入背景图像
        self.back_ground = self.canvas.create_image(580, 120,anchor='nw',image=self.background)  # 贴图背景图像
        self.canvas.pack()



    def erase_the_line(self):
        '''擦除改行'''
        self.x=615
        while self.count:
            self.guess.pop()
            self.chess.pop()
            self.count-=1


    def judge(self):
        '''判断'''
        self.count += 1
        print('模式为',self.mode,'count为',self.count)
        if self.mode==1 and self.count==4:

            self.solution=self.guess
            print(self.guess, self.solution)
            self.initialization()
            print(self.guess, self.solution)

        elif self.count== 4:
            self.colume+=1
            self.count = 0
            self.mastermind()
            self.guess=[]
            correct_num=self.result[0]
            false_num=self.result[1]
            while correct_num:
                self.guess_correct()
                correct_num-=1
            while false_num:
                self.guess_false()
                false_num-=1
            self.role+=1
            self.x_mark=860
            self.y_mark=530
            self.y_mark-=self.role*57
            self.mark_count=0

        if self.result[0]==4:
            self.show_answer()
            if tkinter.messagebox.askyesno(title='Mastermind', message='恭喜你，胜利！\n是否重来'):
                self.destroy_window()
                self.run_game()
            else:
                exit()

        elif self.colume == 8:
            self.show_answer()
            if tkinter.messagebox.askyesno(title='MasterMind', message='游戏失败！\n是否重玩'):
                self.destroy_window()
                self.run_game()
            else:
                exit()



    def guess_correct(self):
        '''正确猜测'''
        guess_correct_photo = tk.PhotoImage(file='guess_correct.png')
        self.mark.append(guess_correct_photo)

        if self.mark_count==2:
            self.mark_count=0
            self.x_mark=860
            self.y_mark+=17
            guess_mark = self.canvas.create_image(self.x_mark, self.y_mark, anchor='nw', image=guess_correct_photo)
            self.x_mark += 17
        else:
            guess_mark = self.canvas.create_image(self.x_mark, self.y_mark, anchor='nw', image=guess_correct_photo)
            self.x_mark += 17
        self.mark_count += 1

    def guess_false(self):
        ''' 错误猜测'''
        guess_false_photo = tk.PhotoImage(file='guess_false.png')
        self.mark.append(guess_false_photo)

        if self.mark_count==2:
            self.mark_count=0
            self.x_mark=860
            self.y_mark+=17
            guess_mark = self.canvas.create_image(self.x_mark, self.y_mark, anchor='nw', image=guess_false_photo)
            self.x_mark += 17
        else:
            guess_mark = self.canvas.create_image(self.x_mark, self.y_mark, anchor='nw', image=guess_false_photo)
            self.x_mark += 17
        self.mark_count += 1



    def random_answer(self):
        '''生成随即答案'''
        num_random = []
        answer_random = []
        for num in range(4):
            answer = random.randint(1, 6)
            num_random.append(answer)
        print(num_random)
        for answer in num_random:
            if answer == 1:
                answer_random.append('O')
            if answer == 2:
                answer_random.append('R')
            if answer == 3:
                answer_random.append('Y')
            if answer == 4:
                answer_random.append('G')
            if answer == 5:
                answer_random.append('B')
            if answer == 6:
                answer_random.append('P')
        self.solution=[0,0]
        print(self.solution)
        self.solution=answer_random
        print(self.solution)


    def destroy_window(self):
        '''关闭窗口并重置数据'''
        self.window.destroy()
        self.colume = 0
        self.result[0] = 0
        self.result[1] = 0
        self.x = 615  # 棋子坐标重置
        self.y = 520
        self.chess.clear()
        self.mark.clear()
        self.count = 0
        self.guess.clear()
        self.x_mark = 860  # 标记坐标重置
        self.y_mark = 530
        self.mark_count = 0
        self.role = 0
        self.answer.clear()
        self.mode=0

    def initialization(self):
        '''初始化数据'''
        self.guess=[]
        self.colume = 0
        self.result[0] = 0
        self.result[1] = 0
        self.x = 615  # 棋子坐标重置
        self.y = 520
        self.chess.clear()
        self.mark.clear()
        self.count = 0
        self.x_mark = 860  # 标记坐标重置
        self.y_mark = 530
        self.mark_count = 0
        self.role = 0
        self.mode = 0

    def doublemode(self):
        '''双人模式'''
        if tkinter.messagebox.askokcancel('Choose game mode ', 'Do you select double player mode?'):
            tkinter.messagebox.showinfo('Mastermind', 'You have chosen double player mode\nPlease select answer')
            self.solution.clear()
            self.initialization()
            self.mode = 1

        else:
            tkinter.messagebox.showinfo('Mastermind', 'Double mode has been canceled')



    def run_game(self):
        '''开始游戏'''
        self.random_answer()
        self.create_window()
        self.create_canvas()
        self.create_button()

    def create_button(self):
        '''创建按钮'''
        self.orange_button_photo = tk.PhotoImage(file='orange.png')
        button_orange = tk.Button(self.window, bg='peru', image=self.orange_button_photo, width=52, height=52,
                                  command=self.create_orangeChess).place(x=480, y=600)
        self.red_button_photo = tk.PhotoImage(file='red.png')
        button_red = tk.Button(self.window,bg='peru', image=self.red_button_photo, width=52, height=52,
                               command=self.create_redChess).place(x=580, y=600)
        self.yellow_button_photo = tk.PhotoImage(file='yellow.png')
        button_yellow = tk.Button(self.window,bg='peru', image=self.yellow_button_photo, width=52, height=52,
                                  command=self.create_yellowChess).place(x=680, y=600)
        self.green_button_photo = tk.PhotoImage(file='green.png')
        button_green = tk.Button(self.window, bg='peru',image=self.green_button_photo, width=52, height=52,
                                 command=self.create_greenChess).place(x=780, y=600)
        self.blue_button_photo = tk.PhotoImage(file='blue.png')
        button_blue = tk.Button(self.window,bg='peru', image=self.blue_button_photo, width=52, height=52,
                                command=self.create_blueChess).place(x=880, y=600)
        self.purple_button_photo = tk.PhotoImage(file='purple.png')
        button_purple = tk.Button(self.window, bg='peru', image=self.purple_button_photo, width=52, height=52,
                               command=self.create_purpleChess).place(x=980, y=600)
        self.erase_button = tk.Button(self.window, bg='peru', text='Erase The Line', font=(15), width=15,
                                      height=2,command=self.erase_the_line).place(x=980, y=300)
        self.mode_button = tk.Button(self.window, bg='peru', text='Double Player Mode', font=(15), width=20,
                                      height=2, command=self.doublemode).place(x=980, y=350)


    def show_answer(self):
        '''显示答案'''
        x2=645
        tk.Label(self.window, text='Answer:', font=('Arial', 18), width=6, height=1, bg='peru').place(x=510, y=50)
        for i in range(4):
            if self.solution[i]=='B':
                self.correct_photo = tk.PhotoImage(file='blue.png')
                self.canvas.create_image(self.x2,70, image=self.correct_photo)
                self.correct_chess_picture.append(self.correct_photo)
                self.x2 += 57
            if self.solution[i]=='P':
                self.correct_photo = tk.PhotoImage(file='purple.png')
                self.canvas.create_image(self.x2, 70, image=self.correct_photo)
                self.correct_chess_picture.append(self.correct_photo)
                self.x2 += 57
            if self.solution[i]=='R':
                self.correct_photo = tk.PhotoImage(file='red.png')
                self.canvas.create_image(self.x2, 70, image=self.correct_photo)
                self.correct_chess_picture.append(self.correct_photo)
                self.x2 += 57
            if self.solution[i]=='Y':
                self.correct_photo = tk.PhotoImage(file='yellow.png')
                self.canvas.create_image(self.x2, 70, image=self.correct_photo)
                self.correct_chess_picture.append(self.correct_photo)
                self.x2 += 57
            if self.solution[i]=='G':
                self.correct_photo = tk.PhotoImage(file='green.png')
                self.canvas.create_image(self.x2, 70, image=self.correct_photo)
                self.correct_chess_picture.append(self.correct_photo)
                self.x2 += 57
            if self.solution[i]=='O':
                self.correct_photo = tk.PhotoImage(file='orange.png')
                self.canvas.create_image(self.x2, 70, image=self.correct_photo)
                self.correct_chess_picture.append(self.correct_photo)
                self.x2 += 57#显示争#    #    #
        self.x2 = 645


    def create_redChess(self):
        '''创建红色棋子'''
        self.guess.append('R')
        red_chess_photo = tk.PhotoImage(file='red.png')
        self.chess.append(red_chess_photo)
        red_chess=self.canvas.create_image(self.x,self.y, anchor='nw',image=red_chess_photo)
        self.x += 57
        if self.x==843:
            self.x=615
            self.y -= 57
        self.judge()


    def create_yellowChess(self):
        '''创建黄色棋子'''
        self.guess.append('Y')
        yellow_chess_photo=tk.PhotoImage(file='yellow.png')
        self.chess.append(yellow_chess_photo)
        yellow_chess=self.canvas.create_image(self.x, self.y, anchor='nw',image=yellow_chess_photo)
        self.x += 57
        if self.x==843:
            self.x=615
            self.y -= 57
        self.judge()


    def create_greenChess(self):
        '''创建绿色棋子'''
        self.guess.append('G')
        green_chess_photo=tk.PhotoImage(file='green.png')
        self.chess.append(green_chess_photo)
        green_chess=self.canvas.create_image(self.x,self.y, anchor='nw',image=green_chess_photo)
        self.x += 57
        if self.x==843:
            self.x=615
            self.y -= 57
        self.judge()

    def create_blueChess(self):
        '''创建蓝色棋子'''
        self.guess.append('B')
        blue_chess_photo=tk.PhotoImage(file='blue.png')
        self.chess.append(blue_chess_photo)
        blue_chess=self.canvas.create_image(self.x, self.y, anchor='nw',image=blue_chess_photo)
        self.x += 57
        if self.x==843:
            self.x=615
            self.y -= 57
        self.judge()


    def create_purpleChess(self):
        '''创建紫色棋子'''
        self.guess.append('P')
        purple_chess_photo = tk.PhotoImage(file='purple.png')
        self.chess.append(purple_chess_photo)
        purple_chess=self.canvas.create_image(self.x,self.y, anchor='nw',image=purple_chess_photo)
        self.x += 57
        if self.x==843:
            self.x=615
            self.y -= 57
        self.judge()


    def create_orangeChess(self):
        '''创建橙色棋子'''
        self.guess.append('O')
        orange_chess_photo = tk.PhotoImage(file='orange.png')
        self.chess.append(orange_chess_photo)
        orange_chess=self.canvas.create_image(self.x,self.y, anchor='nw',image=orange_chess_photo)
        self.x += 57
        if self.x==843:
            self.x=615
            self.y -= 57
        self.judge()


if __name__=='__main__':
    interface=Game() #创建对象
    interface.run_game()
    tkinter.messagebox.showinfo(title='MasterMind', message='欢迎游玩MasterMind游戏')
    interface.window.mainloop()
