## Manini-Case-01

### Description

An employee's machine has been brought to your notice for analysis.
The employee is suspected of engaging in equipment abuse by contravening the company's policies.
You are requested to carry out an inquiry into the staff device to identify any evidence of improper usage. Connect to the netcat session below and answer all the questions correctly to get the flag at the end.

### Solution

In these challenges we'll be using `Autopsy` as it is very sufficient for discovering, parsing and analysing artifact files.

- We can use `ewfinfo` to get the hash of the disk image represented by the Encase files ".E01, .E02"

- The computer name can be found in the file `/etc/hostname`

- The password can be found in `/etc/shadow` but it is hashed. We have been given a wordlist to bruteforce the password using `john`

```sh

└─$ cat shadow.txt                                       
manini:$y$j9T$WAaXEsxn2XMOxQhYFAJ9t0$7PKOLnhZVjKDbkEZ3WvkvbTK2HLMGWDo3EmJG6JuOr8:19739:0:99999:7:::
                                                                                                                                              
└─$ cat passwd.txt   
manini:x:1000:1000:Manini,,,:/home/manini:/bin/bash
                                                                                                                                              
└─$ unshadow passwd.txt shadow.txt > unshadow.txt        
                                                                                                                                              
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt unshadow.txt 
Using default input encoding: UTF-8
No password hashes loaded (see FAQ)
                                                                                                                                              
└─$ john --show unshadow.txt
manini:2024:1000:1000:Manini,,,:/home/manini:/bin/bash

1 password hash cracked, 0 left

```

The password is `2024`
