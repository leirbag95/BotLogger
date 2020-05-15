import modules
from modules.listner import ListenerLOG
from modules.bot import BotLOG
import os
from glob import glob

print("Welcome to BotLogger! 👋")
print("What are you looking for ?")
while True:
    c = int(input("\t1. To record\n\t2.To play\n"))
    if c == 1:
        filename = str(input("Alright! Drop a file name: "))
        llog = ListenerLOG(filename)
        llog.run()
    else:
        print("JSON FILE LIST")
        print(*[ "{0}\n".format(pos_json) for pos_json in os.listdir('.logs/') if pos_json.endswith('.json')])
        filename = str(input("Alright! Drop a file name from the above list: \n"))
        blog = BotLOG(filename)
        blog.run()