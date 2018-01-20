[![Join the chat at https://gitter.im/K4YT3X-DEV/SCUTUM](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/K4YT3X-DEV/SCUTUM?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![status](https://travis-ci.org/K4YT3X/SCUTUM.svg)](https://travis-ci.org/K4YT3X/SCUTUM)

# Hack The Companies

HTC is an educational game that helps people understand basic security challenges for companies and organizations.

In this game, players will play as a hacker or a security manager.

## How to Play:

### Hacker VS. Hacker
You will play the role of a black hat hacker and compete with another hacker (A.I. or online player). Whenever you hack into a company server, the company server will generate a certain amount of profit for you in a period of time. 

During the process, hackers can sabotage the competitor's servers so the competitor stops getting money from that server.

#### Winning Conditions
~~~~
The goal of the two hackers is to loot a certain amount of money from company servers. Whoever reaches that value first will win the game.
~~~~

### Hacker VS. Company

When you enter the main menu, you will select your role. You can either be a security manager or a black hat hacker. The goal of the hacker is to compromise as many servers as they can, and the job of the security manager is to prevent the servers from being hacked.

When a company server gets hacked, the hacker will profit from the data leaked from the server.

### Winning Conditions
#### Hackers:
~~~~
Once the hacker gets a certain amount of money out of the company in a limited time, the hacker wins.
~~~~

#### Security Managers:
~~~~
If the security manager manages to prevent the hacker from stealing a certain amount of money within the limited time, security manager wins.
~~~

Day system - each hacker has one descision per day

hacking difficulty 1-5

hacker attributes:
	Level - skill/hardware level, determines which hacker obtains the server when conflict hacks occur
	money - amount of money, generated each turn depending on how many servers owned
	

Server attributes:
	Status - neutral or hacked
	int down - down for how many days
	Security level - determines the difficulty to hack


