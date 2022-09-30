# Incoming Software Engineer Evaluation

In this repo are a series of coding questions and three quick programming exercises to evaluate where to best place you. Pull this repo and change the upstream branch from the MoonFall one to a personal public repository. A guide on how to do that can be found [here](https://devconnected.com/how-to-change-git-remote-origin/). Please fill out the info section on this page, the complete the quick answer questions below. 

There are also 3 programming challenges written in python 3. If you do not know python you can answer in detailed pseudocode or c++. Detailed descriptions for the tasks are in their folders README files. 

 - [C1: Game of Life](C1/README.md)
 - [C2: Matrix Operations](C2/README.md)
 - [C3: Calculator](C3/README.md)

When you are finished, push the code to your own repo and send the link to maxwildersmith@gmail.com.

---
## Info

Name: 

Email:

Project you are applying for:


---
## Quick Answer Questions
For the following questions answer as best you can, if you do not know, either make your best guess or skip the question. These questions are designed to cover all the potential roles for a project so it is not expected to know the answer to all of them. For the short answer ones answer is one or two sentences.

Sample:

Which of these is the number 5?
 - 1
 - 0
> - 5
 - 4

What is one difference between a float and an int?

> An int is a whole integer number while a float can be a decimal value.

### Questions:
---

**General**

What does an activity diagram show?
>An activity diagram is a complex state/decision diagram which allows developers to visualize the flow between different processes within a program or use case

Which of these languages offers the lowest level of control and fastest execution?
 - Python
 - C#
 - Java
> - C


What is the purpose of version control systems (VCS) such as Git or Mercurial?
>Version Control Systems have multiple advantages to programming on a single system. These include improved communication for collaborative projects, improved systems for code documentation through forks, documented push/pull requests, and other tools, and better version iteration throughout a development lifecycle.
---
**Embedded Systems**

Which level of cache would be accessible by only a single core on a multi-core chip?
> - L1
 - L2
 - L3
 - All levels


Explain one difference between any of these 2 protocols: I2C, SPI, UART:
>intentially blank

What is a feature Java has that C++ does not?
 - Object oriented classes
 - Lambda expressions
 - Data streams
> - Implicit garbage collection


Name one major concern when developing for embedded systems and edge computing such as a deployed Jetson or Raspberry Pi:
> deployed systems may be difficult to access and update after deployment (both physically and with regards to networking)

Which of the following is a job for the DHCP server?
 - Route packets out to the internet
 - Make particular ports available for access on the inter/intranet
> - Assign IP addresses on the network
 - Look up what domain name maps to an address on the internet

---
**Linux**

What does the permission code 777 represent (as used in `chmod 777`)?
>this command provides full read/write/execute privilages to *all* users groups and "others" on a system

Which of these commands sets and environment variable in Linux? 
> - export VAR=val
 - export $VAR=val 
 - echo VAR=val
 - echo $VAR=val


What is one major role of systemd?
>Systemd is a vital component to management of system processes

---
**AI**

Which of these network architectures would be best suited for processing text?
 - Convolution Neural Network
> - Recurrent Neural Network
 - Multilayer Perceptron
 - U-Net


What is one solution to the vanishing gradient problem in backprop?
>intentionally left blank

What is the traditional flow of interactions for a reinforcement learning agent?
 - Read the current state, take an action, environment updates state
 - Make a prediction, evaluate the loss from a target, update model with backprop
 - Generate result, compare result to similar objects of the class, improve discriminator and predictor


Briefly describe either branch and bound or dynamic programming:
>Dynamic programming refers to an algorithmic approach to problem solving in which the problem is broken up into smaller sub-problems to solve

What is the main challenge with implementing A*:
 - Picking the correct heuristic
 - Initialization parameters
 - Solution will not converge
> - Too long of an execution compared to other common pathfinders
