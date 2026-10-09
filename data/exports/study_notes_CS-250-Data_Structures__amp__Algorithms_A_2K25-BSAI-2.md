# 📚 Study Knowledge Base: CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2

*Auto-generated from LMS lecture notes. Compatible with Obsidian & Notion.*

---

## CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2 - CS106B Pointers and Arrays.pdf

### 📝 Executive Summary
This lecture on 'CS106B Pointers and Arrays.pdf' covers key fundamentals across 16 slides/sections. Major themes include Pointers and Arrays, Today's lecture quiz (super important!)., Recall that arrays are one of the fundamental building blocks of the C++ languag, DATA_TYPE_POINTED_TO  * VARIABLE_NAME ;. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Reminder**: Pointers are a topic where doing lots of exercises is more important than ever in order to get comfortable
- **An array**: variable that is able to hold multiple values of some type. An array is made up of cells. Each cell holds a
- **Style Note**: Pointer Declarations
- **The Ampersand Operator**: Different Things in Different Contexts!
- **The Asterisk Operator**: Different Things in Different Contexts!

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Pointers and Arrays and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on CS106B Pointers and Arrays.pdf, p.1: Pointers and Arrays
TUESDAY, JULY 21
Today we'll learn about pointers and arrays in C++ as we build up the toolkit we will need to implement awesome
ADTs like vectors and stacks.
📚 Readings: Text 11.1, 11.2, 11.3
📝 Lecture quiz on Canvas
Contents
1. 

> **Q: Summarize the core mechanism of Today's lecture quiz (super important!). and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on CS106B Pointers and Arrays.pdf, p.2: Today's lecture quiz (super important!).
Next week's section problems! We have a really great pointer tracing exercise planned.
Arrays
We started class today with a brief overview of arrays. We saw the syntax for creating an array and accessing its
e

> **Q: Summarize the core mechanism of Recall that arrays are one of the fundamental building blocks of the C++ languag and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on CS106B Pointers and Arrays.pdf, p.3: Recall that arrays are one of the fundamental building blocks of the C++ language, and they're often used to create
vectors! A vector will often have an array hidden away as a private member variable. If we add more elements than its
array can hold, 

> **Q: Summarize the core mechanism of DATA_TYPE_POINTED_TO  * VARIABLE_NAME ; and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on CS106B Pointers and Arrays.pdf, p.4: DATA_TYPE_POINTED_TO  * VARIABLE_NAME ;
For example, to create a variable named p that can hold the address of an integer, the syntax is as follows:
int *p;
Here's that idea in action:
main.cpp
#include <iostream>
#include "console.h"
using namespace

---

## CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2 - Finalized Course Outline

### 📝 Executive Summary
This lecture on 'Finalized Course Outline' covers key fundamentals across 6 slides/sections. Major themes include COURSE OUTLINE- CS250 Data Structures and Algorithms, Mapping of the Course Learning Outcomes (CLO) to the Programme Learning, 3., Week 14. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **COURSE OUTLINE**: CS250 Data Structures and Algorithms
- **Gain hands**: on experience in programming using the latest Integrated
- **Conducted through in**: class or lab activities.
- **Introduction**: What is a Data Structure?
- **Stacks**: Concept, Implementation, Applications
- **Queues**: Concept, Implementation, Applications
- **Time Complexity II**: Loops and Nested Structures
- **Non-Linear Data Structures I**: Introduction to Trees
- **Tree Traversals**: Inorder, Preorder, Postorder
- **AVL Trees**: Rotations and Balancing

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of COURSE OUTLINE- CS250 Data Structures and Algorithms and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Finalized Course Outline, p.1: COURSE OUTLINE- CS250 Data Structures and Algorithms 
 
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

> **Q: Summarize the core mechanism of Mapping of the Course Learning Outcomes (CLO) to the Programme Learning and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Finalized Course Outline, p.2: Mapping of the Course Learning Outcomes (CLO) to the Programme Learning 
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

> **Q: Summarize the core mechanism of 3. and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Finalized Course Outline, p.3: 3. 
Blended learning 
Conducted through the NUST Learning Management System (LMS), all 
information and materials related to teaching and learning activities will be 
shared with the class via this platform. Additionally, some formative 
assessments 

> **Q: Summarize the core mechanism of Week 14 and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Finalized Course Outline, p.4: Week 14 
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

---

## CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2 - Dynamic Allocation

### 📝 Executive Summary
This lecture on 'Dynamic Allocation' covers key fundamentals across 61 slides/sections. Major themes include Dynamic Allocation: The Basics, string* ptr;, string* ptr;, string* ptr;. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Dynamic Allocation: The Basics**: Dynamic Allocation: The Basics...
- **string* ptr;**: string* ptr;         ptr The variable ptr has type string* rather than string. We’ll explain this in a moment....
- **int* ptr = new int[4];**: int* ptr = new int[4]; ptr Arrays of ints, doubles, chars, or bools initially have garbage values. Other types use good defaults....
- **string* ptr = new string[3];**: string* ptr = new string[3]; ptr...
- **Coffee Shop**: Coffee Shop Office Space Residential            ! ptr string* ptr = new string[3]; ptr[0] = "Coffee Shop"; ptr[1] = "Office Space"; ptr[2] = "Residential";...
- **void makeAnArray() {**: void makeAnArray() {     string* ptr = new string[3]; }   int main() {     for (int i = 0; i < 5; i++) {         makeAnArray();     } }...
- **void makeAnArray() {**: void makeAnArray() {     string* ptr = new string[3]; }   int main() {     for (int i = 0; i < 5; i++) {         makeAnArray();     } }...
- **void makeAnArray() {**: void makeAnArray() {     string* ptr = new string[3]; }   int main() {     for (int i = 0; i < 5; i++) {         makeAnArray();     } }...
- **void makeAnArray() {**: void makeAnArray() {     string* ptr = new string[3]; }   int main() {     for (int i = 0; i < 5; i++) {         makeAnArray();     } }...
- **void makeAnArray() {**: void makeAnArray() {     string* ptr = new string[3]; }   int main() {     for (int i = 0; i < 5; i++) {         makeAnArray();     } }            ! ptr...

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Dynamic Allocation: The Basics and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Dynamic Allocation, p.1: Dynamic Allocation: The Basics

> **Q: Summarize the core mechanism of string* ptr; and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Dynamic Allocation, p.2: string* ptr;
 
 
 
 
ptr
The variable ptr has type
string*
rather than string. We’ll
explain this in a moment.

> **Q: Summarize the core mechanism of string* ptr; and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Dynamic Allocation, p.3: string* ptr;
ptr = new string[3];
 
 
 
ptr

> **Q: Summarize the core mechanism of string* ptr; and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Dynamic Allocation, p.4: string* ptr;
ptr = new string[3];
 
 
 
ptr
This is an array of three
strings. I’ll represent it
as a three-story building.

---

## CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2 - Pointers Worksheet Solution

### 📝 Executive Summary
This lecture on 'Pointers Worksheet Solution' covers key fundamentals across 1 slides/sections. Major themes include // Sean's CS106B Pointers Worksheet! Show the contents of variables a, b, p, and. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **// Sean's CS106B Pointers Worksheet! Show the contents of variables a, b, p, and**: // Sean's CS106B Pointers Worksheet! Show the contents of variables a, b, p, and q // at the various stages of the program's execution where I've drawn the boxes. #include <iostrea...

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of // Sean's CS106B Pointers Worksheet! Show the contents of variables a, b, p, and and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Pointers Worksheet Solution, p.1: // Sean's CS106B Pointers Worksheet! Show the contents of variables a, b, p, and q
// at the various stages of the program's execution where I've drawn the boxes.
#include <iostream>
#include "console.h"
using namespace std;
int main()
{
   int a = 4

---

## CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2 - Josephus Problem

### 📝 Executive Summary
No extractable text found for Josephus Problem.

### 🔑 Key Definitions

### 💡 Core Conceptual Questions
---

## CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2 - Time Complexity in Recursion

### 📝 Executive Summary
This lecture on 'Time Complexity in Recursion' covers key fundamentals across 18 slides/sections. Major themes include CS-250 · Data Structures & Algorithms, The one idea, The method, Step 1. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **A recursive function**: loop in disguise. Count how many calls happen, and
- **The tree**: single line. Each node does constant work c, and
- **Equal levels**: log n of them, cn each.
- **Doubling levels**: 1 + 2 + 4 + … + n = 2n − 1.
- **Root vs leaves**: who does more work?

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of CS-250 · Data Structures & Algorithms and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Time Complexity in Recursion, p.1: CS-250 · Data Structures & Algorithms
Time Complexity 
in Recursion
How to count the cost of a function that calls itself

> **Q: Summarize the core mechanism of The one idea and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Time Complexity in Recursion, p.2: The one idea
Running time = the work done in 
every call, added up.
A recursive function is a loop in disguise. Count how many calls happen, and 
how much work each call does on its own.

> **Q: Summarize the core mechanism of The method and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Time Complexity in Recursion, p.3: The method
Three steps, every time
1
Write the 
recurrence
T(n) = the cost of the calls it 
makes + the work it does itself.
2
Draw the recursion 
tree
One node per call. Write each 
node's own work inside it.
3
Add it up
Sum the work level by level.

> **Q: Summarize the core mechanism of Step 1 and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Time Complexity in Recursion, p.4: Step 1
How to read a recurrence
T(n) = a · T(n/b) + f(n)
a
How many recursive calls each 
call makes
n/b or n − 1
How big each smaller problem is
f(n)
Work done outside the calls: loops, 
comparing, merging
Plus a base case, T(1) = c, that stops the 

---

## CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2 - Big O Worksheet answers

### 📝 Executive Summary
This lecture on 'Big O Worksheet answers' covers key fundamentals across 7 slides/sections. Major themes include Answers & Explanations, See the jump: going from O(n log n) to O(n²) multiplies the work by about 100., E4. About 20 steps; O(log n). 1,000,000 halved 20 times is less than 1, because , Part J: Recursion. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Part A**: Simplify the expression
- **Part B**: Order the growth rates
- **Why**: constants never grow. Logs grow very slowly (doubling n adds just 1). √n is slower
- **See the jump**: going from O(n log n) to O(n²) multiplies the work by about 100.
- **Part F**: Quadratic and cubic time
- **Part K**: Best case and worst case
- **Key idea**: best and worst cases are about which input you get, for the same n. The best
- **Part L**: Data-structure operations
- **Part M**: Reading real timings
- **The trick**: look at what happens to the time when n doubles.

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Answers & Explanations and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Big O Worksheet answers, p.1: Answers & Explanations
Every step count below was checked by running the code. Try each part yourself before
reading its answers.
Part A: Simplify the expression
Part B: Order the growth rates
B1. 1, log n, √n, n, n log n, n², n³, 2ⁿ, n!
Why: constan

> **Q: Summarize the core mechanism of See the jump: going from O(n log n) to O(n²) multiplies the work by about 100. and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Big O Worksheet answers, p.2: See the jump: going from O(n log n) to O(n²) multiplies the work by about 100.
Part C: Constant time
C1. O(1). Three lines, no loop. Reading arr[0] or arr[n-1] is one jump in memory,
however big n is.
C2. O(1). This is the trap. The loop runs 100 tim

> **Q: Summarize the core mechanism of E4. About 20 steps; O(log n). 1,000,000 halved 20 times is less than 1, because  and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Big O Worksheet answers, p.3: E4. About 20 steps; O(log n). 1,000,000 halved 20 times is less than 1, because 2²⁰ ≈
1,048,576. A linear search might need 1,000,000 steps; binary search needs about 20.
Part F: Quadratic and cubic time
F1. 100 times; O(n²). For each of the n values

> **Q: Summarize the core mechanism of Part J: Recursion and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Big O Worksheet answers, p.4: Part J: Recursion
J1. 5 calls; O(n). fact(5) → fact(4) → fact(3) → fact(2) → fact(1). Each call does one
multiplication, and there are n calls. n calls × O(1) work = O(n).
J2. 5 calls; O(log n). halve(16) → halve(8) → halve(4) → halve(2) → halve(1). 

---

## CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2 - CS250 - DSA - Course Outline_BSAI-2K25-A_Fall2026.pdf

### 📝 Executive Summary
This lecture on 'CS250 - DSA - Course Outline_BSAI-2K25-A_Fall2026.pdf' covers key fundamentals across 5 slides/sections. Major themes include Mapping of the Course Learning Outcomes (CLO) to the Programme Learning Outcomes, Details on Innovative T&L practices:, Lab Experiments (if applicable):, Assessment Methods:. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Gain hands**: on experience in programming using the latest Integrated Development
- **Conducted through in**: class or lab activities.
- **Introduction**: What is a Data Structure?
- **Stacks**: Concept, Implementation, Applications
- **Queues**: Concept, Implementation, Applications
- **Time Complexity II**: Loops and Nested Structures
- **Non-Linear Data Structures I**: Introduction to Trees
- **Tree Traversals**: Inorder, Preorder, Postorder
- **AVL Trees**: Rotations and Balancing
- **Applications of Trees**: Heaps and Priority Queues

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Mapping of the Course Learning Outcomes (CLO) to the Programme Learning Outcomes and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on CS250 - DSA - Course Outline_BSAI-2K25-A_Fall2026.pdf, p.1: Mapping of the Course Learning Outcomes (CLO) to the Programme Learning Outcomes (PLO), 
Teaching & Learning (T&L) methods and Assessment methods: 
Course 
Synopsis
This course focuses on equipping students with a solid understanding of data structur

> **Q: Summarize the core mechanism of Details on Innovative T&L practices: and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on CS250 - DSA - Course Outline_BSAI-2K25-A_Fall2026.pdf, p.2: Details on Innovative T&L practices: 
Weekly Schedule: 
CLO 
3
Practice programs using the 
latest IDEs ensuring testing, 
documentation and packaging 
of programs as per standards 
practices applicable to the 
software industry.
NA
5
P-3 
(Guided 
R

> **Q: Summarize the core mechanism of Lab Experiments (if applicable): and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on CS250 - DSA - Course Outline_BSAI-2K25-A_Fall2026.pdf, p.3: Lab Experiments (if applicable): 
Week 7
•
Binary Search Trees (BST) Basics 
•
Tree Traversals: Inorder, Preorder, Postorder
Week 8
•
AVL Trees: Introduction 
•
AVL Trees: Rotations and Balancing
Week 9
Mid-Semester Break
Week 10
•
Applications of Tr

> **Q: Summarize the core mechanism of Assessment Methods: and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on CS250 - DSA - Course Outline_BSAI-2K25-A_Fall2026.pdf, p.4: Assessment Methods: 
Learning resources: 
Grading Policy: 
Lab 12
Implement Counting Sort and Radix Sort; compare with earlier sorting algorithms
Lab 13
Implement Hash Table with chaining and open addressing
Lab 14
Implement Graph representations and

---

## CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2 - Week1_Foundations.pptx

### 📝 Executive Summary
This lecture on 'Week1_Foundations.pptx' covers key fundamentals across 56 slides/sections. Major themes include Slide 1, Slide 2, Slide 3, Slide 4. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Student A**: search the list as it came
- **That gap**: 1,000,000 against 20 — is the entire subject of this course.
- **A data structure**: way of organising data in memory so that it can be used efficiently.
- **Every row**: genuine trade. There is no column of all wins. Choosing a data structure means deciding which operations you will do most often.
- **The obvious algorithm**: and exactly how much it costs.
- **Best case**: 1 comparison  (it is first)
- **Worst case**: n comparisons  (last, or absent)
- **Average**: about n/2 comparisons
- **The pattern**: the work is directly proportional to n. Ten times the data, ten times the time. We will give this pattern a name in Week 5 — O(n) — but you can already see the shape of it.
- **Ask**: how many times can I halve n before only one element is left?

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Slide 1 and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Week1_Foundations.pptx, Slide 1: [0]
[1]
[2]
[3]
[4]
[5]
WEEK 1  ·  3 HOURS
Data Structures
and Algorithms
What a data structure really is, what an algorithm really is,
and why the two are the same subject.
CS-250  ·  BSAI-2K25-A  ·  Fall 2026  ·  Mr. Saud Kamran  ·  Room A-209
[Pre

> **Q: Summarize the core mechanism of Slide 2 and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Week1_Foundations.pptx, Slide 2: ROADMAP
Where we are going this week
Hour 1
Structures &
Algorithms
Why the same data, stored differently,
costs a million times more to search.
Hour 2
Types &
Abstract Data Types
The idea that separates a programmer
from an engineer: WHAT vs HOW.
Ho

> **Q: Summarize the core mechanism of Slide 3 and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Week1_Foundations.pptx, Slide 3: HOUR 1
Structures and
Algorithms
Start with a problem, not a definition.
A million names, one question
What a data structure is
What an algorithm is
Linear search vs binary search

> **Q: Summarize the core mechanism of Slide 4 and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Week1_Foundations.pptx, Slide 4: HOUR 1 · MOTIVATION
A very ordinary problem
You have a list of 1,000,000 student names.
Find out whether "Kamran" is in it.
Two students hand you two different solutions. Both are correct. One of them is a million times faster.
Student A — search the

---

## CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2 - Big O Worksheet

### 📝 Executive Summary
This lecture on 'Big O Worksheet' covers key fundamentals across 11 slides/sections. Major themes include CS-250 Big-O Worksheet: Every Kind of, Recipes for reading code, Part B: Order the growth rates, Big-O: __________. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **CS-250 Big**: O Worksheet: Every Kind of
- **What Big**: O means, in one sentence
- **Big**: O tells you how fast the work grows when the input gets bigger. It does not tell you
- **Tip**: when you are not sure, pick a small n (like 8 or 16) and count the steps by hand. Then
- **Part A**: Simplify the expression
- **Use the two rules**: drop constants, keep the biggest term. Write the Big-O.
- **Part B**: Order the growth rates
- **Answer**: ______________________________________________
- **Part C**: Constant time, O(1)
- **Part E**: Logarithmic time, O(log n)

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of CS-250 Big-O Worksheet: Every Kind of and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Big O Worksheet, p.1: CS-250 Big-O Worksheet: Every Kind of
Running Time
​Oct 4, 2026 · ​@Saud
Start here: the Big-O toolkit
This worksheet has 14 parts (A to N) and about 60 short questions. Work through them in
order: each part adds one new idea. Write your answer in th

> **Q: Summarize the core mechanism of Recipes for reading code and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Big O Worksheet, p.2: Recipes for reading code
Tip: when you are not sure, pick a small n (like 8 or 16) and count the steps by hand. Then
try double that n and see how the count changes.
Part A: Simplify the expression
Use the two rules: drop constants, keep the biggest 

> **Q: Summarize the core mechanism of Part B: Order the growth rates and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Big O Worksheet, p.3: Part B: Order the growth rates
B1. Put these in order from slowest-growing (best) to fastest-growing (worst):
n², log n, 1, n!, n log n, 2ⁿ, n, √n, n³
Answer: ______________________________________________
B2. Fill in the number of steps when n = 1,0

> **Q: Summarize the core mechanism of Big-O: __________ and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Big O Worksheet, p.4: Big-O: __________
C2. (Careful!)
int sum = 0;
for (int i = 0; i < 100; i++)
    sum += i;
Big-O: __________
Part D: Linear time, O(n)
D1.
int sum = 0;
for (int i = 0; i < n; i++)
    sum += arr[i];
Big-O: __________
D2. How many times does the loop b

---

## CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2 - Lecture Links

### 📝 Executive Summary
This lecture on 'Lecture Links' covers key fundamentals across 1 slides/sections. Major themes include Google Interview Prep. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Google Interview Prep**: Google Interview Prep  https://igotanoffer.com/blogs/tech/coding-interview-prep  https://www.youtube.com/c/neetcode  https://neetcode.io/roadmap...

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Google Interview Prep and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture Links, p.1: Google Interview Prep 
https://igotanoffer.com/blogs/tech/coding-interview-prep 
https://www.youtube.com/c/neetcode 
https://neetcode.io/roadmap

---

## CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2 - 04-collections-2.pdf

### 📝 Executive Summary
This lecture on '04-collections-2.pdf' covers key fundamentals across 229 slides/sections. Major themes include Collections, Part Two, Outline for Today, Stack, Car 1. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **An Application**: Balanced Parentheses
- **Time**: Out for Announcements!
- **Important**: Please note the Stanford Computer Forum policies regarding no-
- **Collections, Part Two**: Collections, Part Two...
- **Outline for Today**: Outline for Today ●Stacks ●Pancakes meets parsing! ●Queues ●Playing some music!...
- **Stack**: Stack...
- **Car 1**: Car 1 Car 2 Car 3 This car  can’t leave… … until these  two do. Thanks to Nick Troccoli for this example!...
- **Car 1**: Car 1 Car 2 Car 3 Thanks to Nick Troccoli for this example! Car 4 Car 5 Any new car  precedes all the old  cars. Only this car  can leave....
- **Car 1**: Car 1 Thanks to Nick Troccoli for this example! Car 4 Car 5...
- **Stack**: Stack ●A Stack is a data structure  representing a stack of things. ●Objects can be pushed on top  of the stack or popped from  the top of the stack....

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Collections, Part Two and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on 04-collections-2.pdf, p.1: Collections, Part Two

> **Q: Summarize the core mechanism of Outline for Today and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on 04-collections-2.pdf, p.2: Outline for Today
●Stacks
●Pancakes meets parsing!
●Queues
●Playing some music!

> **Q: Summarize the core mechanism of Stack and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on 04-collections-2.pdf, p.3: Stack

> **Q: Summarize the core mechanism of Car 1 and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on 04-collections-2.pdf, p.4: Car 1
Car 2
Car 3
This car 
can’t leave…
… until these 
two do.
Thanks to Nick Troccoli for this example!

---

## CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2 - Week 2 Lecture - Pointers

### 📝 Executive Summary
This lecture on 'Week 2 Lecture - Pointers' covers key fundamentals across 51 slides/sections. Major themes include Slide 1, Slide 2, Slide 3, Slide 4. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **The way out**: ask for memory while the program is running. To do that we first need to be able to talk about memory at all.
- **The star**: two different things
- **It says**: p is a pointer to int.
- **Hour 1**: what you should now be able to say
- **The stack**: automatic, and unforgiving
- **Disaster 2**: the dangling pointer
- **Match the form**: new/delete, new[]/delete[].
- **Hour 2**: what you should now be able to say
- **Deep**: what you must write
- **It cannot be copied**: only moved. That makes double free impossible by construction.

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Slide 1 and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Week 2 Lecture - Pointers, Slide 1: [0]
[1]
[2]
[3]
[4]
[5]
WEEK 2  ·  3 HOURS
Pointers and
Dynamic Memory
Where your variables actually live, how to ask for memory yourself,
and how to give it back without breaking anything.
CS-250  ·  BSAI-2K25-A  ·  Fall 2026  ·  Mr. Saud Kamran  · 

> **Q: Summarize the core mechanism of Slide 2 and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Week 2 Lecture - Pointers, Slide 2: READ THIS FIRST
The hardest week of the semester
Everything from Week 3 onwards — linked lists, trees, heaps, graphs — is built out of what we cover today.
Memory and
Pointers
What an address is, what a pointer stores,
and how to read and follow one.

> **Q: Summarize the core mechanism of Slide 3 and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Week 2 Lecture - Pointers, Slide 3: HOUR 1
Memory and
Pointers
Before we can build a linked list, we need to know what a link is.
The problem arrays cannot solve
Memory, addresses and &
Declaring and following a pointer
Pointer arithmetic and arrays

> **Q: Summarize the core mechanism of Slide 4 and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Week 2 Lecture - Pointers, Slide 4: HOUR 1 · MOTIVATION
A problem you cannot solve yet
"Ask the user how many marks to enter, then read exactly that many."
THE OBVIOUS ATTEMPT — AND WHY IT FAILS
int n;
cin >> n;          // user types 500

int marks[n];      // ✗ not valid standard C++

---

## CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2 - Pointers Worksheet

### 📝 Executive Summary
This lecture on 'Pointers Worksheet' covers key fundamentals across 1 slides/sections. Major themes include // Sean's CS106B Pointers Worksheet! Show the contents of variables a, b, p, and. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **// Sean's CS106B Pointers Worksheet! Show the contents of variables a, b, p, and**: // Sean's CS106B Pointers Worksheet! Show the contents of variables a, b, p, and q // at the various stages of the program's execution where I've drawn the boxes. #include <iostrea...

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of // Sean's CS106B Pointers Worksheet! Show the contents of variables a, b, p, and and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Pointers Worksheet, p.1: // Sean's CS106B Pointers Worksheet! Show the contents of variables a, b, p, and q
// at the various stages of the program's execution where I've drawn the boxes.
#include <iostream>
#include "console.h"
using namespace std;
int main()
{
   int a = 4

---

## CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2 - CS106B Pointers and Arrays.pdf

### 📝 Executive Summary
This lecture on 'CS106B Pointers and Arrays.pdf' covers key fundamentals across 16 slides/sections. Major themes include Pointers and Arrays, Today's lecture quiz (super important!)., Recall that arrays are one of the fundamental building blocks of the C++ languag, DATA_TYPE_POINTED_TO  * VARIABLE_NAME ;. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Reminder**: Pointers are a topic where doing lots of exercises is more important than ever in order to get comfortable
- **An array**: variable that is able to hold multiple values of some type. An array is made up of cells. Each cell holds a
- **Style Note**: Pointer Declarations
- **The Ampersand Operator**: Different Things in Different Contexts!
- **The Asterisk Operator**: Different Things in Different Contexts!

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Pointers and Arrays and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on CS106B Pointers and Arrays.pdf, p.1: Pointers and Arrays
TUESDAY, JULY 21
Today we'll learn about pointers and arrays in C++ as we build up the toolkit we will need to implement awesome
ADTs like vectors and stacks.
📚 Readings: Text 11.1, 11.2, 11.3
📝 Lecture quiz on Canvas
Contents
1. 

> **Q: Summarize the core mechanism of Today's lecture quiz (super important!). and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on CS106B Pointers and Arrays.pdf, p.2: Today's lecture quiz (super important!).
Next week's section problems! We have a really great pointer tracing exercise planned.
Arrays
We started class today with a brief overview of arrays. We saw the syntax for creating an array and accessing its
e

> **Q: Summarize the core mechanism of Recall that arrays are one of the fundamental building blocks of the C++ languag and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on CS106B Pointers and Arrays.pdf, p.3: Recall that arrays are one of the fundamental building blocks of the C++ language, and they're often used to create
vectors! A vector will often have an array hidden away as a private member variable. If we add more elements than its
array can hold, 

> **Q: Summarize the core mechanism of DATA_TYPE_POINTED_TO  * VARIABLE_NAME ; and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on CS106B Pointers and Arrays.pdf, p.4: DATA_TYPE_POINTED_TO  * VARIABLE_NAME ;
For example, to create a variable named p that can hold the address of an integer, the syntax is as follows:
int *p;
Here's that idea in action:
main.cpp
#include <iostream>
#include "console.h"
using namespace

---

## CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2 - Finalized Course Outline

### 📝 Executive Summary
This lecture on 'Finalized Course Outline' covers key fundamentals across 6 slides/sections. Major themes include COURSE OUTLINE- CS250 Data Structures and Algorithms, Mapping of the Course Learning Outcomes (CLO) to the Programme Learning, 3., Week 14. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **COURSE OUTLINE**: CS250 Data Structures and Algorithms
- **Gain hands**: on experience in programming using the latest Integrated
- **Conducted through in**: class or lab activities.
- **Introduction**: What is a Data Structure?
- **Stacks**: Concept, Implementation, Applications
- **Queues**: Concept, Implementation, Applications
- **Time Complexity II**: Loops and Nested Structures
- **Non-Linear Data Structures I**: Introduction to Trees
- **Tree Traversals**: Inorder, Preorder, Postorder
- **AVL Trees**: Rotations and Balancing

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of COURSE OUTLINE- CS250 Data Structures and Algorithms and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Finalized Course Outline, p.1: COURSE OUTLINE- CS250 Data Structures and Algorithms 
 
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

> **Q: Summarize the core mechanism of Mapping of the Course Learning Outcomes (CLO) to the Programme Learning and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Finalized Course Outline, p.2: Mapping of the Course Learning Outcomes (CLO) to the Programme Learning 
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

> **Q: Summarize the core mechanism of 3. and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Finalized Course Outline, p.3: 3. 
Blended learning 
Conducted through the NUST Learning Management System (LMS), all 
information and materials related to teaching and learning activities will be 
shared with the class via this platform. Additionally, some formative 
assessments 

> **Q: Summarize the core mechanism of Week 14 and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Finalized Course Outline, p.4: Week 14 
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

---

## CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2 - Dynamic Allocation

### 📝 Executive Summary
This lecture on 'Dynamic Allocation' covers key fundamentals across 61 slides/sections. Major themes include Dynamic Allocation: The Basics, string* ptr;, string* ptr;, string* ptr;. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Dynamic Allocation: The Basics**: Dynamic Allocation: The Basics...
- **string* ptr;**: string* ptr;         ptr The variable ptr has type string* rather than string. We’ll explain this in a moment....
- **int* ptr = new int[4];**: int* ptr = new int[4]; ptr Arrays of ints, doubles, chars, or bools initially have garbage values. Other types use good defaults....
- **string* ptr = new string[3];**: string* ptr = new string[3]; ptr...
- **Coffee Shop**: Coffee Shop Office Space Residential            ! ptr string* ptr = new string[3]; ptr[0] = "Coffee Shop"; ptr[1] = "Office Space"; ptr[2] = "Residential";...
- **void makeAnArray() {**: void makeAnArray() {     string* ptr = new string[3]; }   int main() {     for (int i = 0; i < 5; i++) {         makeAnArray();     } }...
- **void makeAnArray() {**: void makeAnArray() {     string* ptr = new string[3]; }   int main() {     for (int i = 0; i < 5; i++) {         makeAnArray();     } }...
- **void makeAnArray() {**: void makeAnArray() {     string* ptr = new string[3]; }   int main() {     for (int i = 0; i < 5; i++) {         makeAnArray();     } }...
- **void makeAnArray() {**: void makeAnArray() {     string* ptr = new string[3]; }   int main() {     for (int i = 0; i < 5; i++) {         makeAnArray();     } }...
- **void makeAnArray() {**: void makeAnArray() {     string* ptr = new string[3]; }   int main() {     for (int i = 0; i < 5; i++) {         makeAnArray();     } }            ! ptr...

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Dynamic Allocation: The Basics and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Dynamic Allocation, p.1: Dynamic Allocation: The Basics

> **Q: Summarize the core mechanism of string* ptr; and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Dynamic Allocation, p.2: string* ptr;
 
 
 
 
ptr
The variable ptr has type
string*
rather than string. We’ll
explain this in a moment.

> **Q: Summarize the core mechanism of string* ptr; and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Dynamic Allocation, p.3: string* ptr;
ptr = new string[3];
 
 
 
ptr

> **Q: Summarize the core mechanism of string* ptr; and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Dynamic Allocation, p.4: string* ptr;
ptr = new string[3];
 
 
 
ptr
This is an array of three
strings. I’ll represent it
as a three-story building.

---

## CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2 - Pointers Worksheet Solution

### 📝 Executive Summary
This lecture on 'Pointers Worksheet Solution' covers key fundamentals across 1 slides/sections. Major themes include // Sean's CS106B Pointers Worksheet! Show the contents of variables a, b, p, and. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **// Sean's CS106B Pointers Worksheet! Show the contents of variables a, b, p, and**: // Sean's CS106B Pointers Worksheet! Show the contents of variables a, b, p, and q // at the various stages of the program's execution where I've drawn the boxes. #include <iostrea...

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of // Sean's CS106B Pointers Worksheet! Show the contents of variables a, b, p, and and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Pointers Worksheet Solution, p.1: // Sean's CS106B Pointers Worksheet! Show the contents of variables a, b, p, and q
// at the various stages of the program's execution where I've drawn the boxes.
#include <iostream>
#include "console.h"
using namespace std;
int main()
{
   int a = 4

---

## CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2 - Josephus Problem

### 📝 Executive Summary
No extractable text found for Josephus Problem.

### 🔑 Key Definitions

### 💡 Core Conceptual Questions
---

## CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2 - Time Complexity in Recursion

### 📝 Executive Summary
This lecture on 'Time Complexity in Recursion' covers key fundamentals across 18 slides/sections. Major themes include CS-250 · Data Structures & Algorithms, The one idea, The method, Step 1. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **A recursive function**: loop in disguise. Count how many calls happen, and
- **The tree**: single line. Each node does constant work c, and
- **Equal levels**: log n of them, cn each.
- **Doubling levels**: 1 + 2 + 4 + … + n = 2n − 1.
- **Root vs leaves**: who does more work?

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of CS-250 · Data Structures & Algorithms and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Time Complexity in Recursion, p.1: CS-250 · Data Structures & Algorithms
Time Complexity 
in Recursion
How to count the cost of a function that calls itself

> **Q: Summarize the core mechanism of The one idea and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Time Complexity in Recursion, p.2: The one idea
Running time = the work done in 
every call, added up.
A recursive function is a loop in disguise. Count how many calls happen, and 
how much work each call does on its own.

> **Q: Summarize the core mechanism of The method and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Time Complexity in Recursion, p.3: The method
Three steps, every time
1
Write the 
recurrence
T(n) = the cost of the calls it 
makes + the work it does itself.
2
Draw the recursion 
tree
One node per call. Write each 
node's own work inside it.
3
Add it up
Sum the work level by level.

> **Q: Summarize the core mechanism of Step 1 and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Time Complexity in Recursion, p.4: Step 1
How to read a recurrence
T(n) = a · T(n/b) + f(n)
a
How many recursive calls each 
call makes
n/b or n − 1
How big each smaller problem is
f(n)
Work done outside the calls: loops, 
comparing, merging
Plus a base case, T(1) = c, that stops the 

---

## CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2 - Big O Worksheet answers

### 📝 Executive Summary
This lecture on 'Big O Worksheet answers' covers key fundamentals across 7 slides/sections. Major themes include Answers & Explanations, See the jump: going from O(n log n) to O(n²) multiplies the work by about 100., E4. About 20 steps; O(log n). 1,000,000 halved 20 times is less than 1, because , Part J: Recursion. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Part A**: Simplify the expression
- **Part B**: Order the growth rates
- **Why**: constants never grow. Logs grow very slowly (doubling n adds just 1). √n is slower
- **See the jump**: going from O(n log n) to O(n²) multiplies the work by about 100.
- **Part F**: Quadratic and cubic time
- **Part K**: Best case and worst case
- **Key idea**: best and worst cases are about which input you get, for the same n. The best
- **Part L**: Data-structure operations
- **Part M**: Reading real timings
- **The trick**: look at what happens to the time when n doubles.

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Answers & Explanations and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Big O Worksheet answers, p.1: Answers & Explanations
Every step count below was checked by running the code. Try each part yourself before
reading its answers.
Part A: Simplify the expression
Part B: Order the growth rates
B1. 1, log n, √n, n, n log n, n², n³, 2ⁿ, n!
Why: constan

> **Q: Summarize the core mechanism of See the jump: going from O(n log n) to O(n²) multiplies the work by about 100. and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Big O Worksheet answers, p.2: See the jump: going from O(n log n) to O(n²) multiplies the work by about 100.
Part C: Constant time
C1. O(1). Three lines, no loop. Reading arr[0] or arr[n-1] is one jump in memory,
however big n is.
C2. O(1). This is the trap. The loop runs 100 tim

> **Q: Summarize the core mechanism of E4. About 20 steps; O(log n). 1,000,000 halved 20 times is less than 1, because  and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Big O Worksheet answers, p.3: E4. About 20 steps; O(log n). 1,000,000 halved 20 times is less than 1, because 2²⁰ ≈
1,048,576. A linear search might need 1,000,000 steps; binary search needs about 20.
Part F: Quadratic and cubic time
F1. 100 times; O(n²). For each of the n values

> **Q: Summarize the core mechanism of Part J: Recursion and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Big O Worksheet answers, p.4: Part J: Recursion
J1. 5 calls; O(n). fact(5) → fact(4) → fact(3) → fact(2) → fact(1). Each call does one
multiplication, and there are n calls. n calls × O(1) work = O(n).
J2. 5 calls; O(log n). halve(16) → halve(8) → halve(4) → halve(2) → halve(1). 

---

## CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2 - CS250 - DSA - Course Outline_BSAI-2K25-A_Fall2026.pdf

### 📝 Executive Summary
This lecture on 'CS250 - DSA - Course Outline_BSAI-2K25-A_Fall2026.pdf' covers key fundamentals across 5 slides/sections. Major themes include Mapping of the Course Learning Outcomes (CLO) to the Programme Learning Outcomes, Details on Innovative T&L practices:, Lab Experiments (if applicable):, Assessment Methods:. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Gain hands**: on experience in programming using the latest Integrated Development
- **Conducted through in**: class or lab activities.
- **Introduction**: What is a Data Structure?
- **Stacks**: Concept, Implementation, Applications
- **Queues**: Concept, Implementation, Applications
- **Time Complexity II**: Loops and Nested Structures
- **Non-Linear Data Structures I**: Introduction to Trees
- **Tree Traversals**: Inorder, Preorder, Postorder
- **AVL Trees**: Rotations and Balancing
- **Applications of Trees**: Heaps and Priority Queues

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Mapping of the Course Learning Outcomes (CLO) to the Programme Learning Outcomes and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on CS250 - DSA - Course Outline_BSAI-2K25-A_Fall2026.pdf, p.1: Mapping of the Course Learning Outcomes (CLO) to the Programme Learning Outcomes (PLO), 
Teaching & Learning (T&L) methods and Assessment methods: 
Course 
Synopsis
This course focuses on equipping students with a solid understanding of data structur

> **Q: Summarize the core mechanism of Details on Innovative T&L practices: and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on CS250 - DSA - Course Outline_BSAI-2K25-A_Fall2026.pdf, p.2: Details on Innovative T&L practices: 
Weekly Schedule: 
CLO 
3
Practice programs using the 
latest IDEs ensuring testing, 
documentation and packaging 
of programs as per standards 
practices applicable to the 
software industry.
NA
5
P-3 
(Guided 
R

> **Q: Summarize the core mechanism of Lab Experiments (if applicable): and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on CS250 - DSA - Course Outline_BSAI-2K25-A_Fall2026.pdf, p.3: Lab Experiments (if applicable): 
Week 7
•
Binary Search Trees (BST) Basics 
•
Tree Traversals: Inorder, Preorder, Postorder
Week 8
•
AVL Trees: Introduction 
•
AVL Trees: Rotations and Balancing
Week 9
Mid-Semester Break
Week 10
•
Applications of Tr

> **Q: Summarize the core mechanism of Assessment Methods: and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on CS250 - DSA - Course Outline_BSAI-2K25-A_Fall2026.pdf, p.4: Assessment Methods: 
Learning resources: 
Grading Policy: 
Lab 12
Implement Counting Sort and Radix Sort; compare with earlier sorting algorithms
Lab 13
Implement Hash Table with chaining and open addressing
Lab 14
Implement Graph representations and

---

## CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2 - Week1_Foundations.pptx

### 📝 Executive Summary
This lecture on 'Week1_Foundations.pptx' covers key fundamentals across 56 slides/sections. Major themes include Slide 1, Slide 2, Slide 3, Slide 4. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Student A**: search the list as it came
- **That gap**: 1,000,000 against 20 — is the entire subject of this course.
- **A data structure**: way of organising data in memory so that it can be used efficiently.
- **Every row**: genuine trade. There is no column of all wins. Choosing a data structure means deciding which operations you will do most often.
- **The obvious algorithm**: and exactly how much it costs.
- **Best case**: 1 comparison  (it is first)
- **Worst case**: n comparisons  (last, or absent)
- **Average**: about n/2 comparisons
- **The pattern**: the work is directly proportional to n. Ten times the data, ten times the time. We will give this pattern a name in Week 5 — O(n) — but you can already see the shape of it.
- **Ask**: how many times can I halve n before only one element is left?

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Slide 1 and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Week1_Foundations.pptx, Slide 1: [0]
[1]
[2]
[3]
[4]
[5]
WEEK 1  ·  3 HOURS
Data Structures
and Algorithms
What a data structure really is, what an algorithm really is,
and why the two are the same subject.
CS-250  ·  BSAI-2K25-A  ·  Fall 2026  ·  Mr. Saud Kamran  ·  Room A-209
[Pre

> **Q: Summarize the core mechanism of Slide 2 and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Week1_Foundations.pptx, Slide 2: ROADMAP
Where we are going this week
Hour 1
Structures &
Algorithms
Why the same data, stored differently,
costs a million times more to search.
Hour 2
Types &
Abstract Data Types
The idea that separates a programmer
from an engineer: WHAT vs HOW.
Ho

> **Q: Summarize the core mechanism of Slide 3 and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Week1_Foundations.pptx, Slide 3: HOUR 1
Structures and
Algorithms
Start with a problem, not a definition.
A million names, one question
What a data structure is
What an algorithm is
Linear search vs binary search

> **Q: Summarize the core mechanism of Slide 4 and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Week1_Foundations.pptx, Slide 4: HOUR 1 · MOTIVATION
A very ordinary problem
You have a list of 1,000,000 student names.
Find out whether "Kamran" is in it.
Two students hand you two different solutions. Both are correct. One of them is a million times faster.
Student A — search the

---

## CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2 - Big O Worksheet

### 📝 Executive Summary
This lecture on 'Big O Worksheet' covers key fundamentals across 11 slides/sections. Major themes include CS-250 Big-O Worksheet: Every Kind of, Recipes for reading code, Part B: Order the growth rates, Big-O: __________. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **CS-250 Big**: O Worksheet: Every Kind of
- **What Big**: O means, in one sentence
- **Big**: O tells you how fast the work grows when the input gets bigger. It does not tell you
- **Tip**: when you are not sure, pick a small n (like 8 or 16) and count the steps by hand. Then
- **Part A**: Simplify the expression
- **Use the two rules**: drop constants, keep the biggest term. Write the Big-O.
- **Part B**: Order the growth rates
- **Answer**: ______________________________________________
- **Part C**: Constant time, O(1)
- **Part E**: Logarithmic time, O(log n)

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of CS-250 Big-O Worksheet: Every Kind of and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Big O Worksheet, p.1: CS-250 Big-O Worksheet: Every Kind of
Running Time
​Oct 4, 2026 · ​@Saud
Start here: the Big-O toolkit
This worksheet has 14 parts (A to N) and about 60 short questions. Work through them in
order: each part adds one new idea. Write your answer in th

> **Q: Summarize the core mechanism of Recipes for reading code and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Big O Worksheet, p.2: Recipes for reading code
Tip: when you are not sure, pick a small n (like 8 or 16) and count the steps by hand. Then
try double that n and see how the count changes.
Part A: Simplify the expression
Use the two rules: drop constants, keep the biggest 

> **Q: Summarize the core mechanism of Part B: Order the growth rates and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Big O Worksheet, p.3: Part B: Order the growth rates
B1. Put these in order from slowest-growing (best) to fastest-growing (worst):
n², log n, 1, n!, n log n, 2ⁿ, n, √n, n³
Answer: ______________________________________________
B2. Fill in the number of steps when n = 1,0

> **Q: Summarize the core mechanism of Big-O: __________ and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Big O Worksheet, p.4: Big-O: __________
C2. (Careful!)
int sum = 0;
for (int i = 0; i < 100; i++)
    sum += i;
Big-O: __________
Part D: Linear time, O(n)
D1.
int sum = 0;
for (int i = 0; i < n; i++)
    sum += arr[i];
Big-O: __________
D2. How many times does the loop b

---

## CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2 - Lecture Links

### 📝 Executive Summary
This lecture on 'Lecture Links' covers key fundamentals across 1 slides/sections. Major themes include Google Interview Prep. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Google Interview Prep**: Google Interview Prep  https://igotanoffer.com/blogs/tech/coding-interview-prep  https://www.youtube.com/c/neetcode  https://neetcode.io/roadmap...

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Google Interview Prep and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture Links, p.1: Google Interview Prep 
https://igotanoffer.com/blogs/tech/coding-interview-prep 
https://www.youtube.com/c/neetcode 
https://neetcode.io/roadmap

---

## CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2 - 04-collections-2.pdf

### 📝 Executive Summary
This lecture on '04-collections-2.pdf' covers key fundamentals across 229 slides/sections. Major themes include Collections, Part Two, Outline for Today, Stack, Car 1. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **An Application**: Balanced Parentheses
- **Time**: Out for Announcements!
- **Important**: Please note the Stanford Computer Forum policies regarding no-
- **Collections, Part Two**: Collections, Part Two...
- **Outline for Today**: Outline for Today ●Stacks ●Pancakes meets parsing! ●Queues ●Playing some music!...
- **Stack**: Stack...
- **Car 1**: Car 1 Car 2 Car 3 This car  can’t leave… … until these  two do. Thanks to Nick Troccoli for this example!...
- **Car 1**: Car 1 Car 2 Car 3 Thanks to Nick Troccoli for this example! Car 4 Car 5 Any new car  precedes all the old  cars. Only this car  can leave....
- **Car 1**: Car 1 Thanks to Nick Troccoli for this example! Car 4 Car 5...
- **Stack**: Stack ●A Stack is a data structure  representing a stack of things. ●Objects can be pushed on top  of the stack or popped from  the top of the stack....

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Collections, Part Two and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on 04-collections-2.pdf, p.1: Collections, Part Two

> **Q: Summarize the core mechanism of Outline for Today and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on 04-collections-2.pdf, p.2: Outline for Today
●Stacks
●Pancakes meets parsing!
●Queues
●Playing some music!

> **Q: Summarize the core mechanism of Stack and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on 04-collections-2.pdf, p.3: Stack

> **Q: Summarize the core mechanism of Car 1 and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on 04-collections-2.pdf, p.4: Car 1
Car 2
Car 3
This car 
can’t leave…
… until these 
two do.
Thanks to Nick Troccoli for this example!

---

## CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2 - Week 2 Lecture - Pointers

### 📝 Executive Summary
This lecture on 'Week 2 Lecture - Pointers' covers key fundamentals across 51 slides/sections. Major themes include Slide 1, Slide 2, Slide 3, Slide 4. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **The way out**: ask for memory while the program is running. To do that we first need to be able to talk about memory at all.
- **The star**: two different things
- **It says**: p is a pointer to int.
- **Hour 1**: what you should now be able to say
- **The stack**: automatic, and unforgiving
- **Disaster 2**: the dangling pointer
- **Match the form**: new/delete, new[]/delete[].
- **Hour 2**: what you should now be able to say
- **Deep**: what you must write
- **It cannot be copied**: only moved. That makes double free impossible by construction.

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Slide 1 and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Week 2 Lecture - Pointers, Slide 1: [0]
[1]
[2]
[3]
[4]
[5]
WEEK 2  ·  3 HOURS
Pointers and
Dynamic Memory
Where your variables actually live, how to ask for memory yourself,
and how to give it back without breaking anything.
CS-250  ·  BSAI-2K25-A  ·  Fall 2026  ·  Mr. Saud Kamran  · 

> **Q: Summarize the core mechanism of Slide 2 and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Week 2 Lecture - Pointers, Slide 2: READ THIS FIRST
The hardest week of the semester
Everything from Week 3 onwards — linked lists, trees, heaps, graphs — is built out of what we cover today.
Memory and
Pointers
What an address is, what a pointer stores,
and how to read and follow one.

> **Q: Summarize the core mechanism of Slide 3 and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Week 2 Lecture - Pointers, Slide 3: HOUR 1
Memory and
Pointers
Before we can build a linked list, we need to know what a link is.
The problem arrays cannot solve
Memory, addresses and &
Declaring and following a pointer
Pointer arithmetic and arrays

> **Q: Summarize the core mechanism of Slide 4 and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Week 2 Lecture - Pointers, Slide 4: HOUR 1 · MOTIVATION
A problem you cannot solve yet
"Ask the user how many marks to enter, then read exactly that many."
THE OBVIOUS ATTEMPT — AND WHY IT FAILS
int n;
cin >> n;          // user types 500

int marks[n];      // ✗ not valid standard C++

---

## CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2 - Pointers Worksheet

### 📝 Executive Summary
This lecture on 'Pointers Worksheet' covers key fundamentals across 1 slides/sections. Major themes include // Sean's CS106B Pointers Worksheet! Show the contents of variables a, b, p, and. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **// Sean's CS106B Pointers Worksheet! Show the contents of variables a, b, p, and**: // Sean's CS106B Pointers Worksheet! Show the contents of variables a, b, p, and q // at the various stages of the program's execution where I've drawn the boxes. #include <iostrea...

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of // Sean's CS106B Pointers Worksheet! Show the contents of variables a, b, p, and and how it applies to CS-250-Data_Structures__amp__Algorithms_A_2K25-BSAI-2.**
>
> *A:* Based on Pointers Worksheet, p.1: // Sean's CS106B Pointers Worksheet! Show the contents of variables a, b, p, and q
// at the various stages of the program's execution where I've drawn the boxes.
#include <iostream>
#include "console.h"
using namespace std;
int main()
{
   int a = 4

---

