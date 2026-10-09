# 📌 CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2 Executive Formula & Concept Cheat-Sheet

*Auto-generated high-yield review matrix for quick exam cramming.*

## 🔑 Essential Definitions & Vocabulary

| Term | Core Definition |
| :--- | :--- |
| **// Sean's CS106B Pointers Worksheet! Show the contents of variables a, b, p, and** | // Sean's CS106B Pointers Worksheet! Show the contents of variables a, b, p, and q // at the various stages of the program's execution where I've drawn the boxes. #include <iostrea... |
| **A data structure** | way of organising data in memory so that it can be used efficiently. |
| **A recursive function** | loop in disguise. Count how many calls happen, and |
| **AVL Trees** | Rotations and Balancing |
| **An Application** | Balanced Parentheses |
| **An array** | variable that is able to hold multiple values of some type. An array is made up of cells. Each cell holds a |
| **Answer** | ______________________________________________ |
| **Applications of Trees** | Heaps and Priority Queues |
| **Ask** | how many times can I halve n before only one element is left? |
| **Average** | about n/2 comparisons |
| **Best case** | 1 comparison  (it is first) |
| **Big** | O tells you how fast the work grows when the input gets bigger. It does not tell you |
| **COURSE OUTLINE** | CS250 Data Structures and Algorithms |
| **CS-250 Big** | O Worksheet: Every Kind of |
| **Car 1** | Car 1 Thanks to Nick Troccoli for this example! Car 4 Car 5... |
| **Coffee Shop** | Coffee Shop Office Space Residential            ! ptr string* ptr = new string[3]; ptr[0] = "Coffee Shop"; ptr[1] = "Office Space"; ptr[2] = "Residential";... |
| **Collections, Part Two** | Collections, Part Two... |
| **Conducted through in** | class or lab activities. |
| **Deep** | what you must write |
| **Disaster 2** | the dangling pointer |
| **Doubling levels** | 1 + 2 + 4 + … + n = 2n − 1. |
| **Dynamic Allocation: The Basics** | Dynamic Allocation: The Basics... |
| **Equal levels** | log n of them, cn each. |
| **Every row** | genuine trade. There is no column of all wins. Choosing a data structure means deciding which operations you will do most often. |
| **Gain hands** | on experience in programming using the latest Integrated Development |
| **Google Interview Prep** | Google Interview Prep  https://igotanoffer.com/blogs/tech/coding-interview-prep  https://www.youtube.com/c/neetcode  https://neetcode.io/roadmap... |
| **Hour 1** | what you should now be able to say |
| **Hour 2** | what you should now be able to say |
| **Important** | Please note the Stanford Computer Forum policies regarding no- |
| **Introduction** | What is a Data Structure? |
| **It cannot be copied** | only moved. That makes double free impossible by construction. |
| **It says** | p is a pointer to int. |
| **Key idea** | best and worst cases are about which input you get, for the same n. The best |
| **Match the form** | new/delete, new[]/delete[]. |
| **Non-Linear Data Structures I** | Introduction to Trees |

## ⚡ Core Rules, Theorems & Key Mechanics

- **Summarize the core mechanism of Pointers and Arrays and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
  > Based on CS106B Pointers and Arrays.pdf, p.1: Pointers and Arrays
TUESDAY, JULY 21
Today we'll learn about pointers and arrays in C++ as we build up the toolkit we will need to implement awesome
ADTs like vectors and stacks.
📚 Readings: Text 11.1, 11.2, 11.3
📝 Lecture quiz on Canvas
Contents
1. 

- **Summarize the core mechanism of Today's lecture quiz (super important!). and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
  > Based on CS106B Pointers and Arrays.pdf, p.2: Today's lecture quiz (super important!).
Next week's section problems! We have a really great pointer tracing exercise planned.
Arrays
We started class today with a brief overview of arrays. We saw the syntax for creating an array and accessing its
e

- **Summarize the core mechanism of Recall that arrays are one of the fundamental building blocks of the C++ languag and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
  > Based on CS106B Pointers and Arrays.pdf, p.3: Recall that arrays are one of the fundamental building blocks of the C++ language, and they're often used to create
vectors! A vector will often have an array hidden away as a private member variable. If we add more elements than its
array can hold, 

- **Summarize the core mechanism of DATA_TYPE_POINTED_TO  * VARIABLE_NAME ; and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
  > Based on CS106B Pointers and Arrays.pdf, p.4: DATA_TYPE_POINTED_TO  * VARIABLE_NAME ;
For example, to create a variable named p that can hold the address of an integer, the syntax is as follows:
int *p;
Here's that idea in action:
main.cpp
#include <iostream>
#include "console.h"
using namespace

- **Summarize the core mechanism of COURSE OUTLINE- CS250 Data Structures and Algorithms and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
  > Based on Finalized Course Outline, p.1: COURSE OUTLINE- CS250 Data Structures and Algorithms 
 
Department: 
Faculty of Computing Knowledge Group: 
Programming Core 
Programme: 
Artificial Intelligence 
Class: 
BSAI-2 
Course code: 
CS-250 
Academic 
Session/Semester: 
Fall 2026 
Course na

- **Summarize the core mechanism of Mapping of the Course Learning Outcomes (CLO) to the Programme Learning and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
  > Based on Finalized Course Outline, p.2: Mapping of the Course Learning Outcomes (CLO) to the Programme Learning 
Outcomes (PLO), Teaching & Learning (T&L) methods and Assessment methods: 
 
No. 
Course Learning Outcomes 
PLO 
(SE) 
SO 
(CS/DS/AI) 
BT Level 
Teaching & 
Learning 
Methods 
A

- **Summarize the core mechanism of 3. and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
  > Based on Finalized Course Outline, p.3: 3. 
Blended learning 
Conducted through the NUST Learning Management System (LMS), all 
information and materials related to teaching and learning activities will be 
shared with the class via this platform. Additionally, some formative 
assessments 

- **Summarize the core mechanism of Week 14 and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
  > Based on Finalized Course Outline, p.4: Week 14 
 
Hashing and Hash Tables 
 
Collision Resolution Techniques 
Week 15 
 
Graphs I: Introduction and Applications 
 
Graphs II: Representations (Adjacency Matrix/List) 
 
Graphs III: Breadth-First Search (BFS) 
Week 16 
 
Graphs IV: Min

- **Summarize the core mechanism of Dynamic Allocation: The Basics and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
  > Based on Dynamic Allocation, p.1: Dynamic Allocation: The Basics

- **Summarize the core mechanism of string* ptr; and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
  > Based on Dynamic Allocation, p.2: string* ptr;
 
 
 
 
ptr
The variable ptr has type
string*
rather than string. We’ll
explain this in a moment.

- **Summarize the core mechanism of string* ptr; and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
  > Based on Dynamic Allocation, p.3: string* ptr;
ptr = new string[3];
 
 
 
ptr

- **Summarize the core mechanism of string* ptr; and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
  > Based on Dynamic Allocation, p.4: string* ptr;
ptr = new string[3];
 
 
 
ptr
This is an array of three
strings. I’ll represent it
as a three-story building.

- **Summarize the core mechanism of // Sean's CS106B Pointers Worksheet! Show the contents of variables a, b, p, and and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
  > Based on Pointers Worksheet Solution, p.1: // Sean's CS106B Pointers Worksheet! Show the contents of variables a, b, p, and q
// at the various stages of the program's execution where I've drawn the boxes.
#include <iostream>
#include "console.h"
using namespace std;
int main()
{
   int a = 4

- **Summarize the core mechanism of CS-250 · Data Structures & Algorithms and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
  > Based on Time Complexity in Recursion, p.1: CS-250 · Data Structures & Algorithms
Time Complexity 
in Recursion
How to count the cost of a function that calls itself

- **Summarize the core mechanism of The one idea and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
  > Based on Time Complexity in Recursion, p.2: The one idea
Running time = the work done in 
every call, added up.
A recursive function is a loop in disguise. Count how many calls happen, and 
how much work each call does on its own.

