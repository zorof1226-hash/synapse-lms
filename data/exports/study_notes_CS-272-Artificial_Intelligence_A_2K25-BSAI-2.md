# 📚 Study Knowledge Base: CS-272-Artificial_Intelligence_A_2K25-BSAI-2

*Auto-generated from LMS lecture notes. Compatible with Obsidian & Notion.*

---

## CS-272-Artificial_Intelligence_A_2K25-BSAI-2 - W2L2.pptx

### 📝 Executive Summary
This lecture on 'W2L2.pptx' covers key fundamentals across 15 slides/sections. Major themes include Slide 1, Slide 2, Slide 3, Slide 4. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Lecture 3**: Agents, Rationality & PEAS  |  1
- **Small world**: candies, turns, win/lose
- **Expected answer**: Because even a simple game has state, actions, goal, and a decision strategy.
- **AI goal**: build agents that can act in the real world
- **Before we continue**: what does PEAS stand for?
- **The core idea**: an agent receives information and takes action.
- **For Candy Game**: what is the environment, percept, and action?
- **Candy example**: "7 candies remain".
- **Example**: robotic vacuum-cleaning agent
- **Yes**: because the outcome may depend on hidden information, chance, or another agent.

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Slide 1 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on W2L2.pptx, Slide 1: CS-370 - Lecture 3
Agents, Rationality, and PEAS
Perceive
Decide
Act
Evaluate
Lecture 3 - Agents, Rationality & PEAS  |  1

> **Q: Summarize the core mechanism of Slide 2 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on W2L2.pptx, Slide 2: Where this lecture fits
From a small game to real-world AI systems
Candy Game
Small world: candies, turns, win/lose
Agent
A system that perceives and acts
Rationality
Chooses action expected to work best
PEAS
Describes the task before coding
ASK STUD

> **Q: Summarize the core mechanism of Slide 3 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on W2L2.pptx, Slide 3: Quick recap from last lecture
AI goal: build agents that can act in the real world
AI systems sense, learn, reason, and take action
In this course, we focus on agents that act rationally
PEAS helps us describe an AI task before designing the agent
QU

> **Q: Summarize the core mechanism of Slide 4 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on W2L2.pptx, Slide 4: Agent and environment
The core idea: an agent receives information and takes action.
AGENT
chooses an action
ENVIRONMENT
world/problem around the agent
Percepts / input
Actions / output
ASK STUDENTS
For Candy Game: what is the environment, percept, a

---

## CS-272-Artificial_Intelligence_A_2K25-BSAI-2 - Lab 5 - Informed Search

### 📝 Executive Summary
This lecture on 'Lab 5 - Informed Search' covers key fundamentals across 13 slides/sections. Major themes include Page 1, Page 2, Page 3, Page 4. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **CS272**: Artificial Intelligence
- **Lab 5**: Informed Search (CLO 4)
- **Note**: You can work in groups of 2 but not more than 2.
- **Deliverables**: Submit search.py and a report document with screenshots of your results (see
- **Deadline**: Will be decided at the end of the lab
- **a heuristic**: function heuristic(state, problem) that returns a number. nullHeuristic in search.py
- **Priority**: the fringe is now a util.PriorityQueue, which always gives back the state with the lowest
- **Greedy search**: priority = h(n)
- **Admissible heuristic**: a heuristic that never overestimates the true remaining cost. When every step
- **Consistent heuristic**: a heuristic where, for every step from n to n', h(n) is no more than the step cost

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Page 1 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on Lab 5 - Informed Search, p.1: Page 1 
 
 
CS272: Artificial Intelligence   
 
Fall 2026 
 
 
 
 
 
 
Department of Computing 
 
CS-272 Artificial Intelligence 
BSAI 2K25 
 
Lab 5: Informed Search (CLO 4) 
 
Date: October 6th, 2026 
Time: 14:00 - 17:00  
 
Instructor: Sadia Shakil

> **Q: Summarize the core mechanism of Page 2 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on Lab 5 - Informed Search, p.2: Page 2 
 
 
CS272: Artificial Intelligence   
 
Fall 2026 
 
 
Lab 5: Informed Search 
 
Implement Questions 1, 2 and 3, which are given below. 
 
Note: You can work in groups of 2 but not more than 2. 
Deliverables: Submit search.py and a report doc

> **Q: Summarize the core mechanism of Page 3 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on Lab 5 - Informed Search, p.3: Page 3 
 
 
CS272: Artificial Intelligence   
 
Fall 2026 
understand in order to complete the assignment, and some of which you can ignore. You can 
download all the code and supporting files from LMS. 
 
 
Attribution: 
This lab is adapted from the

> **Q: Summarize the core mechanism of Page 4 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on Lab 5 - Informed Search, p.4: Page 4 
 
 
CS272: Artificial Intelligence   
 
Fall 2026 
Supporting files you can ignore: 
graphicsDisplay.py 
Graphics for Pacman 
graphicsUtils.py 
Support for Pacman graphics 
textDisplay.py 
ASCII graphics for Pacman 
ghostAgents.py 
Agents to 

---

## CS-272-Artificial_Intelligence_A_2K25-BSAI-2 - Week 3 Lecture 2 - Agent Types

### 📝 Executive Summary
This lecture on 'Week 3 Lecture 2 - Agent Types' covers key fundamentals across 16 slides/sections. Major themes include Slide 1, Slide 2, Slide 3, Slide 4. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Main question**: How does an agent choose an action?
- **Built from W1-L3 ideas**: utility, PEAS, rationality, beliefs, bounded rationality and environment axes.
- **Opening prompt**: Which type would you trust most for urban driving — and why?
- **Predict**: Which type would you trust most for urban driving? Defend your reason.
- **Activity**: write a reflex rule
- **Uses memory**: current percept + internal model → updated state → action.
- **Rules**: Start with 11 candies. Count is hidden. Each player still takes 1 or 2.
- **Chooses actions by asking**: “Which future gets me to the goal?”
- **Route A**: 20min, Route B:10 Min
- **A goal**: based agent knows that both routes reach home. But to compare speed, cost, safety, or comfort, we need something more — utility

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Slide 1 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on Week 3 Lecture 2 - Agent Types, Slide 1: Agent Types
Simple Reflex • Model-Based • Goal-Based • Utility-Based
Technical + Interactive Lecture Deck
Percept
State
Goal
Utility
Action
Main question: How does an agent choose an action?
Built from W1-L3 ideas: utility, PEAS, rationality, beliefs

> **Q: Summarize the core mechanism of Slide 2 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on Week 3 Lecture 2 - Agent Types, Slide 2: Learning path
We move from simple rules to utility-based rational choice.
1
Simple reflex
current percept only

IF condition → THEN action
2
Model-based
percept + memory/state

update internal model, then act
3
Goal-based
model + target goal

search/

> **Q: Summarize the core mechanism of Slide 3 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on Week 3 Lecture 2 - Agent Types, Slide 3: Agent function: the technical core
An agent maps what it has perceived to what it should do.
f : P* → A
percept sequence
Agent program
implements f using rules, state, goals, or utility
Action
Candy Grab
P*: 11 → 9 → 8
A: take 1 or take 2
Thermostat


> **Q: Summarize the core mechanism of Slide 4 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on Week 3 Lecture 2 - Agent Types, Slide 4: Before choosing an agent type: describe the task
PEAS + environment properties decide how much intelligence the agent needs.
1
Describe the task using PEAS
P
Performance
what success/reward means
E
Environment
everything outside the agent
A
Actuators

---

## CS-272-Artificial_Intelligence_A_2K25-BSAI-2 - Lab 4 - Uninformed Search

### 📝 Executive Summary
This lecture on 'Lab 4 - Uninformed Search' covers key fundamentals across 13 slides/sections. Major themes include Page 1, Page 2, Page 3, Page 4. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **CS272**: Artificial Intelligence
- **Lab 4**: Uninformed Search (CLO 4)
- **Date**: September 29th, 2026
- **Note**: You can work in groups of 2 but not more than 2.
- **Deliverables**: Submit search.py and a report document with screenshots of your results (see
- **Deadline**: Will be decided at the end of the lab
- **State**: a compact description of one situation in the search. For the basic maze problems in this lab, a
- **Example**: if Pacman is at (5, 5) and can only move South or West, getSuccessors((5, 5)) would return
- **Search node**: a state together with the path of actions used to reach it, for example ((5, 4), ["South"]).
- **Expanding a state**: removing it from the fringe, checking whether it is the goal, and adding its

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Page 1 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on Lab 4 - Uninformed Search, p.1: Page 1 
 
 
CS272: Artificial Intelligence   
 
Fall 2026 
 
 
 
 
 
 
Department of Computing 
 
CS-272 Artificial Intelligence 
BSAI 2K25 
 
Lab 4: Uninformed Search (CLO 4) 
 
Date: September 29th, 2026 
Time: 14:00 - 17:00  
 
Instructor: Sadia S

> **Q: Summarize the core mechanism of Page 2 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on Lab 4 - Uninformed Search, p.2: Page 2 
 
 
CS272: Artificial Intelligence   
 
Fall 2026 
 
 
Lab 4: Uninformed Search 
 
Implement Questions 1 and 2, which are given below. 
 
Note: You can work in groups of 2 but not more than 2. 
Deliverables: Submit search.py and a report docu

> **Q: Summarize the core mechanism of Page 3 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on Lab 4 - Uninformed Search, p.3: Page 3 
 
 
CS272: Artificial Intelligence   
 
Fall 2026 
developed by the University of California, Berkeley.  
 
Original materials are available at:   
https://inst.eecs.berkeley.edu/~cs188/sp26/projects/proj1/#welcome-to-pacman .  
 
This versio

> **Q: Summarize the core mechanism of Page 4 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on Lab 4 - Uninformed Search, p.4: Page 4 
 
 
CS272: Artificial Intelligence   
 
Fall 2026 
textDisplay.py 
ASCII graphics for Pacman 
ghostAgents.py 
Agents to control ghosts 
 
keyboardAgents.py 
Keyboard interfaces to control Pacman 
layout.py 
Code for reading layout files and s

---

## CS-272-Artificial_Intelligence_A_2K25-BSAI-2 - Lab 1  2 - Introduction to Python.pdf

### 📝 Executive Summary
This lecture on 'Lab 1  2 - Introduction to Python.pdf' covers key fundamentals across 28 slides/sections. Major themes include CS 272: Artificial Intelligence, CS 272: Artificial Intelligence, CS 272: Artificial Intelligence, CS 272: Artificial Intelligence. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **CS 272**: Artificial Intelligence
- **Date**: September 8th, 2026
- **Lab 1 and 2**: Introduction to Python
- **Note**: you may have to type python3.11 or python3.10 rather than python, depending on your
- **There are many built**: in methods which allow you to manipulate strings.
- **TypeError**: 'tuple' object does not support item assignment
- **The last built**: in data structure is the dictionary which stores a map from one type of object (the key)
- **The file**: reading techniques here work for plain text, but later labs in this course will often load
- **Many AI algorithms**: dynamic programming tables, search-state grids, cost matrices, and adjacency
- **ModuleNotFoundError**: No module named 'shop'

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of CS 272: Artificial Intelligence and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on Lab 1  2 - Introduction to Python.pdf, p.1: CS 272: Artificial Intelligence    
 
 
 
 
               
Fall 2026 
 
 
 
 
 
 
Department of Computing 
 
 
CS-272 Artificial Intelligence 
BSAI 2K25 
 
 
Lab Week 1 and 2: Introduction to Python (CLO 4) 
 
 
Date: September 8th, 2026 
September 

> **Q: Summarize the core mechanism of CS 272: Artificial Intelligence and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on Lab 1  2 - Introduction to Python.pdf, p.2: CS 272: Artificial Intelligence    
 
 
 
 
               
Fall 2026 
 
 
Lab 1 and 2: Introduction to Python 
Introduction: 
The purpose of this lab is to get familiar with Python programming language. 
Objectives: 
By the end of this lab, students

> **Q: Summarize the core mechanism of CS 272: Artificial Intelligence and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on Lab 1  2 - Introduction to Python.pdf, p.3: CS 272: Artificial Intelligence    
 
 
 
 
               
Fall 2026 
 
 
Step 1: Install Python 
1. Go to https://www.python.org/downloads/ and download the latest Python 3.14.7 installer for your 
operating system (Windows/macOS/Linux). 
2. Run th

> **Q: Summarize the core mechanism of CS 272: Artificial Intelligence and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on Lab 1  2 - Introduction to Python.pdf, p.4: CS 272: Artificial Intelligence    
 
 
 
 
               
Fall 2026 
 
 
1. Invoking the Interpreter: 
Python can be run in one of two modes. It can either be used interactively, via an interpreter, or it 
can be called from the command line to exe

---

## CS-272-Artificial_Intelligence_A_2K25-BSAI-2 - CS272_Week5_Informed_Search_051026.pdf

### 📝 Executive Summary
This lecture on 'CS272_Week5_Informed_Search_051026.pdf' covers key fundamentals across 25 slides/sections. Major themes include CS272 Artificial Intelligence, CS272 Artificial Intelligence, CS272 Artificial Intelligence, CS272 Artificial Intelligence. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **CS272**: Artificial Intelligence
- **Key idea**: search algorithms mainly differ in how they organize and select nodes from the fringe/frontier.
- **Recap**: Uninformed Search (DFS vs BFS)
- **Memory contrast**: DFS stores a narrow path plus siblings; BFS stores a broad level of the tree.
- **Primary source**: UC Berkeley CS188 Introduction to Artificial Intelligence lecture material by Dan Klein, Pieter Abbeel,
- **Course site**: ai.berkeley.edu / inst.eecs.berkeley.edu/~cs188
- **Lecture theme**: Informed Search — Heuristics, Greedy Search, A* Search, Admissibility, Consistency, and Graph Search.

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of CS272 Artificial Intelligence and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on CS272_Week5_Informed_Search_051026.pdf, p.1: CS272 Artificial Intelligence
Week 5
CS272: Artificial Intelligence
Week 5 Lectures
Informed Search
Heuristics, Greedy Search, and A* Search
Instructor: Dr. Sadia Shakil
Department of Computing, SEECS
(adapted from slides created by Dan Klein and Pie

> **Q: Summarize the core mechanism of CS272 Artificial Intelligence and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on CS272_Week5_Informed_Search_051026.pdf, p.2: CS272 Artificial Intelligence
Week 5
Lecture Roadmap
1. Recap: Uninformed Search (DFS vs BFS)
2. Iterative Deepening
3. Cost-Sensitive Search (Uniform Cost Search)
4. Informed Search (Heuristics, Greedy Search, A* 
Search)

> **Q: Summarize the core mechanism of CS272 Artificial Intelligence and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on CS272_Week5_Informed_Search_051026.pdf, p.3: CS272 Artificial Intelligence
Week 5
Recap: Search Terms
Core vocabulary for search problem formulation and uninformed search algorithms.
Search Problem
• State: abstract world 
configuration
• State space: all possible states
• Initial state 𝒔₀: whe

> **Q: Summarize the core mechanism of CS272 Artificial Intelligence and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on CS272_Week5_Informed_Search_051026.pdf, p.4: CS272 Artificial Intelligence
Week 5
Recap: Search

---

## CS-272-Artificial_Intelligence_A_2K25-BSAI-2 - CS272_Week4_Lecures_final.pdf

### 📝 Executive Summary
This lecture on 'CS272_Week4_Lecures_final.pdf' covers key fundamentals across 67 slides/sections. Major themes include CS272 Artificial Intelligence, CS272 Artificial Intelligence, CS272 Artificial Intelligence, CS272 Artificial Intelligence. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **CS272**: Artificial Intelligence
- **US Berkley Course**: CS 188 Spring 2026 | Introduction to Artificial Intelligence at UC Berkeley
- **Common thread**: using machine learning to extract structure from complex biomedical and
- **Website**: Home | Biosignal Processing and Computational Neuroscience Lab
- **A solution**: sequence of actions (a plan) which transforms the
- **Example**: Traveling in Romania
- **Note**: State space are not moving all the positions on a grid, and they don’t include the history of all the
- **Quiz**: State Space Graphs vs Search Trees
- **Since a state**: space graph counts unique state, whereas a search tree counts paths.
- **Depth**: First Search (DFS): expands the deepest node first

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of CS272 Artificial Intelligence and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on CS272_Week4_Lecures_final.pdf, p.1: CS272 Artificial Intelligence
Week 4
CS272: Artificial Intelligence
Week 4 Lectures
Search and Uninformed Search
Department of Computing, SEECS
Instructor: Dr. Sadia Shakil
(adapted from slides created by Dan Klein and Pieter Abbeel for CS188 Intro t

> **Q: Summarize the core mechanism of CS272 Artificial Intelligence and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on CS272_Week4_Lecures_final.pdf, p.2: CS272 Artificial Intelligence 
 
 
Week 4
Lecture’s Roadmap
1. Recap: Rational, Reflex, and Planning Agents
2. Search Problem Formulation
3. State Spaces, State-Space Graphs, and Search 
Trees
4. General Tree Search and the Fringe
5. Uninformed Searc

> **Q: Summarize the core mechanism of CS272 Artificial Intelligence and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on CS272_Week4_Lecures_final.pdf, p.3: CS272 Artificial Intelligence 
 
 
Week 4
Course information
Name
Email
Office (contact 
number)
Lecturer/Instructor
Dr. Sadia Shakil
sadia.shakil@see
cs.edu.pk
Lab Engineer
Ms. Areeba 
Munir
areeba.munir@se
ecs.edu.pk
Assessment*
Percentage
Theory: 

> **Q: Summarize the core mechanism of CS272 Artificial Intelligence and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on CS272_Week4_Lecures_final.pdf, p.4: CS272 Artificial Intelligence 
 
 
Week 4
Books & Acknoweldgement
Textbook: 
1. Russell, S. J., & Norvig, P. (2021). Artificial Intelligence: A Modern 
Approach, 4th Edition, Pearson.
Reference Book:
1. Boden, M. A. (2018). Artificial Intelligence: A

---

## CS-272-Artificial_Intelligence_A_2K25-BSAI-2 - Lab 3 - Python Libraries and NumPy.pdf

### 📝 Executive Summary
This lecture on 'Lab 3 - Python Libraries and NumPy.pdf' covers key fundamentals across 23 slides/sections. Major themes include CS 272: Artificial Intelligence, CS 272: Artificial Intelligence, CS 272: Artificial Intelligence, CS 272: Artificial Intelligence. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **CS 272**: Artificial Intelligence
- **Lab Week 3**: Python Libraries and NumPy Foundation
- **Date**: September 22nd, 2026
- **Perform element**: wise arithmetic and understand basic broadcasting
- **A library**: broader term for a large suite of code - a toolkit built to solve bigger, higher-level
- **Standard Library**: built-in tools that ship with Python (os, sys, datetime)
- **Third-party libraries**: external tools built by the community (requests, Django,
- **Note**: You will see import numpy as np and import pandas as pd in almost every notebook you ever read.
- **Example 3**: Importing specific names
- **Example 4**: More from the random module

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of CS 272: Artificial Intelligence and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on Lab 3 - Python Libraries and NumPy.pdf, p.1: CS 272: Artificial Intelligence    
 
 
 
 
               
Fall 2026 
 
 
 
 
 
 
 
 
 
 
Department of Computing 
 
 
CS-272 Artificial Intelligence 
BSAI 2K25 
 
 
Lab Week 3: Python Libraries and NumPy Foundation 
 
 
Date: September 22nd, 2026 


> **Q: Summarize the core mechanism of CS 272: Artificial Intelligence and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on Lab 3 - Python Libraries and NumPy.pdf, p.2: CS 272: Artificial Intelligence    
 
 
 
 
               
Fall 2026 
 
 
 
 
Lab Week 3: Python Libraries and NumPy Foundation 
 
1. Introduction:  
So far you have learned the building blocks of Python: variables, data types, conditionals, loops, 

> **Q: Summarize the core mechanism of CS 272: Artificial Intelligence and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on Lab 3 - Python Libraries and NumPy.pdf, p.3: CS 272: Artificial Intelligence    
 
 
 
 
               
Fall 2026 
 
 
 
Use aggregate functions (sum, mean, min, max, std) along a chosen axis 
 
Filter data using boolean masks and conditions 
 
Sort arrays and retrieve the order of elements

> **Q: Summarize the core mechanism of CS 272: Artificial Intelligence and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on Lab 3 - Python Libraries and NumPy.pdf, p.4: CS 272: Artificial Intelligence    
 
 
 
 
               
Fall 2026 
 
 
features. All three exist for the same reason — so you can reuse pre-written code instead of writing everything from 
scratch. 
Concept 
What It Is 
Analogy 
Example 
Module 


---

## CS-272-Artificial_Intelligence_A_2K25-BSAI-2 - CS-272 Artificial Intelligence Fall 2026 Course Outline.pdf

### 📝 Executive Summary
This lecture on 'CS-272 Artificial Intelligence Fall 2026 Course Outline.pdf' covers key fundamentals across 5 slides/sections. Major themes include COURSE OUTLINE, CLO, Week 6, Assessment Methods:. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Lecture Day**: Monday (1400 to 1600 hrs in CR#23 Acad Block)
- **Lab Day**: Tuesday (1400 to 1700 hrs in CR#12 Acad Block)
- **Conducted through in**: class or lab activities.
- **Game Theory - I**: Zero-Sum Games, Minimax,
- **Game Theory - II**: Simultaneous Games, Non-Zero-Sum
- **Responsible and Ethical AI**: Explainability, Uncertainty,
- **Mid**: Semester Exam / No Regular Lab
- **End**: Semester Exam (40-50%)
- **Quiz Policy**: The quizzes will be unannounced / announced and normally last for ten minutes. The question
- **Project Policy**: Students will be required to develop a project during the course which should be completed

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of COURSE OUTLINE and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on CS-272 Artificial Intelligence Fall 2026 Course Outline.pdf, p.1: COURSE OUTLINE 
Department: 
Faculty of Computing 
Knowledge Group:  
Vision and Machine Learning 
Programme: 
Computer Science 
Class: 
BSCS-13AB 
Course code: 
CS-272 
Academic Session/Semester:    Fall 2024/3rd  
Course name: 
Artificial Intellige

> **Q: Summarize the core mechanism of CLO and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on CS-272 Artificial Intelligence Fall 2026 Course Outline.pdf, p.2: CLO 
2 
Apply Artificial Intelligence 
techniques to solve 
computational problems in 
different domains. 
NA 
GA-2 
C-3 
(Apply) 
Active Learning, 
Blended 
Learning 
Quizzes 
Assignments 
MSE 
ESE 
CLO 
3 
Analyze different AI approaches 
for reaso

> **Q: Summarize the core mechanism of Week 6 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on CS-272 Artificial Intelligence Fall 2026 Course Outline.pdf, p.3: Week 6 
Introduction to Probability and Bayesian Networks 
Quiz 2 
Week 7 
Hidden Markov Models, Forward-backward algorithm 
Project Floated 
Week 8 
Markov Decision Processes and 
Introduction 
to 
Reinforcement Learning 
Project Proposal Submission

> **Q: Summarize the core mechanism of Assessment Methods: and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on CS-272 Artificial Intelligence Fall 2026 Course Outline.pdf, p.4: Assessment Methods: 
The final grade is computed from the theory (75 %) and laboratory (25 %) components using the 
weightages given below and awarded according to the NUST relative grading policy notified by the 
Examination Branch. Marks for every 

---

## CS-272-Artificial_Intelligence_A_2K25-BSAI-2 - W2L1.pptx

### 📝 Executive Summary
This lecture on 'W2L1.pptx' covers key fundamentals across 36 slides/sections. Major themes include Slide 1, Slide 2, Slide 3, Slide 4. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Goal of AI**: To build robust, fully autonomous agents in the real world.
- **Definition of AI**: It is a science and a set of computational technologies that are inspired by – but typically operate quite differently from – the ways people use their nervous systems and bodies to sense, learn, reas
- **Use PEAS and task**: environment properties.
- **Warm-up**: Sci‑Fi AI vs Real AI
- **AI in movies**: hook; AI in this course is about decisions, goals, and environments.
- **Human**: like robots, emotions, consciousness, super-intelligence, dramatic autonomy.
- **Use two rounds**: first discover, then explain, then replay.
- **Round 2**: use a planned strategy.
- **Lose**: any move gives opponent a win
- **Winning idea**: always leave a multiple of 3.

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Slide 1 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on W2L1.pptx, Slide 1: CS-370 
Week 2From Candy Game to Intelligent Agents

> **Q: Summarize the core mechanism of Slide 2 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on W2L1.pptx, Slide 2: History of AI
Goal of AI: To build robust, fully autonomous agents in the real world.
Definition of AI: It is a science and a set of computational technologies that are inspired by – but typically operate quite differently from – the ways people use 

> **Q: Summarize the core mechanism of Slide 3 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on W2L1.pptx, Slide 3: Today’s learning outcomes
By the end of this class, students should be able to…
Define AI
Explain AI as machines/programs that act intelligently to achieve goals.
Model a problem
Identify state, actions, transition, goal, and utility.
Describe agents

> **Q: Summarize the core mechanism of Slide 4 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on W2L1.pptx, Slide 4: Warm-up: Sci‑Fi AI vs Real AI
AI in movies is a hook; AI in this course is about decisions, goals, and environments.
🎬
Sci‑Fi AI
Usually shown as
Human-like robots, emotions, consciousness, super-intelligence, dramatic autonomy.
🧠
Course AI
We focus 

---

## CS-272-Artificial_Intelligence_A_2K25-BSAI-2 - W1L1.pptx

### 📝 Executive Summary
This lecture on 'W1L1.pptx' covers key fundamentals across 46 slides/sections. Major themes include Slide 1, What is AI?, What makes humans intelligent?, What makes humans intelligent?. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Autonomy**: A human acts and make decisions on their own
- **Adaptivity**: A human learns from experience and improves
- **Generates complete songs**: including vocals, instruments, lyrics, and even artwork—from simple text prompts.
- **Making a website**: lot easier now, thanks to AI website builders. Big players in the industry, such as Wix and Hostinger, have started offering services to streamline the process. You can answer a few questions through 
- **Bottom left**: act like people --- actually very early definition, dating back to Alan Turing --- Turing test;  problem to do really well you start focusing on things like don’t answer too quickly what the square ro
- **Problem**: Turing test is not reproducible or amenable to mathematical analysis

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Slide 1 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on W1L1.pptx, Slide 1: CS-370  
Week 1

> **Q: Summarize the core mechanism of What is AI? and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on W1L1.pptx, Slide 3: What is AI?

> **Q: Summarize the core mechanism of What makes humans intelligent? and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on W1L1.pptx, Slide 4: What makes humans intelligent?

> **Q: Summarize the core mechanism of What makes humans intelligent? and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on W1L1.pptx, Slide 5: What makes humans intelligent?
Human intelligence is complex, but we can look at two key traits:

Autonomy: A human acts and make decisions on their own

Adaptivity: A human learns from experience and improves

---

## CS-272-Artificial_Intelligence_A_2K25-BSAI-2 - W2L2.pptx

### 📝 Executive Summary
This lecture on 'W2L2.pptx' covers key fundamentals across 15 slides/sections. Major themes include Slide 1, Slide 2, Slide 3, Slide 4. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Lecture 3**: Agents, Rationality & PEAS  |  1
- **Small world**: candies, turns, win/lose
- **Expected answer**: Because even a simple game has state, actions, goal, and a decision strategy.
- **AI goal**: build agents that can act in the real world
- **Before we continue**: what does PEAS stand for?
- **The core idea**: an agent receives information and takes action.
- **For Candy Game**: what is the environment, percept, and action?
- **Candy example**: "7 candies remain".
- **Example**: robotic vacuum-cleaning agent
- **Yes**: because the outcome may depend on hidden information, chance, or another agent.

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Slide 1 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on W2L2.pptx, Slide 1: CS-370 - Lecture 3
Agents, Rationality, and PEAS
Perceive
Decide
Act
Evaluate
Lecture 3 - Agents, Rationality & PEAS  |  1

> **Q: Summarize the core mechanism of Slide 2 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on W2L2.pptx, Slide 2: Where this lecture fits
From a small game to real-world AI systems
Candy Game
Small world: candies, turns, win/lose
Agent
A system that perceives and acts
Rationality
Chooses action expected to work best
PEAS
Describes the task before coding
ASK STUD

> **Q: Summarize the core mechanism of Slide 3 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on W2L2.pptx, Slide 3: Quick recap from last lecture
AI goal: build agents that can act in the real world
AI systems sense, learn, reason, and take action
In this course, we focus on agents that act rationally
PEAS helps us describe an AI task before designing the agent
QU

> **Q: Summarize the core mechanism of Slide 4 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on W2L2.pptx, Slide 4: Agent and environment
The core idea: an agent receives information and takes action.
AGENT
chooses an action
ENVIRONMENT
world/problem around the agent
Percepts / input
Actions / output
ASK STUDENTS
For Candy Game: what is the environment, percept, a

---

## CS-272-Artificial_Intelligence_A_2K25-BSAI-2 - Lab 5 - Informed Search

### 📝 Executive Summary
This lecture on 'Lab 5 - Informed Search' covers key fundamentals across 13 slides/sections. Major themes include Page 1, Page 2, Page 3, Page 4. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **CS272**: Artificial Intelligence
- **Lab 5**: Informed Search (CLO 4)
- **Note**: You can work in groups of 2 but not more than 2.
- **Deliverables**: Submit search.py and a report document with screenshots of your results (see
- **Deadline**: Will be decided at the end of the lab
- **a heuristic**: function heuristic(state, problem) that returns a number. nullHeuristic in search.py
- **Priority**: the fringe is now a util.PriorityQueue, which always gives back the state with the lowest
- **Greedy search**: priority = h(n)
- **Admissible heuristic**: a heuristic that never overestimates the true remaining cost. When every step
- **Consistent heuristic**: a heuristic where, for every step from n to n', h(n) is no more than the step cost

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Page 1 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on Lab 5 - Informed Search, p.1: Page 1 
 
 
CS272: Artificial Intelligence   
 
Fall 2026 
 
 
 
 
 
 
Department of Computing 
 
CS-272 Artificial Intelligence 
BSAI 2K25 
 
Lab 5: Informed Search (CLO 4) 
 
Date: October 6th, 2026 
Time: 14:00 - 17:00  
 
Instructor: Sadia Shakil

> **Q: Summarize the core mechanism of Page 2 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on Lab 5 - Informed Search, p.2: Page 2 
 
 
CS272: Artificial Intelligence   
 
Fall 2026 
 
 
Lab 5: Informed Search 
 
Implement Questions 1, 2 and 3, which are given below. 
 
Note: You can work in groups of 2 but not more than 2. 
Deliverables: Submit search.py and a report doc

> **Q: Summarize the core mechanism of Page 3 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on Lab 5 - Informed Search, p.3: Page 3 
 
 
CS272: Artificial Intelligence   
 
Fall 2026 
understand in order to complete the assignment, and some of which you can ignore. You can 
download all the code and supporting files from LMS. 
 
 
Attribution: 
This lab is adapted from the

> **Q: Summarize the core mechanism of Page 4 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on Lab 5 - Informed Search, p.4: Page 4 
 
 
CS272: Artificial Intelligence   
 
Fall 2026 
Supporting files you can ignore: 
graphicsDisplay.py 
Graphics for Pacman 
graphicsUtils.py 
Support for Pacman graphics 
textDisplay.py 
ASCII graphics for Pacman 
ghostAgents.py 
Agents to 

---

## CS-272-Artificial_Intelligence_A_2K25-BSAI-2 - Week 3 Lecture 2 - Agent Types

### 📝 Executive Summary
This lecture on 'Week 3 Lecture 2 - Agent Types' covers key fundamentals across 16 slides/sections. Major themes include Slide 1, Slide 2, Slide 3, Slide 4. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Main question**: How does an agent choose an action?
- **Built from W1-L3 ideas**: utility, PEAS, rationality, beliefs, bounded rationality and environment axes.
- **Opening prompt**: Which type would you trust most for urban driving — and why?
- **Predict**: Which type would you trust most for urban driving? Defend your reason.
- **Activity**: write a reflex rule
- **Uses memory**: current percept + internal model → updated state → action.
- **Rules**: Start with 11 candies. Count is hidden. Each player still takes 1 or 2.
- **Chooses actions by asking**: “Which future gets me to the goal?”
- **Route A**: 20min, Route B:10 Min
- **A goal**: based agent knows that both routes reach home. But to compare speed, cost, safety, or comfort, we need something more — utility

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Slide 1 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on Week 3 Lecture 2 - Agent Types, Slide 1: Agent Types
Simple Reflex • Model-Based • Goal-Based • Utility-Based
Technical + Interactive Lecture Deck
Percept
State
Goal
Utility
Action
Main question: How does an agent choose an action?
Built from W1-L3 ideas: utility, PEAS, rationality, beliefs

> **Q: Summarize the core mechanism of Slide 2 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on Week 3 Lecture 2 - Agent Types, Slide 2: Learning path
We move from simple rules to utility-based rational choice.
1
Simple reflex
current percept only

IF condition → THEN action
2
Model-based
percept + memory/state

update internal model, then act
3
Goal-based
model + target goal

search/

> **Q: Summarize the core mechanism of Slide 3 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on Week 3 Lecture 2 - Agent Types, Slide 3: Agent function: the technical core
An agent maps what it has perceived to what it should do.
f : P* → A
percept sequence
Agent program
implements f using rules, state, goals, or utility
Action
Candy Grab
P*: 11 → 9 → 8
A: take 1 or take 2
Thermostat


> **Q: Summarize the core mechanism of Slide 4 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on Week 3 Lecture 2 - Agent Types, Slide 4: Before choosing an agent type: describe the task
PEAS + environment properties decide how much intelligence the agent needs.
1
Describe the task using PEAS
P
Performance
what success/reward means
E
Environment
everything outside the agent
A
Actuators

---

## CS-272-Artificial_Intelligence_A_2K25-BSAI-2 - Lab 4 - Uninformed Search

### 📝 Executive Summary
This lecture on 'Lab 4 - Uninformed Search' covers key fundamentals across 13 slides/sections. Major themes include Page 1, Page 2, Page 3, Page 4. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **CS272**: Artificial Intelligence
- **Lab 4**: Uninformed Search (CLO 4)
- **Date**: September 29th, 2026
- **Note**: You can work in groups of 2 but not more than 2.
- **Deliverables**: Submit search.py and a report document with screenshots of your results (see
- **Deadline**: Will be decided at the end of the lab
- **State**: a compact description of one situation in the search. For the basic maze problems in this lab, a
- **Example**: if Pacman is at (5, 5) and can only move South or West, getSuccessors((5, 5)) would return
- **Search node**: a state together with the path of actions used to reach it, for example ((5, 4), ["South"]).
- **Expanding a state**: removing it from the fringe, checking whether it is the goal, and adding its

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Page 1 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on Lab 4 - Uninformed Search, p.1: Page 1 
 
 
CS272: Artificial Intelligence   
 
Fall 2026 
 
 
 
 
 
 
Department of Computing 
 
CS-272 Artificial Intelligence 
BSAI 2K25 
 
Lab 4: Uninformed Search (CLO 4) 
 
Date: September 29th, 2026 
Time: 14:00 - 17:00  
 
Instructor: Sadia S

> **Q: Summarize the core mechanism of Page 2 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on Lab 4 - Uninformed Search, p.2: Page 2 
 
 
CS272: Artificial Intelligence   
 
Fall 2026 
 
 
Lab 4: Uninformed Search 
 
Implement Questions 1 and 2, which are given below. 
 
Note: You can work in groups of 2 but not more than 2. 
Deliverables: Submit search.py and a report docu

> **Q: Summarize the core mechanism of Page 3 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on Lab 4 - Uninformed Search, p.3: Page 3 
 
 
CS272: Artificial Intelligence   
 
Fall 2026 
developed by the University of California, Berkeley.  
 
Original materials are available at:   
https://inst.eecs.berkeley.edu/~cs188/sp26/projects/proj1/#welcome-to-pacman .  
 
This versio

> **Q: Summarize the core mechanism of Page 4 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on Lab 4 - Uninformed Search, p.4: Page 4 
 
 
CS272: Artificial Intelligence   
 
Fall 2026 
textDisplay.py 
ASCII graphics for Pacman 
ghostAgents.py 
Agents to control ghosts 
 
keyboardAgents.py 
Keyboard interfaces to control Pacman 
layout.py 
Code for reading layout files and s

---

## CS-272-Artificial_Intelligence_A_2K25-BSAI-2 - Lab 1  2 - Introduction to Python.pdf

### 📝 Executive Summary
This lecture on 'Lab 1  2 - Introduction to Python.pdf' covers key fundamentals across 28 slides/sections. Major themes include CS 272: Artificial Intelligence, CS 272: Artificial Intelligence, CS 272: Artificial Intelligence, CS 272: Artificial Intelligence. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **CS 272**: Artificial Intelligence
- **Date**: September 8th, 2026
- **Lab 1 and 2**: Introduction to Python
- **Note**: you may have to type python3.11 or python3.10 rather than python, depending on your
- **There are many built**: in methods which allow you to manipulate strings.
- **TypeError**: 'tuple' object does not support item assignment
- **The last built**: in data structure is the dictionary which stores a map from one type of object (the key)
- **The file**: reading techniques here work for plain text, but later labs in this course will often load
- **Many AI algorithms**: dynamic programming tables, search-state grids, cost matrices, and adjacency
- **ModuleNotFoundError**: No module named 'shop'

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of CS 272: Artificial Intelligence and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on Lab 1  2 - Introduction to Python.pdf, p.1: CS 272: Artificial Intelligence    
 
 
 
 
               
Fall 2026 
 
 
 
 
 
 
Department of Computing 
 
 
CS-272 Artificial Intelligence 
BSAI 2K25 
 
 
Lab Week 1 and 2: Introduction to Python (CLO 4) 
 
 
Date: September 8th, 2026 
September 

> **Q: Summarize the core mechanism of CS 272: Artificial Intelligence and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on Lab 1  2 - Introduction to Python.pdf, p.2: CS 272: Artificial Intelligence    
 
 
 
 
               
Fall 2026 
 
 
Lab 1 and 2: Introduction to Python 
Introduction: 
The purpose of this lab is to get familiar with Python programming language. 
Objectives: 
By the end of this lab, students

> **Q: Summarize the core mechanism of CS 272: Artificial Intelligence and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on Lab 1  2 - Introduction to Python.pdf, p.3: CS 272: Artificial Intelligence    
 
 
 
 
               
Fall 2026 
 
 
Step 1: Install Python 
1. Go to https://www.python.org/downloads/ and download the latest Python 3.14.7 installer for your 
operating system (Windows/macOS/Linux). 
2. Run th

> **Q: Summarize the core mechanism of CS 272: Artificial Intelligence and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on Lab 1  2 - Introduction to Python.pdf, p.4: CS 272: Artificial Intelligence    
 
 
 
 
               
Fall 2026 
 
 
1. Invoking the Interpreter: 
Python can be run in one of two modes. It can either be used interactively, via an interpreter, or it 
can be called from the command line to exe

---

## CS-272-Artificial_Intelligence_A_2K25-BSAI-2 - CS272_Week5_Informed_Search_051026.pdf

### 📝 Executive Summary
This lecture on 'CS272_Week5_Informed_Search_051026.pdf' covers key fundamentals across 25 slides/sections. Major themes include CS272 Artificial Intelligence, CS272 Artificial Intelligence, CS272 Artificial Intelligence, CS272 Artificial Intelligence. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **CS272**: Artificial Intelligence
- **Key idea**: search algorithms mainly differ in how they organize and select nodes from the fringe/frontier.
- **Recap**: Uninformed Search (DFS vs BFS)
- **Memory contrast**: DFS stores a narrow path plus siblings; BFS stores a broad level of the tree.
- **Primary source**: UC Berkeley CS188 Introduction to Artificial Intelligence lecture material by Dan Klein, Pieter Abbeel,
- **Course site**: ai.berkeley.edu / inst.eecs.berkeley.edu/~cs188
- **Lecture theme**: Informed Search — Heuristics, Greedy Search, A* Search, Admissibility, Consistency, and Graph Search.

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of CS272 Artificial Intelligence and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on CS272_Week5_Informed_Search_051026.pdf, p.1: CS272 Artificial Intelligence
Week 5
CS272: Artificial Intelligence
Week 5 Lectures
Informed Search
Heuristics, Greedy Search, and A* Search
Instructor: Dr. Sadia Shakil
Department of Computing, SEECS
(adapted from slides created by Dan Klein and Pie

> **Q: Summarize the core mechanism of CS272 Artificial Intelligence and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on CS272_Week5_Informed_Search_051026.pdf, p.2: CS272 Artificial Intelligence
Week 5
Lecture Roadmap
1. Recap: Uninformed Search (DFS vs BFS)
2. Iterative Deepening
3. Cost-Sensitive Search (Uniform Cost Search)
4. Informed Search (Heuristics, Greedy Search, A* 
Search)

> **Q: Summarize the core mechanism of CS272 Artificial Intelligence and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on CS272_Week5_Informed_Search_051026.pdf, p.3: CS272 Artificial Intelligence
Week 5
Recap: Search Terms
Core vocabulary for search problem formulation and uninformed search algorithms.
Search Problem
• State: abstract world 
configuration
• State space: all possible states
• Initial state 𝒔₀: whe

> **Q: Summarize the core mechanism of CS272 Artificial Intelligence and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on CS272_Week5_Informed_Search_051026.pdf, p.4: CS272 Artificial Intelligence
Week 5
Recap: Search

---

## CS-272-Artificial_Intelligence_A_2K25-BSAI-2 - CS272_Week4_Lecures_final.pdf

### 📝 Executive Summary
This lecture on 'CS272_Week4_Lecures_final.pdf' covers key fundamentals across 67 slides/sections. Major themes include CS272 Artificial Intelligence, CS272 Artificial Intelligence, CS272 Artificial Intelligence, CS272 Artificial Intelligence. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **CS272**: Artificial Intelligence
- **US Berkley Course**: CS 188 Spring 2026 | Introduction to Artificial Intelligence at UC Berkeley
- **Common thread**: using machine learning to extract structure from complex biomedical and
- **Website**: Home | Biosignal Processing and Computational Neuroscience Lab
- **A solution**: sequence of actions (a plan) which transforms the
- **Example**: Traveling in Romania
- **Note**: State space are not moving all the positions on a grid, and they don’t include the history of all the
- **Quiz**: State Space Graphs vs Search Trees
- **Since a state**: space graph counts unique state, whereas a search tree counts paths.
- **Depth**: First Search (DFS): expands the deepest node first

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of CS272 Artificial Intelligence and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on CS272_Week4_Lecures_final.pdf, p.1: CS272 Artificial Intelligence
Week 4
CS272: Artificial Intelligence
Week 4 Lectures
Search and Uninformed Search
Department of Computing, SEECS
Instructor: Dr. Sadia Shakil
(adapted from slides created by Dan Klein and Pieter Abbeel for CS188 Intro t

> **Q: Summarize the core mechanism of CS272 Artificial Intelligence and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on CS272_Week4_Lecures_final.pdf, p.2: CS272 Artificial Intelligence 
 
 
Week 4
Lecture’s Roadmap
1. Recap: Rational, Reflex, and Planning Agents
2. Search Problem Formulation
3. State Spaces, State-Space Graphs, and Search 
Trees
4. General Tree Search and the Fringe
5. Uninformed Searc

> **Q: Summarize the core mechanism of CS272 Artificial Intelligence and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on CS272_Week4_Lecures_final.pdf, p.3: CS272 Artificial Intelligence 
 
 
Week 4
Course information
Name
Email
Office (contact 
number)
Lecturer/Instructor
Dr. Sadia Shakil
sadia.shakil@see
cs.edu.pk
Lab Engineer
Ms. Areeba 
Munir
areeba.munir@se
ecs.edu.pk
Assessment*
Percentage
Theory: 

> **Q: Summarize the core mechanism of CS272 Artificial Intelligence and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on CS272_Week4_Lecures_final.pdf, p.4: CS272 Artificial Intelligence 
 
 
Week 4
Books & Acknoweldgement
Textbook: 
1. Russell, S. J., & Norvig, P. (2021). Artificial Intelligence: A Modern 
Approach, 4th Edition, Pearson.
Reference Book:
1. Boden, M. A. (2018). Artificial Intelligence: A

---

## CS-272-Artificial_Intelligence_A_2K25-BSAI-2 - Lab 3 - Python Libraries and NumPy.pdf

### 📝 Executive Summary
This lecture on 'Lab 3 - Python Libraries and NumPy.pdf' covers key fundamentals across 23 slides/sections. Major themes include CS 272: Artificial Intelligence, CS 272: Artificial Intelligence, CS 272: Artificial Intelligence, CS 272: Artificial Intelligence. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **CS 272**: Artificial Intelligence
- **Lab Week 3**: Python Libraries and NumPy Foundation
- **Date**: September 22nd, 2026
- **Perform element**: wise arithmetic and understand basic broadcasting
- **A library**: broader term for a large suite of code - a toolkit built to solve bigger, higher-level
- **Standard Library**: built-in tools that ship with Python (os, sys, datetime)
- **Third-party libraries**: external tools built by the community (requests, Django,
- **Note**: You will see import numpy as np and import pandas as pd in almost every notebook you ever read.
- **Example 3**: Importing specific names
- **Example 4**: More from the random module

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of CS 272: Artificial Intelligence and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on Lab 3 - Python Libraries and NumPy.pdf, p.1: CS 272: Artificial Intelligence    
 
 
 
 
               
Fall 2026 
 
 
 
 
 
 
 
 
 
 
Department of Computing 
 
 
CS-272 Artificial Intelligence 
BSAI 2K25 
 
 
Lab Week 3: Python Libraries and NumPy Foundation 
 
 
Date: September 22nd, 2026 


> **Q: Summarize the core mechanism of CS 272: Artificial Intelligence and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on Lab 3 - Python Libraries and NumPy.pdf, p.2: CS 272: Artificial Intelligence    
 
 
 
 
               
Fall 2026 
 
 
 
 
Lab Week 3: Python Libraries and NumPy Foundation 
 
1. Introduction:  
So far you have learned the building blocks of Python: variables, data types, conditionals, loops, 

> **Q: Summarize the core mechanism of CS 272: Artificial Intelligence and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on Lab 3 - Python Libraries and NumPy.pdf, p.3: CS 272: Artificial Intelligence    
 
 
 
 
               
Fall 2026 
 
 
 
Use aggregate functions (sum, mean, min, max, std) along a chosen axis 
 
Filter data using boolean masks and conditions 
 
Sort arrays and retrieve the order of elements

> **Q: Summarize the core mechanism of CS 272: Artificial Intelligence and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on Lab 3 - Python Libraries and NumPy.pdf, p.4: CS 272: Artificial Intelligence    
 
 
 
 
               
Fall 2026 
 
 
features. All three exist for the same reason — so you can reuse pre-written code instead of writing everything from 
scratch. 
Concept 
What It Is 
Analogy 
Example 
Module 


---

## CS-272-Artificial_Intelligence_A_2K25-BSAI-2 - CS-272 Artificial Intelligence Fall 2026 Course Outline.pdf

### 📝 Executive Summary
This lecture on 'CS-272 Artificial Intelligence Fall 2026 Course Outline.pdf' covers key fundamentals across 5 slides/sections. Major themes include COURSE OUTLINE, CLO, Week 6, Assessment Methods:. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Lecture Day**: Monday (1400 to 1600 hrs in CR#23 Acad Block)
- **Lab Day**: Tuesday (1400 to 1700 hrs in CR#12 Acad Block)
- **Conducted through in**: class or lab activities.
- **Game Theory - I**: Zero-Sum Games, Minimax,
- **Game Theory - II**: Simultaneous Games, Non-Zero-Sum
- **Responsible and Ethical AI**: Explainability, Uncertainty,
- **Mid**: Semester Exam / No Regular Lab
- **End**: Semester Exam (40-50%)
- **Quiz Policy**: The quizzes will be unannounced / announced and normally last for ten minutes. The question
- **Project Policy**: Students will be required to develop a project during the course which should be completed

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of COURSE OUTLINE and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on CS-272 Artificial Intelligence Fall 2026 Course Outline.pdf, p.1: COURSE OUTLINE 
Department: 
Faculty of Computing 
Knowledge Group:  
Vision and Machine Learning 
Programme: 
Computer Science 
Class: 
BSCS-13AB 
Course code: 
CS-272 
Academic Session/Semester:    Fall 2024/3rd  
Course name: 
Artificial Intellige

> **Q: Summarize the core mechanism of CLO and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on CS-272 Artificial Intelligence Fall 2026 Course Outline.pdf, p.2: CLO 
2 
Apply Artificial Intelligence 
techniques to solve 
computational problems in 
different domains. 
NA 
GA-2 
C-3 
(Apply) 
Active Learning, 
Blended 
Learning 
Quizzes 
Assignments 
MSE 
ESE 
CLO 
3 
Analyze different AI approaches 
for reaso

> **Q: Summarize the core mechanism of Week 6 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on CS-272 Artificial Intelligence Fall 2026 Course Outline.pdf, p.3: Week 6 
Introduction to Probability and Bayesian Networks 
Quiz 2 
Week 7 
Hidden Markov Models, Forward-backward algorithm 
Project Floated 
Week 8 
Markov Decision Processes and 
Introduction 
to 
Reinforcement Learning 
Project Proposal Submission

> **Q: Summarize the core mechanism of Assessment Methods: and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on CS-272 Artificial Intelligence Fall 2026 Course Outline.pdf, p.4: Assessment Methods: 
The final grade is computed from the theory (75 %) and laboratory (25 %) components using the 
weightages given below and awarded according to the NUST relative grading policy notified by the 
Examination Branch. Marks for every 

---

## CS-272-Artificial_Intelligence_A_2K25-BSAI-2 - W2L1.pptx

### 📝 Executive Summary
This lecture on 'W2L1.pptx' covers key fundamentals across 36 slides/sections. Major themes include Slide 1, Slide 2, Slide 3, Slide 4. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Goal of AI**: To build robust, fully autonomous agents in the real world.
- **Definition of AI**: It is a science and a set of computational technologies that are inspired by – but typically operate quite differently from – the ways people use their nervous systems and bodies to sense, learn, reas
- **Use PEAS and task**: environment properties.
- **Warm-up**: Sci‑Fi AI vs Real AI
- **AI in movies**: hook; AI in this course is about decisions, goals, and environments.
- **Human**: like robots, emotions, consciousness, super-intelligence, dramatic autonomy.
- **Use two rounds**: first discover, then explain, then replay.
- **Round 2**: use a planned strategy.
- **Lose**: any move gives opponent a win
- **Winning idea**: always leave a multiple of 3.

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Slide 1 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on W2L1.pptx, Slide 1: CS-370 
Week 2From Candy Game to Intelligent Agents

> **Q: Summarize the core mechanism of Slide 2 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on W2L1.pptx, Slide 2: History of AI
Goal of AI: To build robust, fully autonomous agents in the real world.
Definition of AI: It is a science and a set of computational technologies that are inspired by – but typically operate quite differently from – the ways people use 

> **Q: Summarize the core mechanism of Slide 3 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on W2L1.pptx, Slide 3: Today’s learning outcomes
By the end of this class, students should be able to…
Define AI
Explain AI as machines/programs that act intelligently to achieve goals.
Model a problem
Identify state, actions, transition, goal, and utility.
Describe agents

> **Q: Summarize the core mechanism of Slide 4 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on W2L1.pptx, Slide 4: Warm-up: Sci‑Fi AI vs Real AI
AI in movies is a hook; AI in this course is about decisions, goals, and environments.
🎬
Sci‑Fi AI
Usually shown as
Human-like robots, emotions, consciousness, super-intelligence, dramatic autonomy.
🧠
Course AI
We focus 

---

## CS-272-Artificial_Intelligence_A_2K25-BSAI-2 - W1L1.pptx

### 📝 Executive Summary
This lecture on 'W1L1.pptx' covers key fundamentals across 46 slides/sections. Major themes include Slide 1, What is AI?, What makes humans intelligent?, What makes humans intelligent?. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Autonomy**: A human acts and make decisions on their own
- **Adaptivity**: A human learns from experience and improves
- **Generates complete songs**: including vocals, instruments, lyrics, and even artwork—from simple text prompts.
- **Making a website**: lot easier now, thanks to AI website builders. Big players in the industry, such as Wix and Hostinger, have started offering services to streamline the process. You can answer a few questions through 
- **Bottom left**: act like people --- actually very early definition, dating back to Alan Turing --- Turing test;  problem to do really well you start focusing on things like don’t answer too quickly what the square ro
- **Problem**: Turing test is not reproducible or amenable to mathematical analysis

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Slide 1 and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on W1L1.pptx, Slide 1: CS-370  
Week 1

> **Q: Summarize the core mechanism of What is AI? and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on W1L1.pptx, Slide 3: What is AI?

> **Q: Summarize the core mechanism of What makes humans intelligent? and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on W1L1.pptx, Slide 4: What makes humans intelligent?

> **Q: Summarize the core mechanism of What makes humans intelligent? and how it applies to CS-272-Artificial_Intelligence_A_2K25-BSAI-2.**
>
> *A:* Based on W1L1.pptx, Slide 5: What makes humans intelligent?
Human intelligence is complex, but we can look at two key traits:

Autonomy: A human acts and make decisions on their own

Adaptivity: A human learns from experience and improves

---

