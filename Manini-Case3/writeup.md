## Manini-Case-03 

### Solution

- The first thing we need to look at when talking about usually visited website or something like that is the file `/etc/hosts` which contains domain names that can be resolved to their ip addresses without the need to send a request to a dns server. The website is: `freepalestine-foundation.dz`

- We was looking in various log files under `/var/log/` until we found a UUID of the root partition in the file `/var/log/dmesg`

- If you are using autopsy, you might noticed that it detected a file that might be encrypted at the location: `.local/share/Trash/files/secret`
This folder contains password protected zip file and a file called `password.wave`, this file contains some **Beeps** which are surely hiding some data. There are plenty of websites that convert beep audio files to binary code which encodes the password of the zip file. The unziped file contains the password we are looking for.