## Remote Digital Problems

### Desription

As a member of a DFIR team, you are looking into a possible security breach that occurred on a company network. Possible illegal access using Remote connections has been discovered during preliminary investigation. It is your responsibility to examine the cache files that you took from the infected system in order to compile information and piece together the attacker's path.

### Solution


- the challenge's files are Remote desktop cache files ( bmc files ), its goal is to produce logs for the RDP session, and that's by saving small bitmaps files for the screen and caching them in that file

- `bmc-tools.py` is useful open source tool to parse these files.

- Keep looking until you find the flag being typed to the cmd terminal.


`nexus{Intr0_t0_RDP_C4ch3_4n6$$$}`