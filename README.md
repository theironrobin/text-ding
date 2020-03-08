# text-ding
PureOS SMS Alerts

This project is still very new, would love to have people test it. 

steps to run:
1. ```sudo apt-get install vlc python3-pip python3-dbus```
2. ```mkdir ~/Projects & cd ~/Projects```
3. clone the project to Projects directory
4. chmod +x main.py
5. you can run it manually with ```python3 main.py``` or set up autostart below
5. ```cd /home/purism/.config/autostart && touch text-ding.desktop```




2. clone the project 
4. execute the init python script once ```python3 init.py```
5. add this to crontab file, command: crontab -e
```
* * * * * cd /home/purism/Projects/text-ding & /home/purism/Projects/text-ding/main.py
```
you can add this to the end of the cron line for debug: ```>> ~/cron.log 2>&1```
