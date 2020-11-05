'''
this is just to restart the bot if it runs out of memory. probably won't be an issue, but if you have 500mb of ram like me it sure is
'''

import subprocess

filename = 'tetris-bot.py'
while True:
    p = subprocess.Popen('python3 '+filename, shell=True).wait()

    if p != 0:
        continue
    else:
        break
