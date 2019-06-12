#coding:utf-8
from __future__ import division
from __future__ import unicode_literals
import psychopy.visual
import psychopy.event
import psychopy.core
import psychopy.sound
import random
import codecs
import psychopy.gui


param_dict={"Player":"","subj_num":"","gender":["female","male"],"age":"","Internet":["ON","OFF"]}
dlg=psychopy.gui.DlgFromDict(param_dict,title=".. + * *  PLAYER  INFORMATION  * * + ..")
if dlg.OK==False:
    psychopy.core.quit()

win=psychopy.visual.Window(fullscr=True, monitor="testMonitor", units="deg",color="black")
clock=psychopy.core.Clock()

psychopy.event.Mouse(visible=False)

sound=psychopy.sound.Sound("uguisu.wav")
sound2=psychopy.sound.Sound("A",secs=0.3)
sound3=psychopy.sound.Sound("C",secs=0.3)
plz_wait=psychopy.visual.TextStim(win,"他の実験参加者が終わるまで少々お待ちください。\nその間に質問紙への記入をよろしくお願いいたします。",font="ipagothic",pos=(0,0),height=1.0,color="yellow")

fn_PSAP=param_dict["subj_num"] +"_PSAP"+ ".csv"
fn_GO=param_dict["subj_num"] +"_Go"+ ".csv"
fn_IAT=param_dict["subj_num"] +"_IAT"+ ".csv"

datafile_PSAP=codecs.open(fn_PSAP,"w","shift-JIS")
datafile_PSAP.write(param_dict['Player'])
datafile_PSAP.write(",")
datafile_PSAP.write(param_dict["age"])
datafile_PSAP.write(",")
datafile_PSAP.write(param_dict["gender"])
datafile_PSAP.write(",")
datafile_PSAP.write(param_dict["subj_num"])
datafile_PSAP.write("\n\n")
datafile_PSAP.write("a,b,c,RT,rid\n")

datafile_GO=codecs.open(fn_GO,"w","shift-JIS")
datafile_GO.write(param_dict['Player'])
datafile_GO.write(",")
datafile_GO.write(param_dict["age"])
datafile_GO.write(",")
datafile_GO.write(param_dict["gender"])
datafile_GO.write(",")
datafile_GO.write(param_dict["subj_num"])
datafile_GO.write("\n\n")

datafile_IAT=codecs.open(fn_IAT,"w","shift-JIS")
datafile_IAT.write(param_dict['Player'])
datafile_IAT.write(",")
datafile_IAT.write(param_dict["age"])
datafile_IAT.write(",")
datafile_IAT.write(param_dict["gender"])
datafile_IAT.write(",")
datafile_IAT.write(param_dict["subj_num"])
datafile_IAT.write("\n\n")

#==========conection==========
conection=[]
for conect in ["c","o","n"]:
    conection.append(conect)
r=0
schedule=psychopy.visual.TextStim(win,"本日のスケジュール\n\n・ポイント獲得ゲーム一回戦\n・単語分類課題\n・ポイント獲得ゲーム二回戦\n・ボタンを押す？押さない？課題\n・ポイント獲得ゲーム三回戦\n\n・質問紙記入",font="ipagothic",pos=(0,0),height=1.5,color="white")
conect1=psychopy.visual.TextStim(win,text="接続中.",color="white",pos=(0,0),height=1.5,font="Alial")
conect2=psychopy.visual.TextStim(win,text="接続中..",color="white",pos=(0,0),height=1.5,font="Alial")
conect3=psychopy.visual.TextStim(win,text="接続中...",color="white",pos=(0,0),height=1.5,font="Alial")
conected=psychopy.visual.TextStim(win,text="接続完了! (^0^)/",color="white",pos=(0,0),height=1.5,font="Alial")
welcome=psychopy.visual.TextStim(win,text="ようこそ",color="white",pos=(0,5),height=2.0,font="Alial")
welcome2=psychopy.visual.TextStim(win,text=param_dict["Player"],color="Yellow",pos=(0,0),height=2.5,font="Alial")
welcome3=psychopy.visual.TextStim(win,text="さん",color="white",pos=(0,-5),height=2.0,font="Alial")
choose=psychopy.visual.TextStim(win,"相手を選択します",color="white",font="ipagothic",pos=(0,6),height=1.0)
circle=psychopy.visual.ImageStim(win,"circle.png",size=(5,5),pos=(0,-1),ori=r)
point=psychopy.visual.Polygon(win,3,ori=180,size=(1,1),pos=(0,2),fillColor="white")
miss=psychopy.visual.TextStim(win,"割り振り失敗\n再度ルーレットを回してください。",height=1.5,pos=(0,-5),font="ipagothic",color="yellow")
space=psychopy.visual.TextStim(win,"press SPACE key",height=1.0,pos=(0,-7),font="Alial",color="white")
choosed=psychopy.visual.TextStim(win,"相手を選択しました！",color="yellow",font="ipagothic",pos=(0,-1),height=1.5)

schedule.draw()
win.flip()
psychopy.event.waitKeys(keyList=["space"])

for i in conection:
    conect1.draw()
    win.flip()
    psychopy.core.wait(1.0)
    
    conect2.draw()
    win.flip()
    psychopy.core.wait(1.0)
    
    conect3.draw()
    win.flip()
    psychopy.core.wait(1.0)

conect3.draw()
win.flip()
psychopy.core.wait(2.0)

conected.draw()
win.flip()
psychopy.core.wait(3.0)

welcome.draw()
welcome2.draw()
welcome3.draw()
win.flip()
psychopy.core.wait(3.0)

clock.reset()
round=True
while round:
    r=clock.getTime()*600
    circle.setOri(r)
    choose.draw()
    circle.draw()
    point.draw()
    space.draw()
    win.flip()
    
    if psychopy.event.getKeys(keyList=["space"]):
        psychopy.core.wait(2.0)
        
        choose.draw()
        circle.draw()
        point.draw()
        miss.draw()
        space.draw()
        win.flip()
        psychopy.event.waitKeys(keyList=["space"])
        sound3.play()
        round2=True
        while round2:
            r=clock.getTime()*600
            circle.setOri(r)
            choose.draw()
            circle.draw()
            point.draw()
            space.draw()
            win.flip()
            
            if psychopy.event.getKeys(keyList=["space"]):
                psychopy.core.wait(2.0)
                choosed.draw()
                win.flip()
                psychopy.core.wait(3.0)
                round2=False
                round=False

#----------conection----------
sound.play()
#===========PSAP==========

global_clock=psychopy.core.Clock()
clock_rid=psychopy.core.Clock()

Na=0
Nb=0
Nc=0
S=0
Nglobal=0

total=psychopy.visual.TextStim(win,text="Total Score",font="Alial",pos=(0,8),height=1.0)
score=psychopy.visual.TextStim(win,text=S,color="white",font="ipagothic",pos=(0,5),height=2.0)
press=psychopy.visual.TextStim(win,text=Na,color="white",font="ipagothic",pos=(0,0),height=1.5)
ready=psychopy.visual.TextStim(win,text="READY?",font="Alial",pos=(0,0),color="white",height=1.5)
press_space=psychopy.visual.TextStim(win,text="Press SPACE key",pos=(0,-2),color="white",height=1.5)
space=psychopy.visual.TextStim(win,"press SPACE key",pos=(0,-7),height=1.0)
finish=psychopy.visual.TextStim(win,text="Finish",font="Alial",pos=(0,0),color="white",height=2.0)
rect=psychopy.visual.Rect(win,height=2.2,width=5.0,pos=(0,5),lineColor="white",fillColor=None)

which=psychopy.visual.TextStim(win,text="which Bottun?",font="Alial",pos=(0,0),height=2.0,color="white")
A=psychopy.visual.TextStim(win,text="Bottun A",font="Alial",pos=(-5,-6),height=1.0,color="skyblue")
AA=psychopy.visual.TextStim(win,text="Bottun A",font="Alial",pos=(-5,-6),height=1.0,color="white")
B=psychopy.visual.TextStim(win,text="Bottun B",font="Alial",pos=(0,-6),height=1.0,color="salmon")
BB=psychopy.visual.TextStim(win,text="Bottun B",font="Alial",pos=(0,-6),height=1.0,color="white")
C=psychopy.visual.TextStim(win,text="Bottun C",font="Alial",pos=(5,-6),height=1.0,color="yellow")
CC=psychopy.visual.TextStim(win,text="Bottun C",font="Alial",pos=(5,-6),height=1.0,color="white")
Bottun_Rect=psychopy.visual.Rect(win,height=2.5,width=15,pos=(0,-6),fillColor="gray",lineColor="gray")

attack=psychopy.visual.TextStim(win,"相手を攻撃!",font="Alial",pos=(0,-1),height=2.0,color="salmon")
get=psychopy.visual.TextStim(win,"ポイント獲得!",font="Alial",pos=(0,-1),height=2.0,color="skyblue")
protect=psychopy.visual.TextStim(win,"一度のみ守備",font="Alial",pos=(0,-1),height=2.0,color="yellow")
rid=psychopy.visual.TextStim(win,"ポイントを奪われました!",font="Alial",pos=(0,-1),height=2.0,color="white")

psap=psychopy.visual.TextStim(win,"ポイント獲得ゲーム1回戦",font="ipagothic",pos=(0,0),height=1.5,color="white")
inst=psychopy.visual.TextStim(win,"・この課題では，あなたはポイントをより多く獲得することを目的とします。\n・二人一組でゲームに参加し，5分間競い合います。相手はランダムに選ばれます。\n\n・ボタンAを50回押すと，1ポイント獲得できます。\n・ボタンBを10回押すと，相手に攻撃を仕掛け，相手ポイントを減らすことができます。\n　ただし，その回にあなたはポイントを得ることはできません。\n・ボタンCを10回押すと，相手からの攻撃1回分を防ぐ能力を得ます。\n　ただし，あなたがタイミングを指定することはできません。\n\n・一度ボタンを選択すると，押し終えるまで変えることはできません。\n　変えた場合，再度0からの押し直しとなってしまいます。",font="ipagothic",color="white",pos=(0,0),height=1.0)
psychopy.event.Mouse(visible=False)

datafile_PSAP.write(",,,,,一回戦\n")
psap.draw()
win.flip()
psychopy.core.wait(2.0)

inst.draw()
space.draw()
win.flip()
psychopy.event.waitKeys()
sound2.play()

total.draw()
rect.draw()
score.draw()
ready.draw()
press_space.draw()
Bottun_Rect.draw()
AA.draw()
BB.draw()
CC.draw()
win.flip()
psychopy.event.waitKeys(keyList=["space"])

TR=10
global_clock.reset()
clock.reset()
clock_rid.reset()
psychopy.event.getKeys()
while global_clock.getTime()<300:
    Na=0
    Nb=0
    Nc=0
    
    which.draw()
    Bottun_Rect.draw()
    A.draw()
    B.draw()
    C.draw()
    total.draw()
    rect.draw()
    score.draw()
    win.flip()
    
    psychopy.event.getKeys()
    choice=psychopy.event.getKeys(keyList=["escape","num_1","num_2","num_3"])
    for key in choice:
        if "escape" in choice:
            psychopy.core.quit()
        
        elif "num_1" in choice:
            total.draw()
            rect.draw()
            score.draw()
            Bottun_Rect.draw()
            BB.draw()
            CC.draw()
            A.draw()
            win.flip()
            psychopy.core.wait(0.3)
        
        elif "num_2" in choice:
            clock_rid.getTime() - 8
            total.draw()
            rect.draw()
            score.draw()
            Bottun_Rect.draw()
            AA.draw()
            CC.draw()
            B.draw()
            win.flip()
            psychopy.core.wait(0.3)
           
        elif "num_3" in choice:
            total.draw()
            rect.draw()
            score.draw()
            Bottun_Rect.draw()
            AA.draw()
            BB.draw()
            C.draw()
            win.flip()
            psychopy.core.wait(0.3)
            
    psychopy.event.getKeys()
    wait=True
    while wait:

        if clock_rid.getTime() > TR and clock_rid.getTime() < TR + 0.7:
            S -= 1
            score.setText(S)
            rid.draw()
            total.draw()
            rect.draw()
            score.draw()
            Bottun_Rect.draw()
            AA.draw()
            BB.draw()
            CC.draw()
            win.flip()
            clock_rid.reset()
            datafile_PSAP.write(",,,,1\n")
            time_rid=[37,32,40,20,5,60]
            TR=random.choice(time_rid)
            psychopy.core.wait(1.0)
            wait=True
            
        else:
            keys=psychopy.event.getKeys(keyList=["escape","num_1","num_2","num_3"])
            for key in keys:
                if "escape" in keys:
                    psychopy.core.quit()
                    
                elif "num_1" in keys:
                    if Na<50:
                        Nglobal += 1
                        Na += 1
                        Nb = 0
                        Nc = 0
                        press.setText(Na)
                        press.draw()
                        total.draw()
                        rect.draw()
                        score.draw()
                        Bottun_Rect.draw()
                        A.draw()
                        BB.draw()
                        CC.draw()
                        win.flip()
                        wait=True
                    elif Na>=50:
                        Nglobal += 1
                        S += 1
                        score.setText(S)
                        get.draw()
                        total.draw()
                        rect.draw()
                        score.draw()
                        Bottun_Rect.draw()
                        AA.draw()
                        BB.draw()
                        CC.draw()
                        win.flip()
                        datafile_PSAP.write("1,0,0,{},0\n".format(clock.getTime()))
                        psychopy.core.wait(0.7)
                        clock.reset()
                        wait=False
                        break
                    
                elif "num_2" in keys:
                    if Nb<10:
                        Nglobal += 1
                        Nb += 1
                        Na = 0
                        Nc = 0
                        press.setText(Nb)
                        press.draw()
                        total.draw()
                        rect.draw()
                        score.draw()
                        Bottun_Rect.draw()
                        AA.draw()
                        B.draw()
                        CC.draw()
                        win.flip()
                        wait=True
                    elif Nb>=10:
                        Nglobal += 1
                        attack.draw()
                        total.draw()
                        rect.draw()
                        score.draw()
                        Bottun_Rect.draw()
                        AA.draw()
                        BB.draw()
                        CC.draw()
                        win.flip()
                        datafile_PSAP.write("0,1,0,{},0\n".format(clock.getTime()))
                        psychopy.core.wait(0.7)
                        clock.reset()
                        wait=False
                        break
                
                elif "num_3" in keys:
                    if Nc<10:
                        Nglobal += 1
                        Nc += 1
                        Na = 0
                        Nb = 0
                        press.setText(Nc)
                        press.draw()
                        total.draw()
                        rect.draw()
                        score.draw()
                        Bottun_Rect.draw()
                        AA.draw()
                        BB.draw()
                        C.draw()
                        win.flip()
                        wait=True
                    elif Nc>=10:
                        clock_rid.getTime() -10
                        Nglobal += 1
                        protect.draw()
                        total.draw()
                        rect.draw()
                        score.draw()
                        Bottun_Rect.draw()
                        AA.draw()
                        BB.draw()
                        CC.draw()
                        win.flip()
                        datafile_PSAP.write("0,0,1,{},0\n".format(clock.getTime()))
                        psychopy.core.wait(0.7)
                        clock.reset()
                        wait=False
                        break


finish.draw()
total.draw()
rect.draw()
score.draw()
win.flip()
datafile_PSAP.write(",,,,,{},{}\n".format(Nglobal,S))
psychopy.core.wait(2.0)

#----------PSAP----------
sound.play()
plz_wait.draw()
win.flip()
psychopy.event.waitKeys(keyList=["space"])
#==========IAT==========

#設計
#1 自己Mー他者O 
#2 攻撃Aー非攻撃N 
#3pra AM-NO 
#3　AM-NO  
#5 N-A 
#6pra NM-AO 　
#6 NM-AO 
#8 O-M 
#9pra NO-AM 
#9 NO-AM 
#11 A-N 
#12pra AO-NM 
#12 AO-NM 

#条件
conditionsAN=[]
conditionsMO=[]
conditionsIATpra=[]
conditionsIAT=[]
for stim2 in ["罵倒","陰口","排斥","脅迫","介抱","賛美","談笑","握手"]:
    conditionsAN.append(stim2)
for stim1 in [u"自己",u"自分",u"私達",u"学生",u"他者",u"他人",u"彼等",u"教師"]:
    conditionsMO.append(stim1)
conditionsIATpra= conditionsAN + conditionsMO
conditionsIAT=conditionsAN + conditionsMO
conditionsAN *=2
random.shuffle(conditionsAN)
conditionsMO *=2
random.shuffle(conditionsMO)
conditionsIATpra *=1
random.shuffle(conditionsIATpra)
conditionsIAT *=3
random.shuffle(conditionsIAT)

psychopy.event.Mouse(visible=False)

#教示文
ready=psychopy.visual.TextStim(win,text="READY?",font="Alial",color="white",pos=(0,0),height=3.0)
finish=psychopy.visual.TextStim(win,text="Finish!",font="Alial",color="white",pos=(0,0),height=2.0)
press=psychopy.visual.TextStim(win,text="press SPACE key",font="ipagothic",color="white",pos=(0,-3.0),height=1.5)
practice=psychopy.visual.TextStim(win,text="これから練習試行を始めます",font="ipagothic",color="white",pos=(0,0),height=2.0)
experiment=psychopy.visual.TextStim(win,text="これから本試行を始めます\nスペースキーで開始します",font="ipagothic",color="white",pos=(0,0),height=2.0)

instxan=psychopy.visual.TextStim(win,text="XX",font="ipagothic",color="skyblue",pos=(0,0),height=3.0)
instxmo=psychopy.visual.TextStim(win,text="XX",font="ipagothic",color="lightgreen",pos=(0,0),height=3.0)

inst1=psychopy.visual.TextStim(win,text="これから単語分類課題を行っていただきます。",font="ipagothic",color="white",pos=(0,0),height=1.5)
inst2=psychopy.visual.TextStim(win,text="「自己」「自分」「私達」「学生」\n\nの単語が出てきた場合には'e'のキーを押します。",font="ipagothic",color="white",pos=(0,-1),height=1.5)
inst3=psychopy.visual.TextStim(win,text="「他者」「他人」「彼等」「教師」\n\nの単語が出てきた場合には'i'のキーを押します。",font="ipagothic",color="white",pos=(0,-1),height=1.5)

inst5=psychopy.visual.TextStim(win,text="「罵倒」「陰口」「排斥」「脅迫」\n\nの単語が出てきた場合には'e'のキーを押します。",font="ipagothic",color="white",pos=(0,-1),height=1.5)
inst6=psychopy.visual.TextStim(win,text="「介抱」「賛美」「談笑」「握手」\n\nの単語が出てきた場合には'i'のキーを押します。",font="ipagothic",color="white",pos=(0,-1),height=1.5)

inst8=psychopy.visual.TextStim(win,text="「自己」「自分」「私達」「学生」\n「罵倒」「陰口」「排斥」「脅迫」\n\nの単語が出てきた場合には'e'のキーを押します。",font="ipagothic",color="white",pos=(0,-1),height=1.5)
inst9=psychopy.visual.TextStim(win,text="「他者」「他人」「彼等」「教師」\n「介抱」「賛美」「談笑」「握手」\n\nの単語が出てきた場合には'i'のキーを押します。",font="ipagothic",color="white",pos=(0,-1),height=1.5)

inst10=psychopy.visual.TextStim(win,text="「介抱」「賛美」「談笑」「握手」\n\nの単語が出てきた場合には'e'のキーを押します。",font="ipagothic",color="white",pos=(0,-1),height=1.5)
inst11=psychopy.visual.TextStim(win,text="「罵倒」「陰口」「排斥」「脅迫」\n\nの単語が出てきた場合には'i'のキーを押します。",font="ipagothic",color="white",pos=(0,-1),height=1.5)

inst12=psychopy.visual.TextStim(win,text="「自己」「自分」「私達」「学生」\n「介抱」「賛美」「談笑」「握手」\n\nの単語が出てきた場合には'e'のキーを押します。",font="ipagothic",color="white",pos=(0,-1),height=1.5)
inst13=psychopy.visual.TextStim(win,text="「他者」「他人」「彼等」「教師」\n「罵倒」「陰口」「排斥」「脅迫」\n\nの単語が出てきた場合には'i'のキーを押します。",font="ipagothic",color="white",pos=(0,-1),height=1.5)

inst14=psychopy.visual.TextStim(win,text="「他者」「他人」「彼等」「教師」\n\nの単語が出てきた場合には'e'のキーを押します。",font="ipagothic",color="white",pos=(0,-1),height=1.5)
inst15=psychopy.visual.TextStim(win,text="「自己」「自分」「私達」「学生」\n\nの単語が出てきた場合には'i'のキーを押します。",font="ipagothic",color="white",pos=(0,-1),height=1.5)

inst16=psychopy.visual.TextStim(win,text="「他者」「他人」「彼等」「教師」\n「介抱」「賛美」「談笑」「握手」\n\nの単語が出てきた場合には'e'のキーを押します。",font="ipagothic",color="white",pos=(0,-1),height=1.5)
inst17=psychopy.visual.TextStim(win,text="「自己」「自分」「私達」「学生」\n「罵倒」「陰口」「排斥」「脅迫」\n\nの単語が出てきた場合には'i'のキーを押します。",font="ipagothic",color="white",pos=(0,-1),height=1.5)

inst18=psychopy.visual.TextStim(win,text="「他者」「他人」「彼等」「教師」\n「罵倒」「陰口」「排斥」「脅迫」\n\nの単語が出てきた場合には'e'のキーを押します。",font="ipagothic",color="white",pos=(0,-1),height=1.5)
inst19=psychopy.visual.TextStim(win,text="「自己」「自分」「私達」「学生」\n「介抱」「賛美」「談笑」「握手」\n\nの単語が出てきた場合には'i'のキーを押します。",font="ipagothic",color="white",pos=(0,-1),height=1.5)


#刺激 及び 対概念
#------------------------------
stim01=psychopy.visual.TextStim(win,font="ipagothic",color="lightgreen",pos=(0,0),height=3.0)
stim02=psychopy.visual.TextStim(win,font="ipagothic",color="skyblue",pos=(0,0),height=3.0)

agg=psychopy.visual.TextStim(win,text="攻撃的",font="ipagothic",color="skyblue",pos=(-10,10),height=2.7)
agg2=psychopy.visual.TextStim(win,text="攻撃的",font="ipagothic",color="skyblue",pos=(10,10),height=2.7)
non=psychopy.visual.TextStim(win,text="非攻撃的",font="ipagothic",color="skyblue",pos=(10,10),height=2.7)
non2=psychopy.visual.TextStim(win,text="非攻撃的", font="ipagothic",color="skyblue",pos=(-10,10),height=2.7)

me=psychopy.visual.TextStim(win,text="自己",font="ipagothic",color="lightgreen",pos=(-10,6),height=2.7)
oth=psychopy.visual.TextStim(win,text="他者",font="ipagothic",color="lightgreen",pos=(10,6),height=2.7)
me2=psychopy.visual.TextStim(win,text="自己",font="ipagothic",color="lightgreen",pos=(10,6),height=2.7)
oth2=psychopy.visual.TextStim(win,text="他者",font="ipagothic",color="lightgreen",pos=(-10,6),height=2.7)

fix=psychopy.visual.TextStim(win,text="+",font="ipagothic",color="white",pos=(0,0),height=3.0)
false=psychopy.visual.TextStim(win,text="×",font="ipagothic",color="red",pos=(0,0),height=3.0)
#--------------------------------

IAT=psychopy.visual.TextStim(win,"単語分類課題",font="ipagothic",pos=(0,0),height=1.5)
#------------------------------------------------------------------------
                     #実験開始
#------------------------------------------------------------------------

#第1セッション
datafile_IAT.write("1st section(MO)\n")

IAT.draw()
win.flip()
psychopy.core.wait(2.0)

inst1.draw()
press.draw()
win.flip()
psychopy.event.waitKeys(keyList=['space'])

inst2.draw()
me.draw()
oth.draw()
win.flip()
psychopy.event.waitKeys(keyList=["e"])

inst3.draw()
me.draw()
oth.draw()
win.flip()
psychopy.event.waitKeys(keyList=["i"])

instxmo.draw()
press.draw()
me.draw()
oth.draw()
win.flip()
psychopy.event.waitKeys(keyList=["space"])

me.draw()
oth.draw()
ready.draw()
press.draw()
win.flip()
psychopy.event.waitKeys(keyList=["space"])

me.draw()
oth.draw()
fix.draw()
win.flip()
psychopy.core.wait(1.0)

for conditionMO in conditionsMO:
    
    stim1=conditionMO         
    stim01.setText(stim1)
    
    waiting_keypress=True
    psychopy.event.getKeys()
    clock.reset()
    while waiting_keypress:
        if conditionMO in (u"自己",u"自分",u"私達",u"学生"):
            correct_key="e"
        else:
            correct_key="i"
            
        keys=psychopy.event.getKeys(keyList=["e","i","escape"])  
        
        for key in keys:                                                 
            if "escape" in keys:
                datafile_IAT.close()
                psychopy.core.quit()
            elif correct_key in keys:
                datafile_IAT.write(",,{:.5f},{}\n".format(clock.getTime(),stim1))
                datafile_IAT.flush()
                waiting_keypress=False
                break
            else:
                datafile_IAT.write("{},{:.5f}".format(key,clock.getTime()))
                datafile_IAT.flush()
                me.draw()
                oth.draw()
                false.draw()
                win.flip()
                psychopy.core.wait(0.3)
                waiting_keypress=True
                
        me.draw()
        oth.draw()
        stim01.draw()
        win.flip()
        
    me.draw()
    oth.draw()
    fix.draw()
    win.flip()
    psychopy.core.wait(0.25)

sound.play()
plz_wait.draw()
win.flip()
psychopy.event.waitKeys(keyList=["space"])

#第2セッション
datafile_IAT.write("2nd section(AN)\n")

inst5.draw()
agg.draw()
non.draw()
win.flip()
psychopy.event.waitKeys(keyList=['e'])

inst6.draw()
agg.draw()
non.draw()
win.flip()
psychopy.event.waitKeys(keyList=["i"])

instxan.draw()
press.draw()
agg.draw()
non.draw()
win.flip()
psychopy.event.waitKeys(keyList=["space"])

agg.draw()
non.draw()
ready.draw()
press.draw()
win.flip()
psychopy.event.waitKeys(keyList=["space"])

agg.draw()
non.draw()
fix.draw()
win.flip()
psychopy.core.wait(1.5)

for conditionAN in conditionsAN:
    
    stim2=conditionAN         
    stim02.setText(stim2)
    
    waiting_keypress=True
    psychopy.event.getKeys()
    clock.reset()
    while waiting_keypress:
        if conditionAN in ("罵倒","陰口","排斥","脅迫"):
            correct_key="e"
        else:
            correct_key="i"
            
        keys=psychopy.event.getKeys(keyList=["e","i","escape"])  
        for key in keys:                                                 
            if "escape" in keys:
                datafile_IAT.close()
                psychopy.core.quit()
            elif correct_key in keys:
                datafile_IAT.write(",,{:.5f},{}\n".format(clock.getTime(),stim2))
                datafile_IAT.flush()
                waiting_keypress=False
                break
            else:
                datafile_IAT.write("{},{:.5f}".format(key,clock.getTime()))
                datafile_IAT.flush()
                agg.draw()
                non.draw()
                false.draw()
                win.flip()
                psychopy.core.wait(0.3)
                waiting_keypress=True
        agg.draw()
        non.draw()
        stim02.draw()
        win.flip()
    agg.draw()
    non.draw()
    fix.draw()
    win.flip()
    psychopy.core.wait(0.25)

sound.play()
plz_wait.draw()
win.flip()
psychopy.event.waitKeys(keyList=["space"])

#第3練習
datafile_IAT.write("practice for 3rd\n")

inst8.draw()
non.draw()
agg.draw()
me.draw()
oth.draw()
win.flip()
psychopy.event.waitKeys(keyList=["e"])

inst9.draw()
non.draw()
agg.draw()
me.draw()
oth.draw()
win.flip()
psychopy.event.waitKeys(keyList=["i"])

agg.draw()
non.draw()
oth.draw()
me.draw()
practice.draw()
press.draw()
win.flip()
psychopy.event.waitKeys(keyList=["space"])

agg.draw()
non.draw()
oth.draw()
me.draw()
fix.draw()
win.flip()
psychopy.core.wait(1.5)

for conditionIATpra in conditionsIATpra:
    
    stim1=conditionIATpra
    stim2=conditionIATpra
    stim01.setText(stim1)
    stim02.setText(stim2)
    
    waiting_keypress=True
    psychopy.event.getKeys()
    clock.reset()
    while waiting_keypress:
        if conditionIATpra in [u"罵倒","陰口","排斥","脅迫",u"自己",u"自分",u"私達",u"学生"]:
            correct_key="e"
        else:
            correct_key="i"
            
        keys=psychopy.event.getKeys(keyList=["e","i","escape"])  
        for key in keys:                                                 
            if "escape" in keys:
                datafile_IAT.close()
                psychopy.core.quit()
            elif correct_key in keys:
                datafile_IAT.write(",,{:.5f},{}\n".format(clock.getTime(),stim1 or stim2))
                datafile_IAT.flush()
                waiting_keypress=False
                break
            else:
                datafile_IAT.write("{},{:.5f}".format(key,clock.getTime()))
                datafile_IAT.flush()
                me.draw()
                oth.draw()
                agg.draw()
                non.draw()
                false.draw()
                win.flip()
                psychopy.core.wait(0.3)
                waiting_keypress=True
        me.draw()
        oth.draw()
        agg.draw()
        non.draw()
        if conditionIATpra in [u"自己",u"自分",u"私達",u"学生",u"他者",u"他人",u"彼等",u"教師"]:
            stim01.draw()
        else:
            stim02.draw()
        win.flip()
        
    me.draw()
    oth.draw()
    agg.draw()
    non.draw()
    fix.draw()
    win.flip()
    psychopy.core.wait(0.25)
#第3セッション
datafile_IAT.write("3rd section(AMNO)\n")

agg.draw()
non.draw()
me.draw()
oth.draw()
experiment.draw()
press.draw()
win.flip()
psychopy.event.waitKeys(keyList=["space"])

agg.draw()
non.draw()
me.draw()
oth.draw()
fix.draw()
win.flip()
psychopy.core.wait(1.5)

for conditionIAT in conditionsIAT:
    
    stim1=conditionIAT
    stim2=conditionIAT
    stim01.setText(stim1)
    stim02.setText(stim2)
    
    waiting_keypress=True
    psychopy.event.getKeys()
    clock.reset()
    while waiting_keypress:
        if conditionIAT in [u"罵倒","陰口","排斥","脅迫",u"自己",u"自分",u"私達",u"学生"]:
            correct_key="e"
        else:
            correct_key="i"
            
        keys=psychopy.event.getKeys(keyList=["e","i","escape"])  
        for key in keys:                                                 
            if "escape" in keys:
                datafile_IAT.close()
                psychopy.core.quit()
            elif correct_key in keys:
                datafile_IAT.write(",,{:.5f},{}\n".format(clock.getTime(),stim1 or stim2))
                datafile_IAT.flush()
                waiting_keypress=False
                break
            else:
                datafile_IAT.write("{},{:.5f}".format(key,clock.getTime()))
                datafile_IAT.flush()
                me.draw()
                oth.draw()
                agg.draw()
                non.draw()
                false.draw()
                win.flip()
                psychopy.core.wait(0.3)
                waiting_keypress=True
        
        me.draw()
        oth.draw()
        agg.draw()
        non.draw()
        if conditionIAT in [u"自己",u"自分",u"私達",u"学生",u"他者",u"他人",U"彼等",u"教師"]:
            stim01.draw()
        else:
            stim02.draw()
        win.flip()
        
    me.draw()
    oth.draw()
    agg.draw()
    non.draw()
    fix.draw()
    win.flip()
    psychopy.core.wait(0.25)

sound.play()
plz_wait.draw()
win.flip()
psychopy.event.waitKeys(keyList=["space"])

# section 4
datafile_IAT.write("4th section(NA)\n")

inst10.draw()
agg2.draw()
non2.draw()
win.flip()
psychopy.event.waitKeys(keyList=["e"])

inst11.draw()
agg2.draw()
non2.draw()
win.flip()
psychopy.event.waitKeys(keyList=["i"])

ready.draw()
press.draw()
agg2.draw()
non2.draw()
win.flip()
psychopy.event.waitKeys(keyList=["space"])

fix.draw()
agg2.draw()
non2.draw()
win.flip()
psychopy.core.wait(1.5)

for conditionAN in conditionsAN:
    
    stim2=conditionAN
    stim02.setText(stim2)
    
    waiting_keypress=True
    psychopy.event.getKeys()
    clock.reset()
    while waiting_keypress:
        if conditionAN in ("談笑","握手","賛美","介抱"):
            correct_key="e"
        else:
            correct_key="i"
        
        keys=psychopy.event.getKeys(keyList=["e","i","escape"])
        for key in keys:
            if "escape" in keys:
                datafile_IAT.close()
                psychopy.core.quit()
            elif correct_key in keys:
                datafile_IAT.write(",,{:.5f},{}\n".format(clock.getTime(),stim2))
                datafile_IAT.flush()
                waiting_keypress=False
                break
            else:
                datafile_IAT.write("{},{:.5f}".format(key,clock.getTime()))
                datafile_IAT.flush()
                agg2.draw()
                non2.draw()
                false.draw()
                win.flip()
                psychopy.core.wait(0.3)
                waiting_keypress=True
        agg2.draw()
        non2.draw()
        stim02.draw()
        win.flip()
    agg2.draw()
    non2.draw()
    fix.draw()
    win.flip()
    psychopy.core.wait(0.25)

#section 5 pra (MN-AO)
datafile_IAT.write("5th section pra (MNAO)\n")

inst12.draw()
me.draw()
oth.draw()
agg2.draw()
non2.draw()
win.flip()
psychopy.event.waitKeys(keyList=["e"])

inst13.draw()
oth.draw()
me.draw()
agg2.draw()
non2.draw()
win.flip()
psychopy.event.waitKeys(keyList=["i"])

practice.draw()
press.draw()
oth.draw()
me.draw()
agg2.draw()
non2.draw()
win.flip()
psychopy.event.waitKeys(keyList=["space"])

fix.draw()
oth.draw()
me.draw()
agg2.draw()
non2.draw()
win.flip()
psychopy.core.wait(1.5)

for conditionIATpra in conditionsIATpra:
    stim1=conditionIATpra
    stim2=conditionIATpra
    stim01.setText(stim1)
    stim02.setText(stim2)
    
    waiting_keypress=True
    psychopy.event.getKeys()
    clock.reset()
    while waiting_keypress:
        if conditionIATpra in ["他者","他人","彼等","教師","罵倒","脅迫","陰口","排斥"]:
            correct_key="i"
        else:
            correct_key="e"
        keys=psychopy.event.getKeys(keyList=["e","i","escape"])
        for key in keys:
            if "escape" in keys:
                datafile_IAT.close()
                psychopy.core.quit()
            elif correct_key in keys:
                datafile_IAT.write(",,{:.5f},{}\n".format(clock.getTime(),stim1 or stim2))
                datafile_IAT.flush()
                waiting_keypress=False
                break
            else:
                datafile_IAT.write("{},{:.5f}".format(key,clock.getTime()))
                datafile_IAT.flush()
                me.draw()
                oth.draw()
                agg2.draw()
                non2.draw()
                false.draw()
                win.flip()
                psychopy.core.wait(0.3)
                waiting_keypress=True
        me.draw()
        oth.draw()
        agg2.draw()
        non2.draw()
        if conditionIATpra in ["自己","自分","学生","私達","他者","他人","彼等","教師"]:
            stim01.draw()
        else:
            stim02.draw()
        win.flip()
        
    me.draw()
    oth.draw()
    agg2.draw()
    non2.draw()
    fix.draw()
    win.flip()
    psychopy.core.wait(0.25)
    
#section 5 (NM-AO)
datafile_IAT.write("5th section (NMAO)\n")

experiment.draw()
press.draw()
me.draw()
oth.draw()
agg2.draw()
non2.draw()
win.flip()
psychopy.event.waitKeys(keyList=["space"])
    
agg2.draw()
non2.draw()
me.draw()
oth.draw()
fix.draw()
win.flip()
psychopy.core.wait(1.5)

for conditionIAT in conditionsIAT:
    
    stim1=conditionIAT
    stim2=conditionIAT
    stim01.setText(stim1)
    stim02.setText(stim2)
    
    waiting_keypress=True
    psychopy.event.getKeys()
    clock.reset()
    while waiting_keypress:
        if conditionIAT in ["他者","他人","彼等","教師","罵倒","陰口","排斥","脅迫"]:
            correct_key="i"
        else:
            correct_key="e"
        
        keys=psychopy.event.getKeys(keyList=["e","i","escape"])
        for key in keys:
            if "escape" in keys:
                datafile_IAT.close()
                psychopy.core.quit()
            elif correct_key in keys:
                datafile_IAT.write(",,{:.5f},{}\n".format(clock.getTime(),stim1 or stim2))
                datafile_IAT.flush()
                waiting_keypress=False
                break
            else:
                datafile_IAT.write("{},{:.5f}".format(key,clock.getTime()))
                datafile_IAT.flush()
                me.draw()
                oth.draw()
                agg2.draw()
                non2.draw()
                false.draw()
                win.flip()
                psychopy.core.wait(0.3)
                waiting_keypress=True
        me.draw()
        oth.draw()
        agg2.draw()
        non2.draw()
        if conditionIAT in ["自己","自分","私達","学生","他者","他人","彼等","教師"]:
            stim01.draw()
        else:
            stim02.draw()
        win.flip()
    
    me.draw()
    oth.draw()
    agg2.draw()
    non2.draw()
    fix.draw()
    win.flip()
    psychopy.core.wait(0.25)

#section 6 OM
datafile_IAT.write("6th section(OM)\n")

inst14.draw()
me2.draw()
oth2.draw()
win.flip()
psychopy.event.waitKeys(keyList=["e"])

inst15.draw()
me2.draw()
oth2.draw()
win.flip()
psychopy.event.waitKeys(keyList=["i"])

ready.draw()
press.draw()
me2.draw()
oth2.draw()
win.flip()
psychopy.event.waitKeys(keyList=["space"])

fix.draw()
me2.draw()
oth2.draw()
win.flip()
psychopy.core.wait(1.5)

for conditionMO in conditionsMO:
    stim1=conditionMO
    stim01.setText(stim1)
    
    waiting_keypress=True
    psychopy.event.getKeys()
    clock.reset()
    while waiting_keypress:
        if conditionMO in ["他者","他人","彼等","教師"]:
            correct="e"
        else:
            correct="i"
        keys=psychopy.event.getKeys(keyList=["e","i","escape"])
        for key in keys:
            if "escape" in keys:
                datafile_IAT.close()
                psychopy.core.quit()
            elif correct in keys:
                datafile_IAT.write(",,{:.5f},{}\n".format(clock.getTime(),stim1))
                datafile_IAT.flush()
                waiting_keypress=False
                break
            else:
                datafile_IAT.write("{},{:.5f}".format(key,clock.getTime()))
                datafile_IAT.flush()
                false.draw()
                me2.draw()
                oth2.draw()
                win.flip()
                psychopy.core.wait(0.3)
                waiting_keypress=True
        me2.draw()
        oth2.draw()
        stim01.draw()
        win.flip()
        
    me2.draw()
    oth2.draw()
    fix.draw()
    win.flip()
    psychopy.core.wait(0.25)

#section 7 pra NOAM
datafile_IAT.write("7th pra section(NOAM)\n")

inst16.draw()
me2.draw()
oth2.draw()
agg2.draw()
non2.draw()
win.flip()
psychopy.event.waitKeys(keyList=["e"])

inst17.draw()
me2.draw()
oth2.draw()
agg2.draw()
non2.draw()
win.flip()
psychopy.event.waitKeys(keyList=["i"])

practice.draw()
press.draw()
me2.draw()
oth2.draw()
agg2.draw()
non2.draw()
win.flip()
psychopy.event.waitKeys(keyList=["space"])

fix.draw()
me2.draw()
oth2.draw()
agg2.draw()
non2.draw()
win.flip()
psychopy.core.wait(1.5)

for conditionIATpra in conditionsIATpra:
    
    stim1=conditionIATpra
    stim2=conditionIATpra
    stim01.setText(stim1)
    stim02.setText(stim2)
    
    wait=True
    psychopy.event.getKeys()
    clock.reset()
    while wait:
        if conditionIATpra in ["自己","自分","私達","学生","罵倒","陰口","排斥","脅迫"]:
            correct="i"
        else:
            correct="e"
        keys=psychopy.event.getKeys(keyList=["e","i","escape"])
        for key in keys:
            if "escape" in keys:
                datafile_IAT.close()
                psychopy.core.quit()
            elif correct in keys:
                datafile_IAT.write(",,{:.5f},{}\n".format(clock.getTime(),stim1 or stim2))
                datafile_IAT.flush()
                wait=False
                break
            else:
                datafile_IAT.write("{},{:.5f}".format(key,clock.getTime()))
                datafile_IAT.flush()
                false.draw()
                me2.draw()
                oth2.draw()
                agg2.draw()
                non2.draw()
                win.flip()
                wait=True
                psychopy.core.wait(0.3)
        me2.draw()
        oth2.draw()
        agg2.draw()
        non2.draw()
        if conditionIATpra in["自己","自分","私達","学生","他者","他人","彼等","教師"]:
            stim01.draw()
        else:
            stim02.draw()
        win.flip()
    
    me2.draw()
    oth2.draw()
    agg2.draw()
    non2.draw()
    fix.draw()
    win.flip()
    psychopy.core.wait(0.25)
    

#section 7 NO-AM
datafile_IAT.write("7th section(NOAM)\n")

experiment.draw()
press.draw()
me2.draw()
oth2.draw()
agg2.draw()
non2.draw()
win.flip()
psychopy.event.waitKeys(keyList=["space"])

fix.draw()
me2.draw()
oth2.draw()
agg2.draw()
non2.draw()
win.flip()
psychopy.core.wait(1.5)

for conditionIAT in conditionsIAT:
    
    stim1=conditionIAT
    stim2=conditionIAT
    stim01.setText(stim1)
    stim02.setText(stim2)
    
    wait=True
    psychopy.event.getKeys()
    clock.reset()
    while wait:
        if conditionIAT in ["自分","自己","私達","学生","罵倒","陰口","排斥","脅迫"]:
            correct="i"
        else:
            correct="e"
        keys=psychopy.event.getKeys(keyList=["e","i","escape"])
        for key in keys:
            if "escape" in keys:
                datafile_IAT.close()
                psychopy.core.quit()
            elif correct in keys:
                datafile_IAT.write(",,{:.5f},{}\n".format(clock.getTime(),stim1 or stim2))
                datafile_IAT.flush()
                wait=False
                break
            else:
                datafile_IAT.write("{},{:.5f}".format(key,clock.getTime()))
                datafile_IAT.flush()
                false.draw()
                me2.draw()
                oth2.draw()
                agg2.draw()
                non2.draw()
                win.flip()
                psychopy.core.wait(0.3)
        me2.draw()
        oth2.draw()
        agg2.draw()
        non2.draw()
        if conditionIAT in ["自己","自分","私達","学生","他者","他人","彼等","教師"]:
            stim01.draw()
        else:
            stim02.draw()
        win.flip()
    
    me2.draw()
    oth2.draw()
    agg2.draw()
    non2.draw()
    fix.draw()
    win.flip()
    psychopy.core.wait(0.25)

# section 8 A-N
datafile_IAT.write("8th section(AN)\n")

inst5.draw()
agg.draw()
non.draw()
win.flip()
psychopy.event.waitKeys(keyList=["e"])

inst6.draw()
agg.draw()
non.draw()
win.flip()
psychopy.event.waitKeys(keyList=["i"])

ready.draw()
press.draw()
agg.draw()
non.draw()
win.flip()
psychopy.event.waitKeys(keyList=["space"])

fix.draw()
agg.draw()
non.draw()
win.flip()
psychopy.core.wait(1.5)

for conditionAN in conditionsAN:
    
    stim2=conditionAN
    stim02.setText(stim2)
    
    wait=True
    psychopy.event.getKeys()
    clock.reset()
    while wait:
        if conditionAN in ["罵倒","排斥","陰口","脅迫"]:
            correct="e"
        else:
            correct="i"
        
        keys=psychopy.event.getKeys(keyList=["e","i","escape"])
        for key in keys:
            if "escape" in keys:
                datafile_IAT.close()
                psychopy.core.quit()
            elif correct in keys:
                datafile_IAT.write(",,{:.5f},{}\n".format(clock.getTime(),stim2))
                datafile_IAT.flush()
                wait=False
                break
            else:
                datafile_IAT.write("{},{:.5f}".format(key,clock.getTime()))
                datafile_IAT.flush()
                agg.draw()
                non.draw()
                false.draw()
                win.flip()
                psychopy.core.wait(0.3)
        agg.draw()
        non.draw()
        stim02.draw()
        win.flip()
    agg.draw()
    non.draw()
    fix.draw()
    win.flip()
    psychopy.core.wait(0.25)

#section 9 pra (AO-NM)
datafile_IAT.write("9th section pra (AONM)\n")

inst18.draw()
agg.draw()
non.draw()
me2.draw()
oth2.draw()
win.flip()
psychopy.event.waitKeys(keyList=["e"])

inst19.draw()
agg.draw()
non.draw()
me2.draw()
oth2.draw()
win.flip()
psychopy.event.waitKeys(keyList=["i"])

practice.draw()
press.draw()
agg.draw()
non.draw()
me2.draw()
oth2.draw()
win.flip()
psychopy.event.waitKeys(keyList=["space"])

fix.draw()
agg.draw()
non.draw()
me2.draw()
oth2.draw()
win.flip()
psychopy.core.wait(1.5)

for conditionIATpra in conditionsIATpra:
    
    stim1=conditionIATpra
    stim2=conditionIATpra
    stim01.setText(stim1)
    stim02.setText(stim2)
    
    wait=True
    psychopy.event.getKeys()
    clock.reset()
    while wait:
        if conditionIATpra in ["他者","他人","彼等","教師","罵倒","陰口","脅迫","排斥"]:
            correct="e"
        else:
            correct="i"
        keys=psychopy.event.getKeys(keyList=["e","i","escape"])
        for key in keys:
            if "escape" in keys:
                datafile_IAT.close()
                psychopy.core.quit()
            elif correct in keys:
                datafile_IAT.write(",,{:.5f},{}\n".format(clock.getTime(),stim1 or stim2))
                datafile_IAT.flush()
                wait=False
                break
            else:
                datafile_IAT.write("{},{:.5f}".format(key,clock.getTime()))
                datafile_IAT.flush()
                false.draw()
                me2.draw()
                oth2.draw()
                agg.draw()
                non.draw()
                win.flip()
                psychopy.core.wait(0.3)
        me2.draw()
        oth2.draw()
        agg.draw()
        non.draw()
        if conditionIATpra in ["自己","自分","私達","学生","他者","他人","彼等","教師"]:
            stim01.draw()
        else:
            stim02.draw()
        win.flip()
    me2.draw()
    oth2.draw()
    agg.draw()
    non.draw()
    fix.draw()
    win.flip()
    psychopy.core.wait(0.25)

#section 9 (AO-NM)
datafile_IAT.write("9th section(AONM)\n")

experiment.draw()
press.draw()
agg.draw()
non.draw()
me2.draw()
oth2.draw()
win.flip()
psychopy.event.waitKeys(keyList=["space"])

fix.draw()
agg.draw()
non.draw()
me2.draw()
oth2.draw()
win.flip()
psychopy.core.wait(1.5)

for conditionIAT in conditionsIAT:
    
    stim1=conditionIAT
    stim2=conditionIAT
    stim01.setText(stim1)
    stim02.setText(stim2)
    
    wait=True
    psychopy.event.getKeys()
    clock.reset()
    while wait:
        if conditionIAT in ["他者","他人","彼等","教師","罵倒","陰口","排斥","脅迫"]:
            correct="e"
        else:
            correct="i"
        keys=psychopy.event.getKeys(keyList=["e","i","escape"])
        for key in keys:
            if "escape" in keys:
                datafile_IAT.close()
                psychopy.core.quit()
            elif correct in keys:
                datafile_IAT.write(",,{:.5f},{}\n".format(clock.getTime(),stim1 or stim2))
                datafile_IAT.flush()
                wait=False
                break
            else:
                datafile_IAT.write("{},{:.5f}".format(key,clock.getTime()))
                datafile_IAT.flush()
                false.draw()
                me2.draw()
                oth2.draw()
                agg.draw()
                non.draw()
                win.flip()
                psychopy.core.wait(0.3)
        me2.draw()
        oth2.draw()
        agg.draw()
        non.draw()
        if conditionIAT in ["自己","自分","私達","学生","他者","他人","彼等","教師"]:
            stim01.draw()
        else:
            stim02.draw()
        win.flip()
    me2.draw()
    oth2.draw()
    agg.draw()
    non.draw()
    fix.draw()
    win.flip()
    psychopy.core.wait(0.25)

finish.draw()
win.flip()
psychopy.core.wait(1.0)

datafile_IAT.close()

#----------IAT----------
sound.play()
plz_wait.draw()
win.flip()
psychopy.event.waitKeys(keyList=["space"])

#===========PSAP==========

global_clock=psychopy.core.Clock()
clock_rid=psychopy.core.Clock()

Na=0
Nb=0
Nc=0
Nglobal=0

total=psychopy.visual.TextStim(win,text="Total Score",font="Alial",pos=(0,8),height=1.0)
score=psychopy.visual.TextStim(win,text=S,color="white",font="ipagothic",pos=(0,5),height=2.0)
press=psychopy.visual.TextStim(win,text=Na,color="white",font="ipagothic",pos=(0,0),height=1.5)
ready=psychopy.visual.TextStim(win,text="READY?",font="Alial",pos=(0,0),color="white",height=1.5)
press_space=psychopy.visual.TextStim(win,text="Press SPACE key",pos=(0,-2),color="white",height=1.5)
space=psychopy.visual.TextStim(win,"press SPACE key",pos=(0,-7),height=1.0)
finish=psychopy.visual.TextStim(win,text="Finish",font="Alial",pos=(0,0),color="white",height=2.0)
rect=psychopy.visual.Rect(win,height=2.2,width=5.0,pos=(0,5),lineColor="white",fillColor=None)

which=psychopy.visual.TextStim(win,text="which Bottun?",font="Alial",pos=(0,0),height=2.0,color="white")
A=psychopy.visual.TextStim(win,text="Bottun A",font="Alial",pos=(-5,-6),height=1.0,color="skyblue")
AA=psychopy.visual.TextStim(win,text="Bottun A",font="Alial",pos=(-5,-6),height=1.0,color="white")
B=psychopy.visual.TextStim(win,text="Bottun B",font="Alial",pos=(0,-6),height=1.0,color="salmon")
BB=psychopy.visual.TextStim(win,text="Bottun B",font="Alial",pos=(0,-6),height=1.0,color="white")
C=psychopy.visual.TextStim(win,text="Bottun C",font="Alial",pos=(5,-6),height=1.0,color="yellow")
CC=psychopy.visual.TextStim(win,text="Bottun C",font="Alial",pos=(5,-6),height=1.0,color="white")
Bottun_Rect=psychopy.visual.Rect(win,height=2.5,width=15,pos=(0,-6),fillColor="gray",lineColor="gray")

attack=psychopy.visual.TextStim(win,"相手を攻撃!",font="Alial",pos=(0,-1),height=2.0,color="salmon")
get=psychopy.visual.TextStim(win,"ポイント獲得!",font="Alial",pos=(0,-1),height=2.0,color="skyblue")
protect=psychopy.visual.TextStim(win,"一度のみ守備",font="Alial",pos=(0,-1),height=2.0,color="yellow")
rid=psychopy.visual.TextStim(win,"ポイントを奪われました!",font="Alial",pos=(0,-1),height=2.0,color="white")

psap=psychopy.visual.TextStim(win,"ポイント獲得ゲーム2回戦",font="ipagothic",pos=(0,0),height=1.5,color="white")
inst=psychopy.visual.TextStim(win,"・この課題では，あなたはポイントをより多く獲得することを目的とします。\n・二人一組でゲームに参加し，5分間競い合います。相手はランダムに選ばれます。\n\n・ボタンAを50回押すと，1ポイント獲得できます。\n・ボタンBを10回押すと，相手に攻撃を仕掛け，相手ポイントを減らすことができます。\n　ただし，その回にあなたはポイントを得ることはできません。\n・ボタンCを10回押すと，相手からの攻撃1回分を防ぐ能力を得ます。\n　ただし，あなたがタイミングを指定することはできません。\n\n・一度ボタンを選択すると，押し終えるまで変えることはできません。\n　変えた場合，再度0からの押し直しとなってしまいます。",font="ipagothic",color="white",pos=(0,0),height=1.0)
psychopy.event.Mouse(visible=False)

datafile_PSAP.write(",,,,,二回戦\n")
psap.draw()
win.flip()
psychopy.core.wait(2.0)

inst.draw()
space.draw()
win.flip()
psychopy.event.waitKeys()
sound2.play()

total.draw()
rect.draw()
score.draw()
ready.draw()
press_space.draw()
Bottun_Rect.draw()
AA.draw()
BB.draw()
CC.draw()
win.flip()
psychopy.event.waitKeys(keyList=["space"])
TR=14
global_clock.reset()
clock.reset()
clock_rid.reset()
psychopy.event.getKeys()
while global_clock.getTime()<300:
    Na=0
    Nb=0
    Nc=0
    
    which.draw()
    Bottun_Rect.draw()
    A.draw()
    B.draw()
    C.draw()
    total.draw()
    rect.draw()
    score.draw()
    win.flip()
    
    psychopy.event.getKeys()
    choice=psychopy.event.getKeys(keyList=["escape","num_1","num_2","num_3"])
    for key in choice:
        if "escape" in choice:
            psychopy.core.quit()
        
        elif "num_1" in choice:
            total.draw()
            rect.draw()
            score.draw()
            Bottun_Rect.draw()
            BB.draw()
            CC.draw()
            A.draw()
            win.flip()
            psychopy.core.wait(0.3)
        
        elif "num_2" in choice:
            clock_rid.getTime() - 8
            total.draw()
            rect.draw()
            score.draw()
            Bottun_Rect.draw()
            AA.draw()
            CC.draw()
            B.draw()
            win.flip()
            psychopy.core.wait(0.3)
           
        elif "num_3" in choice:
            total.draw()
            rect.draw()
            score.draw()
            Bottun_Rect.draw()
            AA.draw()
            BB.draw()
            C.draw()
            win.flip()
            psychopy.core.wait(0.3)
            
    psychopy.event.getKeys()
    wait=True
    while wait:

        if clock_rid.getTime() > TR and clock_rid.getTime() < TR + 0.7:
            S -= 1
            score.setText(S)
            rid.draw()
            total.draw()
            rect.draw()
            score.draw()
            Bottun_Rect.draw()
            AA.draw()
            BB.draw()
            CC.draw()
            win.flip()
            clock_rid.reset()
            datafile_PSAP.write(",,,,1\n")
            time_rid=[37,32,40,20,5,60]
            TR=random.choice(time_rid)
            psychopy.core.wait(1.0)
            wait=True
            
        else:
            keys=psychopy.event.getKeys(keyList=["escape","num_1","num_2","num_3"])
            for key in keys:
                if "escape" in keys:
                    psychopy.core.quit()
                    
                elif "num_1" in keys:
                    if Na<50:
                        Nglobal += 1
                        Na += 1
                        Nb = 0
                        Nc = 0
                        press.setText(Na)
                        press.draw()
                        total.draw()
                        rect.draw()
                        score.draw()
                        Bottun_Rect.draw()
                        A.draw()
                        BB.draw()
                        CC.draw()
                        win.flip()
                        wait=True
                    elif Na>=50:
                        Nglobal += 1
                        S += 1
                        score.setText(S)
                        get.draw()
                        total.draw()
                        rect.draw()
                        score.draw()
                        Bottun_Rect.draw()
                        AA.draw()
                        BB.draw()
                        CC.draw()
                        win.flip()
                        datafile_PSAP.write("1,0,0,{},0\n".format(clock.getTime()))
                        psychopy.core.wait(0.7)
                        clock.reset()
                        wait=False
                        break
                    
                elif "num_2" in keys:
                    if Nb<10:
                        Nglobal += 1
                        Nb += 1
                        Na = 0
                        Nc = 0
                        press.setText(Nb)
                        press.draw()
                        total.draw()
                        rect.draw()
                        score.draw()
                        Bottun_Rect.draw()
                        AA.draw()
                        B.draw()
                        CC.draw()
                        win.flip()
                        wait=True
                    elif Nb>=10:
                        Nglobal += 1
                        attack.draw()
                        total.draw()
                        rect.draw()
                        score.draw()
                        Bottun_Rect.draw()
                        AA.draw()
                        BB.draw()
                        CC.draw()
                        win.flip()
                        datafile_PSAP.write("0,1,0,{},0\n".format(clock.getTime()))
                        psychopy.core.wait(0.7)
                        clock.reset()
                        wait=False
                        break
                
                elif "num_3" in keys:
                    if Nc<10:
                        Nglobal += 1
                        Nc += 1
                        Na = 0
                        Nb = 0
                        press.setText(Nc)
                        press.draw()
                        total.draw()
                        rect.draw()
                        score.draw()
                        Bottun_Rect.draw()
                        AA.draw()
                        BB.draw()
                        C.draw()
                        win.flip()
                        wait=True
                    elif Nc>=10:
                        clock_rid.getTime() -10
                        Nglobal += 1
                        protect.draw()
                        total.draw()
                        rect.draw()
                        score.draw()
                        Bottun_Rect.draw()
                        AA.draw()
                        BB.draw()
                        CC.draw()
                        win.flip()
                        datafile_PSAP.write("0,0,1,{},0\n".format(clock.getTime()))
                        psychopy.core.wait(0.7)
                        clock.reset()
                        wait=False
                        break


finish.draw()
total.draw()
rect.draw()
score.draw()
win.flip()
datafile_PSAP.write(",,,,,{},{}\n".format(Nglobal,S))
psychopy.core.wait(2.0)

#----------PSAP----------
sound.play()
plz_wait.draw()
win.flip()
psychopy.event.waitKeys(keyList=["space"])
#==========Go/ No-Go==========
datafile_GO.write("ans,RT,target\n")


conditions=[]
for num in [4,5,6,9]:
    for col in ["lightgreen","skyblue"]:
        conditions.append([num,col])

numb=psychopy.visual.TextStim(win,font="Alial",pos=(0,0),height=1.5)
ready=psychopy.visual.TextStim(win,text="Ready?",font="Alial",color="white",pos=(0,0),height=1.5)
space=psychopy.visual.TextStim(win,"press SPACE key",font="Alial",pos=(0,-5),height=1.0)
inst0=psychopy.visual.TextStim(win,text="数字が見えたらスペースキーをなるべく早く押す",font="ipagothic",color="white",height=1.5,pos=(0,0))
inst1=psychopy.visual.TextStim(win,text="青色の偶数\n緑色の奇数ならスペースキーをなるべく早く押す\n\n青色の奇数\n緑色の偶数ならスペースキーを押さない",font="ipagothic",pos=(0,0),height=1.5)

finish=psychopy.visual.TextStim(win,text="FINISH!",font="ipagothic",color="yellow",pos=(0,0),height=1.5)
crct=psychopy.visual.Circle(win,radius=1.5,fillColor=None,lineColor="red",pos=(0,0))
fls=psychopy.visual.TextStim(win,text="×",font="ipagothic",color="red",height=3,pos=(0,0))
gonogo=psychopy.visual.TextStim(win,"ボタンを押す？押さない？課題",font="ipagothic",pos=(0,0),height=1.5)


conditions *= 1
random.shuffle(conditions)
datafile_GO.write(",,,練習\n")

gonogo.draw()
win.flip()
psychopy.core.wait(2.0)

inst0.draw()
space.draw()
win.flip()
psychopy.event.waitKeys()

ready.draw()
space.draw()
win.flip()
psychopy.event.waitKeys()

for condition in conditions:
    num=condition[0]
    col=condition[1]
    numb.setText(num)
    numb.setColor(col)
    
    win.flip()
    psychopy.core.wait(1.0)
    
    numb.draw()
    win.flip()
    psychopy.core.wait(0.1)
    
    wait=True
    false=False
    correct=False
    psychopy.event.getKeys()
    clock.reset()
    while wait:
        keys=psychopy.event.getKeys(keyList=["escape","space"])
        if clock.getTime()<=1.2:
            if clock.getTime()<=0.5:
                for key in keys:
                    if "escape" in keys:
                        datafile_GO.close()
                        psychopy.core.quit()
                    elif "space" in keys:
                        datafile_GO.write("1,{:.5f},{}\n".format(clock.getTime(),num))
                        datafile_GO.flush()
                        correct=True
                        break
                        
        elif clock.getTime()>1.2:
            if correct:
                crct.draw()
                win.flip()
                psychopy.core.wait(0.2)
                wait=False
                break
                
            else:
                datafile_GO.write("0,,{}\n".format(num))
                datafile_GO.flush()
                fls.draw()
                win.flip()
                psychopy.core.wait(0.2)
                wait=False
                break

sound.play()
plz_wait.draw()
win.flip()
psychopy.event.waitKeys()

conditions=[]
for num in [2,3,4,5,6,7,8,9]:
    for col in ["lightgreen","skyblue"]:
        conditions.append([num,col])

conditions *= 6
random.shuffle(conditions)

datafile_GO.write(",,,本試\n")
inst1.draw()
space.draw()
win.flip()
psychopy.event.waitKeys()

ready.draw()
space.draw()
win.flip()
psychopy.event.waitKeys()
for condition in conditions:
    num=condition[0]
    col=condition[1]
    numb.setText(num)
    numb.setColor(col)
    
    win.flip()
    psychopy.core.wait(1.0)
 
    numb.draw()
    win.flip()
    psychopy.core.wait(0.1)
    
    wait=True
    false=False
    correct=False
    psychopy.event.getKeys()
    clock.reset()
    while wait:
        keys=psychopy.event.getKeys(keyList=["escape","space"])
        if num in [2,4,6,8]:
            if col in ["skyblue"]:
                if clock.getTime()<=1.2:
                    if clock.getTime()<=0.5:
                        for key in keys:
                            if "escape" in keys:
                                datafile_GO.close()
                                psychopy.core.quit()
                            elif "space" in keys:
                                datafile_GO.write("1,{:.5f},{},{}\n".format(clock.getTime(),num,col))
                                datafile_GO.flush()
                                correct=True
                                break
                            
                elif clock.getTime()>1.2:
                    if correct:
                        crct.draw()
                        win.flip()
                        psychopy.core.wait(0.2)
                        wait=False
                        break
                
                    else:
                        datafile_GO.write("0,,{},{}\n".format(num,col))
                        datafile_GO.flush()
                        fls.draw()
                        win.flip()
                        psychopy.core.wait(0.2)
                        wait=False
                        break
            elif col in ["lightgreen"]:
                if clock.getTime()<=1.2:
                    for key in keys:
                        if "escape" in keys:
                            datafile_GO.close()
                            psychopy.core.quit()
                        elif "space" in keys:
                            datafile_GO.write("0,{:.5f},{},{}\n".format(clock.getTime(),num,col))
                            datafile_GO.flush()
                            false=True
                            break
                    
                elif clock.getTime()>1.2:
                    if false:
                        fls.draw()
                        win.flip()
                        psychopy.core.wait(0.2)
                        wait=False
                        break
                    else:
                        datafile_GO.write("1,,{},{}\n".format(num,col))
                        datafile_GO.flush()
                        crct.draw()
                        win.flip()
                        psychopy.core.wait(0.2)
                        wait=False
                        break
                
        elif num in [3,5,7,9]:
            if col in ["lightgreen"]:
                if clock.getTime()<=1.2:
                    if clock.getTime()<=0.5:
                        for key in keys:
                            if "escape" in keys:
                                datafile.close()
                                psychopy.core.quit()
                            elif "space" in keys:
                                datafile_GO.write("1,{:.5f},{},{}\n".format(clock.getTime(),num,col))
                                datafile_GO.flush()
                                correct=True
                                break
                            
                elif clock.getTime()>1.2:
                    if correct:
                        crct.draw()
                        win.flip()
                        psychopy.core.wait(0.2)
                        wait=False
                        break
                
                    else:
                        datafile_GO.write("0,,{},{}\n".format(num,col))
                        datafile_GO.flush()
                        fls.draw()
                        win.flip()
                        psychopy.core.wait(0.2)
                        wait=False
                        break
            if col in ["skyblue"]:
                if clock.getTime()<=1.2:
                    for key in keys:
                        if "escape" in keys:
                            datafile_GO.close()
                            psychopy.core.quit()
                        elif "space" in keys:
                            datafile_GO.write("0,{:.5f},{},{}\n".format(clock.getTime(),num,col))
                            datafile_GO.flush()
                            false=True
                            break
                    
                elif clock.getTime()>1.2:
                    if false:
                        fls.draw()
                        win.flip()
                        psychopy.core.wait(0.2)
                        wait=False
                        break
                    else:
                        datafile_GO.write("1,,{},{}\n".format(num,col))
                        datafile_GO.flush()
                        crct.draw()
                        win.flip()
                        psychopy.core.wait(0.2)
                        wait=False
                        break
    

finish.draw()
win.flip()
psychopy.core.wait(2.0)

datafile_GO.close()
#----------Go/ No-Go----------
sound.play()
plz_wait.draw()
win.flip()
psychopy.event.waitKeys(keyList=["space"])

#===========PSAP==========

global_clock=psychopy.core.Clock()
clock_rid=psychopy.core.Clock()

Na=0
Nb=0
Nc=0
Nglobal=0

total=psychopy.visual.TextStim(win,text="Total Score",font="Alial",pos=(0,8),height=1.0)
score=psychopy.visual.TextStim(win,text=S,color="white",font="ipagothic",pos=(0,5),height=2.0)
press=psychopy.visual.TextStim(win,text=Na,color="white",font="ipagothic",pos=(0,0),height=1.5)
ready=psychopy.visual.TextStim(win,text="READY?",font="Alial",pos=(0,0),color="white",height=1.5)
press_space=psychopy.visual.TextStim(win,text="Press SPACE key",pos=(0,-2),color="white",height=1.5)
space=psychopy.visual.TextStim(win,"press SPACE key",pos=(0,-7),height=1.0)
finish=psychopy.visual.TextStim(win,text="Finish",font="Alial",pos=(0,0),color="white",height=2.0)
rect=psychopy.visual.Rect(win,height=2.2,width=5.0,pos=(0,5),lineColor="white",fillColor=None)

which=psychopy.visual.TextStim(win,text="which Bottun?",font="Alial",pos=(0,0),height=2.0,color="white")
A=psychopy.visual.TextStim(win,text="Bottun A",font="Alial",pos=(-5,-6),height=1.0,color="skyblue")
AA=psychopy.visual.TextStim(win,text="Bottun A",font="Alial",pos=(-5,-6),height=1.0,color="white")
B=psychopy.visual.TextStim(win,text="Bottun B",font="Alial",pos=(0,-6),height=1.0,color="salmon")
BB=psychopy.visual.TextStim(win,text="Bottun B",font="Alial",pos=(0,-6),height=1.0,color="white")
C=psychopy.visual.TextStim(win,text="Bottun C",font="Alial",pos=(5,-6),height=1.0,color="yellow")
CC=psychopy.visual.TextStim(win,text="Bottun C",font="Alial",pos=(5,-6),height=1.0,color="white")
Bottun_Rect=psychopy.visual.Rect(win,height=2.5,width=15,pos=(0,-6),fillColor="gray",lineColor="gray")

attack=psychopy.visual.TextStim(win,"相手を攻撃!",font="Alial",pos=(0,-1),height=2.0,color="salmon")
get=psychopy.visual.TextStim(win,"ポイント獲得!",font="Alial",pos=(0,-1),height=2.0,color="skyblue")
protect=psychopy.visual.TextStim(win,"一度のみ守備",font="Alial",pos=(0,-1),height=2.0,color="yellow")
rid=psychopy.visual.TextStim(win,"ポイントを奪われました!",font="Alial",pos=(0,-1),height=2.0,color="white")

psap=psychopy.visual.TextStim(win,"ポイント獲得ゲーム3回戦",font="ipagothic",pos=(0,0),height=1.5,color="white")
inst=psychopy.visual.TextStim(win,"・この課題では，あなたはポイントをより多く獲得することを目的とします。\n・二人一組でゲームに参加し，5分間競い合います。相手はランダムに選ばれます。\n\n・ボタンAを50回押すと，1ポイント獲得できます。\n・ボタンBを10回押すと，相手に攻撃を仕掛け，相手ポイントを減らすことができます。\n　ただし，その回にあなたはポイントを得ることはできません。\n・ボタンCを10回押すと，相手からの攻撃1回分を防ぐ能力を得ます。\n　ただし，あなたがタイミングを指定することはできません。\n\n・一度ボタンを選択すると，押し終えるまで変えることはできません。\n　変えた場合，再度0からの押し直しとなってしまいます。",font="ipagothic",color="white",pos=(0,0),height=1.0)
psychopy.event.Mouse(visible=False)

datafile_PSAP.write(",,,,,三回戦\n")
psap.draw()
win.flip()
psychopy.core.wait(2.0)

inst.draw()
space.draw()
win.flip()
psychopy.event.waitKeys()
sound2.play()

total.draw()
rect.draw()
score.draw()
ready.draw()
press_space.draw()
Bottun_Rect.draw()
AA.draw()
BB.draw()
CC.draw()
win.flip()
psychopy.event.waitKeys(keyList=["space"])
TR=21
global_clock.reset()
clock.reset()
clock_rid.reset()
psychopy.event.getKeys()
while global_clock.getTime()<300:
    Na=0
    Nb=0
    Nc=0
    
    which.draw()
    Bottun_Rect.draw()
    A.draw()
    B.draw()
    C.draw()
    total.draw()
    rect.draw()
    score.draw()
    win.flip()
    
    psychopy.event.getKeys()
    choice=psychopy.event.getKeys(keyList=["escape","num_1","num_2","num_3"])
    for key in choice:
        if "escape" in choice:
            psychopy.core.quit()
        
        elif "num_1" in choice:
            total.draw()
            rect.draw()
            score.draw()
            Bottun_Rect.draw()
            BB.draw()
            CC.draw()
            A.draw()
            win.flip()
            psychopy.core.wait(0.3)
        
        elif "num_2" in choice:
            clock_rid.getTime() - 8
            total.draw()
            rect.draw()
            score.draw()
            Bottun_Rect.draw()
            AA.draw()
            CC.draw()
            B.draw()
            win.flip()
            psychopy.core.wait(0.3)
           
        elif "num_3" in choice:
            total.draw()
            rect.draw()
            score.draw()
            Bottun_Rect.draw()
            AA.draw()
            BB.draw()
            C.draw()
            win.flip()
            psychopy.core.wait(0.3)
            
    psychopy.event.getKeys()
    wait=True
    while wait:

        if clock_rid.getTime() > TR and clock_rid.getTime() < TR + 0.7:
            S -= 1
            score.setText(S)
            rid.draw()
            total.draw()
            rect.draw()
            score.draw()
            Bottun_Rect.draw()
            AA.draw()
            BB.draw()
            CC.draw()
            win.flip()
            clock_rid.reset()
            datafile_PSAP.write(",,,,1\n")
            time_rid=[37,32,40,20,5,60]
            TR=random.choice(time_rid)
            psychopy.core.wait(1.0)
            wait=True
            
        else:
            keys=psychopy.event.getKeys(keyList=["escape","num_1","num_2","num_3"])
            for key in keys:
                if "escape" in keys:
                    psychopy.core.quit()
                    
                elif "num_1" in keys:
                    if Na<50:
                        Nglobal += 1
                        Na += 1
                        Nb = 0
                        Nc = 0
                        press.setText(Na)
                        press.draw()
                        total.draw()
                        rect.draw()
                        score.draw()
                        Bottun_Rect.draw()
                        A.draw()
                        BB.draw()
                        CC.draw()
                        win.flip()
                        wait=True
                    elif Na>=50:
                        Nglobal += 1
                        S += 1
                        score.setText(S)
                        get.draw()
                        total.draw()
                        rect.draw()
                        score.draw()
                        Bottun_Rect.draw()
                        AA.draw()
                        BB.draw()
                        CC.draw()
                        win.flip()
                        datafile_PSAP.write("1,0,0,{},0\n".format(clock.getTime()))
                        psychopy.core.wait(0.7)
                        clock.reset()
                        wait=False
                        break
                    
                elif "num_2" in keys:
                    if Nb<10:
                        Nglobal += 1
                        Nb += 1
                        Na = 0
                        Nc = 0
                        press.setText(Nb)
                        press.draw()
                        total.draw()
                        rect.draw()
                        score.draw()
                        Bottun_Rect.draw()
                        AA.draw()
                        B.draw()
                        CC.draw()
                        win.flip()
                        wait=True
                    elif Nb>=10:
                        Nglobal += 1
                        attack.draw()
                        total.draw()
                        rect.draw()
                        score.draw()
                        Bottun_Rect.draw()
                        AA.draw()
                        BB.draw()
                        CC.draw()
                        win.flip()
                        datafile_PSAP.write("0,1,0,{},0\n".format(clock.getTime()))
                        psychopy.core.wait(0.7)
                        clock.reset()
                        wait=False
                        break
                
                elif "num_3" in keys:
                    if Nc<10:
                        Nglobal += 1
                        Nc += 1
                        Na = 0
                        Nb = 0
                        press.setText(Nc)
                        press.draw()
                        total.draw()
                        rect.draw()
                        score.draw()
                        Bottun_Rect.draw()
                        AA.draw()
                        BB.draw()
                        C.draw()
                        win.flip()
                        wait=True
                    elif Nc>=10:
                        clock_rid.getTime() -10
                        Nglobal += 1
                        protect.draw()
                        total.draw()
                        rect.draw()
                        score.draw()
                        Bottun_Rect.draw()
                        AA.draw()
                        BB.draw()
                        CC.draw()
                        win.flip()
                        datafile_PSAP.write("0,0,1,{},0\n".format(clock.getTime()))
                        psychopy.core.wait(0.7)
                        clock.reset()
                        wait=False
                        break


finish.draw()
total.draw()
rect.draw()
score.draw()
win.flip()
datafile_PSAP.write(",,,,,{},{}\n".format(Nglobal,S))
psychopy.core.wait(2.0)

#----------PSAP----------
#==========Last Chance==========
op1=S +27
op2=S +19
op3=S +11
othp1=psychopy.visual.TextStim(win,text=op1,font="Alial",color="white",pos=(-0.5,5))
othp2=psychopy.visual.TextStim(win,text=op2,font="Alial",color="white",pos=(-0.5,3.5))
othp3=psychopy.visual.TextStim(win,text=op3,font="Alial",color="white",pos=(-0.5,2))
you=psychopy.visual.TextStim(win,S,font="Alial",color="white",pos=(-0.5,0.5))
player1=psychopy.visual.TextStim(win,"1位　Player2:      points",font="ipagothic",pos=(-3,5),height=1.0)
player2=psychopy.visual.TextStim(win,"2位　Player1:      points",font="ipagothic",pos=(-3,3.5),height=1.0)
player3=psychopy.visual.TextStim(win,"3位　Player3:      points",font="ipagothic",pos=(-3,2),height=1.0)
player4=psychopy.visual.TextStim(win,"4位　 あなた:      points",font="ipagothic",pos=(-3,0.5),height=1.0)
result=psychopy.visual.TextStim(win,"結果発表！",height=3.0,pos=(0,0),color="yellow",font="ipagothic")
last=psychopy.visual.TextStim(win,"LAST CHANCE",height=3.0,pos=(0,0),color="red",font="Alial")
inst=psychopy.visual.TextStim(win,"残念ながら最下位だったあなたにラストチャンスです。\n次の選択肢から一つ選ぶことで，最終的な結果を変えられます。\nこの最終的な結果は他のプレイヤーにも告知されません。\nただし，「強奪」の選択肢を選んだ場合は，減点されたことのみ他のプレイヤーに伝えられます。",height=0.9,pos=(0,-3),color="white")
choice2=psychopy.visual.TextStim(win,"選択肢1： 10ポイント得る\n選択肢2: 10ポイント他のプレイヤー達から強奪\n選択肢3: 15ポイント他のプレイヤー達から強奪\n選択肢4: 20ポイント他のプレイヤー達から強奪\n選択肢5: 30ポイント他のプレイヤー達から強奪",pos=(-8,0),height=1.0,color="white",font="ipagothic")
othp1_2=psychopy.visual.TextStim(win,text=op1,font="Alial",color="white",pos=(10.5,2.5))
othp2_2=psychopy.visual.TextStim(win,text=op2,font="Alial",color="white",pos=(10.5,1))
othp3_2=psychopy.visual.TextStim(win,text=op3,font="Alial",color="white",pos=(10.5,-0.5))
you_2=psychopy.visual.TextStim(win,S,font="Alial",color="white",pos=(10.5,-2))
player1_2=psychopy.visual.TextStim(win,"1位　Player2:      points",font="ipagothic",pos=(8,2.5),height=1.0)
player2_2=psychopy.visual.TextStim(win,"2位　Player1:      points",font="ipagothic",pos=(8,1),height=1.0)
player3_2=psychopy.visual.TextStim(win,"3位　Player3:      points",font="ipagothic",pos=(8,-0.5),height=1.0)
player4_2=psychopy.visual.TextStim(win,"4位　 あなた:      points",font="ipagothic",pos=(8,-2),height=1.0)
press_space=psychopy.visual.TextStim(win,"press SPACE key",font="Alial",pos=(0,-8),height=1.0)
press_num=psychopy.visual.TextStim(win,"該当する選択肢の数字をキーボードで押してください",font="ipagothic",pos=(0,-8),height=1.0)


result.draw()
win.flip()
psychopy.core.wait(1.0)

othp1.draw()
othp2.draw()
othp3.draw()
you.draw()
player1.draw()
player2.draw()
player3.draw()
player4.draw()
press_space.draw()
win.flip()
psychopy.event.waitKeys()

last.draw()
win.flip()
psychopy.core.wait(1.0)

othp1.draw()
othp2.draw()
othp3.draw()
you.draw()
player1.draw()
player2.draw()
player3.draw()
player4.draw()
inst.draw()
press_space.draw()
win.flip()
psychopy.event.waitKeys()
choise=True
while choise:
    keys=psychopy.event.getKeys(keyList=["escape","1","3","4","5","num_1","num_2","num_3","num_4","num_5"])
    for key in keys:
        if "escape" in keys:
            psychopy.core.quit()
        else:
            datafile_PSAP.write("last,{}".format(key))
            choise=False
            break
    
    othp1_2.draw()
    othp2_2.draw()
    othp3_2.draw()
    you_2.draw()
    player1_2.draw()
    player2_2.draw()
    player3_2.draw()
    player4_2.draw()
    choice2.draw()
    press_num.draw()
    win.flip()


thankyou=psychopy.visual.TextStim(win,text="課題は以上です。\nお疲れ様でした。\nカーテンを開けて実験者をお待ちください。\nお待ちの間，質問紙への記入を続けてください。",font="ipagothic",color="white",pos=(0,0),height=1.3)
you2=psychopy.visual.TextStim(win,S,pos=(10,-10),font="Alial",color="white",height=1.0)

sound.play()
thankyou.draw()
you2.draw()
win.flip()
psychopy.event.waitKeys(keyList=["return"])

