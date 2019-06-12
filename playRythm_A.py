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


param_dict={"subj_num":"","gender":["female","male"],"age":""}
dlg=psychopy.gui.DlgFromDict(param_dict,title="PLAYER  INFORMATION")
if dlg.OK==False:
    psychopy.core.quit()

win=psychopy.visual.Window(fullscr=True, monitor="testMonitor", units="deg",color="gray")
clock=psychopy.core.Clock()

filename= param_dict["subj_num"] + "_" + param_dict["gender"] + "_"+ param_dict["age"] + "_A.csv"
datafile=codecs.open(filename,"w","shift-JIS")

psychopy.event.Mouse(visible=False)

inst1=psychopy.visual.TextStim(win,"2つ目の課題は、リズムを再生する課題です。\n音刺激が前半と後半にわかれており、\n前半で聴いたメロディーを後半で再生してもらいます。\n後半ではメロディーは流れず、\n小節の頭の音のみ提示されます。\n前半と後半は連続しており、前半が終わると\nすぐに後半が始まるので注意してください。\nよろしければスペースキーを押してください。",pos=(0,0),height=1.3,color="white",font="ipagothic")
inst2=psychopy.visual.TextStim(win,"リズムの再生はキー押しで行います。\n前半で聴いたリズムを再現するように\njのキーを連打してください。\n先ほどの課題と同様に、\nReady？の画面が提示されるので、\nスペースキーを押すと次へ進みます。\nよろしければスペースキーを押して、\n練習試行を開始してください。",pos=(0,0),height=1.3,color="white",font="ipagothic")
inst3=psychopy.visual.TextStim(win,"再生→jのキー",font="ipagothic",pos=(0,0),height=2.0,color="white")
ready=psychopy.visual.TextStim(win,"Ready?",font="Alial",pos=(0,0),height=2.0,color="white")
inst4=psychopy.visual.TextStim(win,"練習試行は以上です。",font="ipagothic",pos=(0,0),height=2.0,color="white")
inst5=psychopy.visual.TextStim(win,"これから本試行を始めます。\n練習試行と流れは同じです。\n\nよろしければスペースキーを押して\n本試行を開始してください。",font="ipagothic",pos=(0,0),height=2.0,color="white")
end=psychopy.visual.TextStim(win,"これで2つ目の課題は終了です。\nご協力ありがとうございました。",pos=(0,0),font="ipagothic",height=2.0)

sound=psychopy.sound.Sound()


practice=[]
for pra in ["13sb2.wav","16sb0.wav","23sb3.wav","31sb1.wav","42sb4.wav","60sb2.wav"]:
    practice.append(pra)
random.shuffle(practice)

trial=[]
for tri in ["1sa3.wav","2sa4.wav","3sa0.wav","4sa1.wav","5sa2.wav","6sa3.wav","7sa4.wav","8sa0.wav","9sa1.wav","10sa2.wav","11sa3.wav","12sa4.wav","13sa0.wav","14sa1.wav","15sa2.wav","16sa3.wav","17sa4.wav","18sa0.wav","19sa1.wav","20sa2.wav","21sa0.wav","22sa4.wav","23sa1.wav","24sa2.wav","25sa3.wav","26sa0.wav","27sa4.wav","28sa1.wav","29sa2.wav","30sa3.wav","31sa0.wav","32sa4.wav","33sa1.wav","34sa2.wav","35sa3.wav","36sa0.wav","37sa4.wav","38sa1.wav","39sa2.wav","40sa3.wav","41sa0.wav","42sa1.wav","43sa2.wav","44sa3.wav","45sa4.wav","46sa0.wav","47sa1.wav","48sa2.wav","49sa3.wav","50sa4.wav","51sa0.wav","52sa1.wav","53sa2.wav","54sa3.wav","55sa4.wav","56sa0.wav","57sa1.wav","58sa2.wav","59sa3.wav","60sa4.wav"]:
    trial.append(tri)
random.shuffle(trial)

inst1.draw()
win.flip()
psychopy.event.waitKeys(keyList=["space"])

inst2.draw()
win.flip()
psychopy.event.waitKeys(keyList=["space"])

datafile.write("practice\n")

for p in practice:
    pra=p
    sound.setSound(pra)
    
    ready.draw()
    win.flip()
    psychopy.event.waitKeys(keyList=["space"])
    datafile.write("\n{},".format(pra))
    
    
    if p in ("13sb2.wav"):
        finish=24
    elif p in ("16sb0.wav"):
        finish=32
    elif p in ("23sb3.wav"):
        finish=12
    elif p in ("31sb1.wav"):
        finish=10
    elif p in ("42sb4.wav"):
        finish=9
    elif p in ("60sb2.wav"):
        finish=8
    
    wait=True
    sound.play()
    clock.reset()
    while wait:
        if clock.getTime() <= finish:
            keys=psychopy.event.getKeys(keyList=["escape","j"])
            for key in keys:
                if "escape" in keys:
                    datafile.close()
                    psychopy.core.quit()
            
                elif "j" in keys:
                    datafile.write("{:.5f},".format(clock.getTime()))
                    datafile.flush()
            inst3.draw()
            win.flip()
        elif clock.getTime() > finish:
            wait=False
            break

inst4.draw()
win.flip()
psychopy.event.waitKeys(keyList=["space"])


inst5.draw()
win.flip()
psychopy.event.waitKeys(keyList=["space"])

datafile.write("\n\ntrial\n")

for t in trial:
    tri=t
    sound.setSound(tri)
    
    ready.draw()
    win.flip()
    psychopy.event.waitKeys(keyList=["space"])
    datafile.write("\n{},".format(tri))
    
    
    if t in ("1sa3.wav","2sa4.wav","3sa0.wav","4sa1.wav","5sa2.wav","6sa3.wav","7sa4.wav","16sa3.wav","17sa4.wav"):
        finish=32
    elif t in ("8sa0.wav","9sa1.wav","10sa2.wav","11sa3.wav","12sa4.wav","13sa0.wav","14sa1.wav","15sa2.wav","18sa0.wav","19sa1.wav","20sa2.wav"):
        finish=24
    elif t in ("36sa0.wav","37sa4.wav"):
        finish=13
    elif t in ("21sa0.wav","22sa4.wav","23sa1.wav","24sa2.wav","25sa3.wav","26sa0.wav","27sa4.wav"):
        finish=12
    elif t in ("28sa1.wav","29sa2.wav","30sa3.wav","31sa0.wav","32sa4.wav","33sa1.wav","34sa2.wav","35sa3.wav","38sa1.wav","39sa2.wav","40sa3.wav"):
        finish=10
    elif t in ("41sa0.wav","42sa1.wav","43sa2.wav","44sa3.wav","45sa4.wav","46sa0.wav","47sa1.wav","48sa2.wav","56sa0.wav","57sa1.wav","58sa2.wav"):
        finish=9
    elif t in ("59sa3.wav","60sa4.wav"):
        finish=8
    elif t in ("49sa3.wav","50sa4.wav","51sa0.wav","52sa1.wav","53sa2.wav","54sa3.wav","55sa4.wav"):
        finish=7
        
    wait=True
    sound.play()
    clock.reset()
    while wait:
        if clock.getTime() <= finish:
            keys=psychopy.event.getKeys(keyList=["escape","j"])
            for key in keys:
                if "escape" in keys:
                    datafile.close()
                    psychopy.core.quit()
            
                elif "j" in keys:
                    datafile.write("{:.5f},".format(clock.getTime()))
                    datafile.flush()
            inst3.draw()
            win.flip()
        elif clock.getTime() > finish:
            wait=False
            break


end.draw()
win.flip()
psychopy.core.wait(1.0)