#coding:utf-8
from __future__ import division
from __future__ import unicode_literals
import psychopy.visual
import psychopy.core
import psychopy.event
import random
import codecs

# "#"から始まる緑字はメモです。"#~!~"の所は吉野さんが記入する箇所があります。"#"だけのところは、一応、その個所のプログラムの説明となっています。

datafile=codecs.open("ファイル名.csv","w","shift-JIS")   #~!~"ファイル名"の所に、その被験者のデータファイル名を被験者ごとに記入。ブロックがわかるようにしておくと良いかもex., s1_nf(被験者1の名前（n）から顔（f）)
datafile.write("prime,stim,rt,key\n")    #データファイルに「プライム、ターゲット、反応時間、押したキー」を記入

win=psychopy.visual.Window(fullscr=False,monitor="testMonitor",units="cm",color="black")    #実験中のスクリーンについて
clock=psychopy.core.clock()    #計測時計の設定

conditions=[]
for prime in [u"ひなの",u"あやか",u"まりな",u"ももか",u"ひろし",u"たける",u"ゆうた",u"けんと",u"さくら",u"ありさ",u"だいち",u"ふみや"]:
    for target in ["CHUSEI1.png","CHUSEI2.png","CHUSEI3.png","chusei4.png","chusei5.png","CHUSEI6.png","CHUSEI7.png","chusei8.png","chusei9.png","female1.png","female2.png","female3.png","female4.png","male1.png","male2.png","male3.png","male4.png","female5.png","female6.png","male5.png","male6.png"]:
        conditions.append([prime,target])
        
conditions *= 2    #~!~くり返しの数
random.shuffle(conditions)    #シャッフル

img=psychopy.visual.ImageStim(win,size=(5,5),pos=(0,0))
name=psychopy.visual.TextStim(win,font="ipagothic",color="white",pos=(0,0),height=3.0)

fix=psychopy.visual.TextStim(win,text="+",font="Alial",color="white",pos=(0,0),height=3.0)    #注視点
male=psychopy.visual.TextStim(win,text="男性",font="ipagothic",color="white",pos=(-10,6),height=2.5)
female=psychopy.visual.TextStim(win,text="女性",font="ipagothic",color="white",pos=(10,6),height=2.5)
ready=psychopy.visual.TextStim(win,text="Ready?\npress SPACE key",font="ipagothic",color="white",pos=(0,0),height=3.0)

#-------- experiment -----------------


for condition in conditions:
    
    prime=condition[0]
    target=condition[1]
    name.setImage(prime)
    img.setText(target)
    
    ready.draw()
    win.flip()
    psychopy.event.waitKeys(keyList=["space"])
    
    fix.draw()
    win.flip()
    psychopy.core.wait(0.5)
    
    name.draw()
    fix.draw()
    win.flip()
    psychopy.core.wait(0.15)
    
    waiting_keypress=True
    psychopy.event.getKeys()
    clock.reset()
    while waiting_keypress:
        keys=psychopy.event.getKeys(keyList=["e","i","escape"])
        for key in keys:
            if "escape" in keys:
                datafile.close()
                psychopy.core.quit()
            elif "e" or "i" in keys:
                datafile.write("{},{},{:.3f},{}\n".format(prime,target,clock.getTime,key))
                datafile.flush()
                waiting_keypress=False
                break
        male.draw()
        female.draw()
        img.draw()
        win.flip()

datafile.close()