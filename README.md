# laggingFriends
Tiny project for dropping packets with a chosen probability


## What can you do:
After man-in-the-middle attack to your friend, you can choose a probability for dropping packages.<br>
Just for your friends' fun :)


## How do you use it:
```
# Before run "droop.py" run arpspoof as indicated in the help menu

python droop.py
      _                                    _        _   
     | |                                  | |      | |  
   __| |_ __ ___  _ __    _ __   __ _  ___| | _____| |_ 
  / _` | '__/ _ \| '_ \  | '_ \ / _` |/ __| |/ / _ \ __|
 | (_| | | | (_) | |_) | | |_) | (_| | (__|   <  __/ |_ 
  \__,_|_|  \___/| .__/  | .__/ \__,_|\___|_|\_\___|\__|
                 | |     | |                            
                 |_|     |_|                            
press -h for help

Need two arguments <ip> <probability*100>
PoC of dropping tool.
Remember to do men-in-the-middle attack before using this tool (you can use arpspoof)

Version: 2.4
Usage: arpspoof [-i interface] [-c own|host|both] [-t target] [-r] host

```


## What do you need:
```
# Before run "droop.py" run the following command:

apt-get install build-essential python-dev libnetfilter-queue-dev
```
