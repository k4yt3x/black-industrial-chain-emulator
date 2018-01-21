[![Join the chat at https://gitter.im/K4YT3X-DEV/SCUTUM](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/K4YT3X-DEV/SCUTUM?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![status](https://travis-ci.org/K4YT3X/SCUTUM.svg)](https://travis-ci.org/K4YT3X/SCUTUM)

<center>
<img src="https://user-images.githubusercontent.com/21986859/35191084-e3c27724-fe3f-11e7-94c2-9584635bfc3f.png" width="600" height="600"></center>

# Black Industrial Chain Emulator

Black Industrial Chain Emulator (BICE) is an educational game designed to help company employees or ordinary people understand how the black industry works thus to make people be more aware about security and prevent low-level exploits from making damage to companies or individuals.

This game have different modes. In the hacker vs. hacker mode, two or more players will play as hackers. They will try to phish, exploit or attack companies using various of methods and gain money from companies by selling information.

<img width="843" alt="ui" src="https://user-images.githubusercontent.com/21986859/35191073-af913350-fe3f-11e7-981b-a250b533496c.png">

In hacker vs. security manager mode, the player playing as security manager will learn how to patch common vulnerabilities and how to keep servers secure. They need to protect servers and assets safe from the players playing as hacker who will be trying to generate as much profit as possible by exploiting the company.

## How We Developed This Game

We originally designed this game to be a traditional online multiplayer game which uses UDP clients and UDP servers. However, inspired by **StdLib**'s flexibility and convenience, we created a **serverless** multiplayer game with high modularity.

During the development, we encountered issues with Ajax which was a key to the successful deployment of our service. We tried looking for solutions on Google, and we also tried asking mentors. Unfortunately, we weren't able to develop a solution for fixing Ajax due to the time constraint and the lack of front-end developing capability.

However, we didn't stop there when we encountered obstacles. We continued on exploring more possibilities of improving our program within our range of capability. We looked into Unreal Engine 4 and Unity 5. Eventually, we were made a simple map demo rendering with Unity 5. We believe that we can finish this project with high-quality if we had more time.

</br>

## How to Play

#

### Hacker VS. Hacker

You will play the role of a black hat hacker and compete with another hacker (A.I. or online player). Whenever you hack into a company server, the company server will generate a certain amount of profit for you in a period of time. 

During the process, hackers can sabotage the competitor's servers so the competitor stops getting money from that server.

#### Winning Conditions

	The goal of the two hackers is to loot a certain amount of money from company servers. Whoever reaches that value first will win the game.

#
### Hacker VS. Company

When you enter the main menu, you will select your role. You can either be a security manager or a black hat hacker. The goal of the hacker is to compromise as many servers as they can, and the job of the security manager is to prevent the servers from being hacked.

When a company server gets hacked, the hacker will profit from the data leaked from the server.

### Winning Conditions

#### Hackers

	Once the hacker gets a certain amount of money out of the company in a limited time, the hacker wins.

#### Security Managers

	If the security manager manages to prevent the hacker from stealing a certain amount of money within the limited time, security manager wins.

Day system - each hacker has one chance to make a decision per day

hacking difficulty 1-5

hacker attributes:
	Level - skill/hardware level, determines which hacker obtains the server when conflict hacks occur
	money - amount of money, generated each turn depending on how many servers owned

Server attributes:
	Status - neutral or hacked
	int down - down for how many days
	Security level - determines the difficulty to hack


