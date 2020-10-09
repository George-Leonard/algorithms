#------------------------------------------------------------------------------
#-----------------------Made by George Leonard 15/09/2019----------------------
#------------------------------------------------------------------------------

import os, time, pyperclip, unscrambler as u
log = open(os.getenv("APPDATA") +"/.minecraft/logs/latest.log", "r")

arkhamwords = []
u.addword("Wolverine", arkhamwords)
u.addword("playervaults", arkhamwords)
u.addword("Arkham Network", arkhamwords)
u.addword("Youtube", arkhamwords)
u.addword("Legend", arkhamwords)
u.addword("towny", arkhamwords)
u.addword("steak", arkhamwords)
u.addword("pandas", arkhamwords)
u.addword("superman", arkhamwords)
u.addword("hulk", arkhamwords)
u.addword("auction", arkhamwords)
u.addword("Twitter", arkhamwords)
u.addword("villager", arkhamwords)
u.addword("lightning", arkhamwords)
u.addword("message", arkhamwords)
u.addword("oldschool-prison", arkhamwords)
u.addword("scrambler", arkhamwords)
u.addword("events", arkhamwords)
u.addword("Discord", arkhamwords)
u.addword("black-panther", arkhamwords)
u.addword("harvest", arkhamwords)
u.addword("Play-mc", arkhamwords)
u.addword("creepers", arkhamwords)
    

while True:
    line = log.readline()


#------------------------------------------------------------------------------
#                               Reaction word
#------------------------------------------------------------------------------
    if "[Client thread/INFO]: [CHAT] Reaction Word:" in line:
        rlist = list(line)
        print(line)
        rword = rlist[55:]
        rword = rword[:(len(rword)-1)]
        for c in rword:
            for i in (" [],''"):
                rword = str(rword).replace(i, '')


        if not line:
            time.sleep(0.1)
            continue




        print(rword)
        pyperclip.copy(rword) 
        
#------------------------------------------------------------------------------
#                              Math Problem
#------------------------------------------------------------------------------

    if "[Client thread/INFO]: [CHAT] Math problem:" in line:

        mlist = list(line)
        print(line)
        mquestion = mlist[54:]
        mquestion = mquestion[:(len(mquestion)-1)]
        for c in mquestion:
            for i in (" [],''"):
                mquestion = str(mquestion).replace(i,'')

        if not line:
            time.sleep(0.1)
            continue



        print(eval(mquestion))
        pyperclip.copy(eval(mquestion))
        
#------------------------------------------------------------------------------
#                             Unscramble word
#------------------------------------------------------------------------------
# WORDS : Wolverine, playervaults, Arkham Network, YouTube, Legend, towny, steak, pandas, superman, hulk, auction, Twitter, villager, lightning, message, 
#         oldschool-prison, scrambler, events, Discord, black-panther, harvest, Play-mc, creepers

    if "[Client thread/INFO]: [CHAT] Scrambled word:" in line:
        swlist = list(line)
        print(line)
        sw = swlist[56:]
        sw = sw[:(len(sw)-1)]
        #print(sw)
        for c in sw:
            for i in (" [],''"):
                sw = str(sw).replace(i,'')


        text = u.unscramble(sw, arkhamwords))
        print(text)
        pyperclip.copy(text)

    if not line:
        time.sleep(0.1)
        continue

#https://github.com/George-Leonard/                      

