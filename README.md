# text-ding
PureOS SMS Alerts

This project is still very new, would love to have people test it. 

You will need python3 and vlc.

steps to set up:
1. mkdir ~/Projects & cd ~/Projects
2. clone the project 
3. chmod +x *.python
4. execute the init python script once
5. add this to crontab file, command: crontab -e
```
* * * * * cd /home/purism/Projects/text-ding & /home/purism/Projects/text-ding/main.py
```
