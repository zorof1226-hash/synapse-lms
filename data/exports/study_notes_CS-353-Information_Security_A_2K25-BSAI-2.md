# 📚 Study Knowledge Base: CS-353-Information_Security_A_2K25-BSAI-2

*Auto-generated from LMS lecture notes. Compatible with Obsidian & Notion.*

---

## CS-353-Information_Security_A_2K25-BSAI-2 - CS353-W5-DES

### 📝 Executive Summary
This lecture on 'CS353-W5-DES' covers key fundamentals across 98 slides/sections. Major themes include CHAPTER 4 Block Ciphers and Data Encryption Standard (DES), LEARNING OBJECTIVES, LEARNING OBJECTIVES, Modern Block Ciphers. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Source**: William Stallings, Cryptography and Network Security: Principles and Practice, 7th Edition, published by Pearson Education, Inc., publishing as Prentice Hall, 2017.
- **A block cipher**: type of symmetric encryption which operates on blocks of data. Modern block ciphers typically use a block length of 64,128, 256 bits
- **Confusion**: making the relationship between the key and the ciphertext as complex and involved as possible
- **Diffusion**: the property that redundancy in the statistics of the plaintext is "dissipated" in the statistics of the ciphertext
- **S-P network**: a special form of substitution-transposition product cipher
- **Substitution**: Permutation (S-P) networks form the basis of modern block ciphers.
- **Data encrypted in 64**: bit blocks using a 56-bit key (effective key); Ciphertext is of 64-bit long
- **Data**: need to be broken into 64-bit blocks; add pad bits at the last message if necessary.
- **DES operates on 64**: bit blocks of plaintext. After an initial permutation the block is broken into right half and left half, each being 32 bits long
- **Takes 32**: bit R half and 48-bit sub-key and:

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of CHAPTER 4 Block Ciphers and Data Encryption Standard (DES) and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on CS353-W5-DES, Slide 1: CHAPTER 4 Block Ciphers and Data Encryption Standard (DES)
1
Source: William Stallings, Cryptography and Network Security: Principles and Practice, 7th Edition, published by Pearson Education, Inc., publishing as Prentice Hall, 2017.

> **Q: Summarize the core mechanism of LEARNING OBJECTIVES and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on CS353-W5-DES, Slide 2: LEARNING OBJECTIVES
2
Upon completion of this material, you should be able to:
Understand the distinction between stream ciphers and block ciphers.
Present an overview of the Feistel cipher and explain how decryption is the inverse of encryption.

> **Q: Summarize the core mechanism of LEARNING OBJECTIVES and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on CS353-W5-DES, Slide 3: LEARNING OBJECTIVES
3
Upon completion of this material, you should be able to:
Present an overview of Data Encryption Standard (DES).
Encryption, Decryption process

> **Q: Summarize the core mechanism of Modern Block Ciphers and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on CS353-W5-DES, Slide 4: Modern Block Ciphers
Most widely used types of cryptographic algorithms

Focus on block ciphers design principles

DES and AES
4
Source: William Stallings, Cryptography and Network Security: Principles and Practice, 7th Edition, published by Pearson 

---

## CS-353-Information_Security_A_2K25-BSAI-2 - Week 1-Lecture InfoSec

### 📝 Executive Summary
This lecture on 'Week 1-Lecture InfoSec' covers key fundamentals across 58 slides/sections. Major themes include CS-353 Information Security (2+1), Ice Breaking Session, Course Information, IS Course Topics. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Analyze real**: world scenarios from an information security perspective and model them using different security measures.
- **Ref**: elearningindustry.com/modern-student-learning-life-infographic
- **This**: classic example of an unintentional breach of availability.
- **The email**: scam. The hacker is not directly trying to steal data (yet); their immediate goal is to deceive the student into believing the email is authentic.
- **Examples**: password, ACL, firewall
- **MPLS  Multi**: Protocol Label Switching
- **Source**: Whitman, M. E., & Mattord, H. J. (2018). Principles of information security (7th ed.). Cengage Learning.
- **Active Attacks**: These involve the attacker trying to modify, disrupt, or destroy information or services. The goal is to change the state of the system.
- **Example**: A Denial of Service (DoS) attack that floods a server with traffic to make a website unavailable is an active attack. A hacker changing a student's grade in a database is also an active attack.
- **Passive Attacks**: These involve the attacker trying to monitor or eavesdrop on a system or network without changing anything. The goal is to gain information without being detected.

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of CS-353 Information Security (2+1) and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on Week 1-Lecture InfoSec, Slide 1: CS-353 Information Security (2+1)
Lecture 1
Hirra Anwar

> **Q: Summarize the core mechanism of Ice Breaking Session and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on Week 1-Lecture InfoSec, Slide 2: Ice Breaking Session
Instructor Introduction
Students Introduction
Basic Intro (e.g. name, background, interests, future aspirations etc.)
What is the most important thing you learned at university? 
One word you would use to describe yourself.
What 

> **Q: Summarize the core mechanism of Course Information and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on Week 1-Lecture InfoSec, Slide 3: Course Information
Course Code: CS-353
Pre-Req: N/A
Text book: 
Principles of Information Security, Michael E. Whitman and Herbert J.Mattord Publisher: Cengage Learning; ISBN: 1285448367, 6th edition.
Reference books: 
1. William Stallings and Lawrie

> **Q: Summarize the core mechanism of IS Course Topics and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on Week 1-Lecture InfoSec, Slide 4: IS Course Topics
4

---

## CS-353-Information_Security_A_2K25-BSAI-2 - Week 2-Classical Cryptography- part I

### 📝 Executive Summary
This lecture on 'Week 2-Classical Cryptography- part I' covers key fundamentals across 27 slides/sections. Major themes include Week 2, LEARNING OBJECTIVES, LEARNING OBJECTIVES, Terms. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Source**: Whitman, M. E., & Mattord, H. J. (2018). Principles of information security (7th ed.). Cengage Learning.
- **Example**: In a “three-character substitution to the right”
- **Shift cipher**: each letter is replaced by shifting alphabets few positions to the right. i.e. shift of 1,2,3,5..
- **PT**: larger key size means greater security
- **CT**: WKJHV JUVZO DGVQV KNOHJ VKIVJ OVPXJ DIZ
- **Initial alphabet**: ABCDEFGHIJKLMNOPQRSTUVWXYZ
- **Table 8**: 2 can be used in different ways, e.g.:

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Week 2 and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on Week 2-Classical Cryptography- part I, p.1: Week 2 
Classical Cryptography 
Part I 
1 
Hirra Anwar

> **Q: Summarize the core mechanism of LEARNING OBJECTIVES and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on Week 2-Classical Cryptography- part I, p.2: LEARNING OBJECTIVES 
- part I 
2 
 
Upon completion of this material, you 
should be able to: 
●Explain the basic 
principles of 
cryptography 
●Learn about the 
classical ciphers

> **Q: Summarize the core mechanism of LEARNING OBJECTIVES and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on Week 2-Classical Cryptography- part I, p.3: LEARNING OBJECTIVES 
- part II 
3 
 
Upon completion of this material, you 
should be able to: 
●Describe the 
operating principles 
of the most popular 
cryptographic tools 
●List and explain the 
major protocols used 
for secure 
communications

> **Q: Summarize the core mechanism of Terms and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on Week 2-Classical Cryptography- part I, p.4: Terms 
●
plaintext - original message  
●
ciphertext - coded message  
●
cipher - algorithm for transforming plaintext to ciphertext  
●
key - info used in cipher known only to sender/receiver  
●
encipher (encrypt) - converting plaintext to cipherte

---

## CS-353-Information_Security_A_2K25-BSAI-2 - CS-353-Information Security_Course_ouline_Hirra Anwar_approved.docx

### 📝 Executive Summary
No extractable text found for CS-353-Information Security_Course_ouline_Hirra Anwar_approved.docx.

### 🔑 Key Definitions

### 💡 Core Conceptual Questions
---

## CS-353-Information_Security_A_2K25-BSAI-2 - Lab 4 - IS.docx

### 📝 Executive Summary
No extractable text found for Lab 4 - IS.docx.

### 🔑 Key Definitions

### 💡 Core Conceptual Questions
---

## CS-353-Information_Security_A_2K25-BSAI-2 - DES example

### 📝 Executive Summary
This lecture on 'DES example' covers key fundamentals across 13 slides/sections. Major themes include [Email Reply], the content of data stored on various media, providing encryption of, some extra bytes at the tail end for the encryption. Once the encrypted message , Example: Let K be the hexadecimal key K = 133457799BBCDFF1. This gives us as the. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **the total message**: multiple of 8 bytes (or 16 hexadecimal digits, or 64 bits).
- **Example**: Let M be the plain text message M = 0123456789ABCDEF, where M is in
- **Step 1**: Create 16 subkeys, each of which is 48-bits long.
- **The 64**: bit key is permuted according to the following table, PC-1. Since the first entry
- **Step 2**: Encode each 64-bit block of data.
- **where each Bi**: group of six bits. We now calculate
- **Triple**: DES is just DES with two 56-bit keys applied. Given a plaintext message, the first
- **Homepage**: http://orlingrabbe.com/
- **Laissez Faire City Times**: http://zolatimes.com/

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of [Email Reply] and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on DES example, p.1: [Email Reply]
The DES Algorithm Illustrated
by J. Orlin Grabbe
The DES (Data Encryption Standard) algorithm is the most widely used encryption
algorithm in the world. For many years, and among many people, "secret code making"
and DES have been synon

> **Q: Summarize the core mechanism of the content of data stored on various media, providing encryption of and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on DES example, p.2: the content of data stored on various media, providing encryption of
adequate strength can be devised and validated and is inherently integrable
into system architecture. The National Bureau of Standards solicits proposed
techniques and algorithms fo

> **Q: Summarize the core mechanism of some extra bytes at the tail end for the encryption. Once the encrypted message  and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on DES example, p.3: some extra bytes at the tail end for the encryption. Once the encrypted message has been
decrypted, these extra bytes are thrown away. There are, of course, different padding
schemes--different ways to add extra bytes. Here we will just add 0s at the

> **Q: Summarize the core mechanism of Example: Let K be the hexadecimal key K = 133457799BBCDFF1. This gives us as the and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on DES example, p.4: Example: Let K be the hexadecimal key K = 133457799BBCDFF1. This gives us as the
binary key (setting 1 = 0001, 3 = 0011, etc., and grouping together every eight bits, of
which the last one in each group will be unused):
K = 00010011 00110100 01010111

---

## CS-353-Information_Security_A_2K25-BSAI-2 - Lab 2 - IS.docx

### 📝 Executive Summary
No extractable text found for Lab 2 - IS.docx.

### 🔑 Key Definitions

### 💡 Core Conceptual Questions
---

## CS-353-Information_Security_A_2K25-BSAI-2 - Lab 3 - IS

### 📝 Executive Summary
No extractable text found for Lab 3 - IS.

### 🔑 Key Definitions

### 💡 Core Conceptual Questions
---

## CS-353-Information_Security_A_2K25-BSAI-2 - CS353-W4-Modern Ciphers - Symmetric Cryptography-I

### 📝 Executive Summary
This lecture on 'CS353-W4-Modern Ciphers - Symmetric Cryptography-I' covers key fundamentals across 40 slides/sections. Major themes include CHAPTER 4 Block Ciphers and Data Encryption Standard (DES)

CHAPTER 6 Advanced E, LEARNING OBJECTIVES, LEARNING OBJECTIVES, Modern Block Ciphers. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Source**: William Stallings, Cryptography and Network Security: Principles and Practice, 7th Edition, published by Pearson Education, Inc., publishing as Prentice Hall, 2017.
- **A block cipher**: type of symmetric encryption which operates on blocks of data. Modern block ciphers typically use a block length of 128 bits or more
- **Confusion**: making the relationship between the key and the ciphertext as complex and involved as possible
- **Diffusion**: the property that redundancy in the statistics of the plaintext is "dissipated" in the statistics of the ciphertext
- **S-P network**: a special form of substitution-transposition product cipher
- **Substitution**: Permutation (S-P) networks form the basis of modern block ciphers.
- **Data encrypted in 64**: bit blocks using a 56-bit key (effective key); Ciphertext is of 64-bit long
- **Data**: need to be broken into 64-bit blocks; add pad bits at the last message if necessary.
- **DES operates on 64**: bit blocks of plaintext. After an initial permutation the block is broken into right half and left half, each being 32 bits long
- **Takes 32**: bit R half and 48-bit sub-key and:

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of CHAPTER 4 Block Ciphers and Data Encryption Standard (DES)

CHAPTER 6 Advanced E and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on CS353-W4-Modern Ciphers - Symmetric Cryptography-I, Slide 1: CHAPTER 4 Block Ciphers and Data Encryption Standard (DES)

CHAPTER 6 Advanced Encryption Standard (AES)
1
Source: William Stallings, Cryptography and Network Security: Principles and Practice, 7th Edition, published by Pearson Education, Inc., publi

> **Q: Summarize the core mechanism of LEARNING OBJECTIVES and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on CS353-W4-Modern Ciphers - Symmetric Cryptography-I, Slide 2: LEARNING OBJECTIVES
2
Upon completion of this material, you should be able to:
Understand the distinction between stream ciphers and block ciphers.
Present an overview of the Feistel cipher and explain how decryption is the inverse of encryption.

> **Q: Summarize the core mechanism of LEARNING OBJECTIVES and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on CS353-W4-Modern Ciphers - Symmetric Cryptography-I, Slide 3: LEARNING OBJECTIVES
3
Upon completion of this material, you should be able to:
Present an overview of Data Encryption Standard (DES).

> **Q: Summarize the core mechanism of Modern Block Ciphers and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on CS353-W4-Modern Ciphers - Symmetric Cryptography-I, Slide 4: Modern Block Ciphers
Most widely used types of cryptographic algorithms

Focus on block ciphers design principles

DES and AES
4
Source: William Stallings, Cryptography and Network Security: Principles and Practice, 7th Edition, published by Pearson 

---

## CS-353-Information_Security_A_2K25-BSAI-2 - Week 2-Classical Cryptography-part II.pdf

### 📝 Executive Summary
This lecture on 'Week 2-Classical Cryptography-part II.pdf' covers key fundamentals across 73 slides/sections. Major themes include Week 2, LEARNING OBJECTIVES, Terms, Introduction. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Source**: Whitman, M. E., & Mattord, H. J. (2018). Principles of information security (7th ed.). Cengage Learning.
- **Example**: In a “three-character substitution to the right”
- **Shift cipher**: each letter is replaced by shifting alphabets few positions to the right. i.e. shift of 1,2,3,5..
- **PT**: larger key size means greater security
- **CT**: WKJHV JUVZO DGVQV KNOHJ VKIVJ OVPXJ DIZ
- **Initial alphabet**: ABCDEFGHIJKLMNOPQRSTUVWXYZ
- **Table 8**: 2 can be used in different ways, e.g.:
- **English language**: Relative Letter Frequencies
- **The Affine cipher**: monoalphabetic substitution cipher. It is similar
- **We normally use**: A=0, B=1, C=2,…,Z=25

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Week 2 and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on Week 2-Classical Cryptography-part II.pdf, p.1: Week 2 
Classical Cryptography 
Part II 
1 
Hirra Anwar

> **Q: Summarize the core mechanism of LEARNING OBJECTIVES and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on Week 2-Classical Cryptography-part II.pdf, p.2: LEARNING OBJECTIVES 
- part I 
2 
 
Upon completion of this material, you 
should be able to: 
●Explain the basic 
principles of 
cryptography 
●Learn about the 
classical ciphers

> **Q: Summarize the core mechanism of Terms and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on Week 2-Classical Cryptography-part II.pdf, p.3: Terms 
●
plaintext - original message  
●
ciphertext - coded message  
●
cipher - algorithm for transforming plaintext to ciphertext  
●
key - info used in cipher known only to sender/receiver  
●
encipher (encrypt) - converting plaintext to cipherte

> **Q: Summarize the core mechanism of Introduction and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on Week 2-Classical Cryptography-part II.pdf, p.4: Introduction 
cryptography → the process of making and using codes 
to secure information. 
4

---

## CS-353-Information_Security_A_2K25-BSAI-2 - IS Lab Policy  Guidelines.pdf

### 📝 Executive Summary
This lecture on 'IS Lab Policy  Guidelines.pdf' covers key fundamentals across 1 slides/sections. Major themes include INFORMATION SECURITY LAB GUIDELINES & POLICY. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Use of AI**: Direct copy-pasting from AI tools is strictly prohibited and will result in zero marks. AI tools may only be
- **Plagiarism Policy**: Plagiarism is strictly not allowed. If any two lab reports are found to be similar, zero marks will be
- **INFORMATION SECURITY LAB GUIDELINES & POLICY**: INFORMATION SECURITY LAB GUIDELINES & POLICY 1. Lab Timings & Attendance : The lab starts at 9:00 AM, so all students must arrive on time. Attendance may be taken at any time betwe...

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of INFORMATION SECURITY LAB GUIDELINES & POLICY and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on IS Lab Policy  Guidelines.pdf, p.1: INFORMATION SECURITY LAB GUIDELINES & POLICY
1.
Lab Timings & Attendance : The lab starts at 9:00 AM, so all students must arrive on time. Attendance may be
taken at any time between 9:15 AM to 9:30 AM or right after explaining the lab tasks.
2.
Atte

---

## CS-353-Information_Security_A_2K25-BSAI-2 - Lab 5 - IS.docx

### 📝 Executive Summary
No extractable text found for Lab 5 - IS.docx.

### 🔑 Key Definitions

### 💡 Core Conceptual Questions
---

## CS-353-Information_Security_A_2K25-BSAI-2 - Lab 1 - IS

### 📝 Executive Summary
No extractable text found for Lab 1 - IS.

### 🔑 Key Definitions

### 💡 Core Conceptual Questions
---

## CS-353-Information_Security_A_2K25-BSAI-2 - CS353-W5-DES

### 📝 Executive Summary
This lecture on 'CS353-W5-DES' covers key fundamentals across 98 slides/sections. Major themes include CHAPTER 4 Block Ciphers and Data Encryption Standard (DES), LEARNING OBJECTIVES, LEARNING OBJECTIVES, Modern Block Ciphers. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Source**: William Stallings, Cryptography and Network Security: Principles and Practice, 7th Edition, published by Pearson Education, Inc., publishing as Prentice Hall, 2017.
- **A block cipher**: type of symmetric encryption which operates on blocks of data. Modern block ciphers typically use a block length of 64,128, 256 bits
- **Confusion**: making the relationship between the key and the ciphertext as complex and involved as possible
- **Diffusion**: the property that redundancy in the statistics of the plaintext is "dissipated" in the statistics of the ciphertext
- **S-P network**: a special form of substitution-transposition product cipher
- **Substitution**: Permutation (S-P) networks form the basis of modern block ciphers.
- **Data encrypted in 64**: bit blocks using a 56-bit key (effective key); Ciphertext is of 64-bit long
- **Data**: need to be broken into 64-bit blocks; add pad bits at the last message if necessary.
- **DES operates on 64**: bit blocks of plaintext. After an initial permutation the block is broken into right half and left half, each being 32 bits long
- **Takes 32**: bit R half and 48-bit sub-key and:

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of CHAPTER 4 Block Ciphers and Data Encryption Standard (DES) and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on CS353-W5-DES, Slide 1: CHAPTER 4 Block Ciphers and Data Encryption Standard (DES)
1
Source: William Stallings, Cryptography and Network Security: Principles and Practice, 7th Edition, published by Pearson Education, Inc., publishing as Prentice Hall, 2017.

> **Q: Summarize the core mechanism of LEARNING OBJECTIVES and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on CS353-W5-DES, Slide 2: LEARNING OBJECTIVES
2
Upon completion of this material, you should be able to:
Understand the distinction between stream ciphers and block ciphers.
Present an overview of the Feistel cipher and explain how decryption is the inverse of encryption.

> **Q: Summarize the core mechanism of LEARNING OBJECTIVES and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on CS353-W5-DES, Slide 3: LEARNING OBJECTIVES
3
Upon completion of this material, you should be able to:
Present an overview of Data Encryption Standard (DES).
Encryption, Decryption process

> **Q: Summarize the core mechanism of Modern Block Ciphers and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on CS353-W5-DES, Slide 4: Modern Block Ciphers
Most widely used types of cryptographic algorithms

Focus on block ciphers design principles

DES and AES
4
Source: William Stallings, Cryptography and Network Security: Principles and Practice, 7th Edition, published by Pearson 

---

## CS-353-Information_Security_A_2K25-BSAI-2 - Week 1-Lecture InfoSec

### 📝 Executive Summary
This lecture on 'Week 1-Lecture InfoSec' covers key fundamentals across 58 slides/sections. Major themes include CS-353 Information Security (2+1), Ice Breaking Session, Course Information, IS Course Topics. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Analyze real**: world scenarios from an information security perspective and model them using different security measures.
- **Ref**: elearningindustry.com/modern-student-learning-life-infographic
- **This**: classic example of an unintentional breach of availability.
- **The email**: scam. The hacker is not directly trying to steal data (yet); their immediate goal is to deceive the student into believing the email is authentic.
- **Examples**: password, ACL, firewall
- **MPLS  Multi**: Protocol Label Switching
- **Source**: Whitman, M. E., & Mattord, H. J. (2018). Principles of information security (7th ed.). Cengage Learning.
- **Active Attacks**: These involve the attacker trying to modify, disrupt, or destroy information or services. The goal is to change the state of the system.
- **Example**: A Denial of Service (DoS) attack that floods a server with traffic to make a website unavailable is an active attack. A hacker changing a student's grade in a database is also an active attack.
- **Passive Attacks**: These involve the attacker trying to monitor or eavesdrop on a system or network without changing anything. The goal is to gain information without being detected.

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of CS-353 Information Security (2+1) and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on Week 1-Lecture InfoSec, Slide 1: CS-353 Information Security (2+1)
Lecture 1
Hirra Anwar

> **Q: Summarize the core mechanism of Ice Breaking Session and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on Week 1-Lecture InfoSec, Slide 2: Ice Breaking Session
Instructor Introduction
Students Introduction
Basic Intro (e.g. name, background, interests, future aspirations etc.)
What is the most important thing you learned at university? 
One word you would use to describe yourself.
What 

> **Q: Summarize the core mechanism of Course Information and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on Week 1-Lecture InfoSec, Slide 3: Course Information
Course Code: CS-353
Pre-Req: N/A
Text book: 
Principles of Information Security, Michael E. Whitman and Herbert J.Mattord Publisher: Cengage Learning; ISBN: 1285448367, 6th edition.
Reference books: 
1. William Stallings and Lawrie

> **Q: Summarize the core mechanism of IS Course Topics and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on Week 1-Lecture InfoSec, Slide 4: IS Course Topics
4

---

## CS-353-Information_Security_A_2K25-BSAI-2 - Week 2-Classical Cryptography- part I

### 📝 Executive Summary
This lecture on 'Week 2-Classical Cryptography- part I' covers key fundamentals across 27 slides/sections. Major themes include Week 2, LEARNING OBJECTIVES, LEARNING OBJECTIVES, Terms. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Source**: Whitman, M. E., & Mattord, H. J. (2018). Principles of information security (7th ed.). Cengage Learning.
- **Example**: In a “three-character substitution to the right”
- **Shift cipher**: each letter is replaced by shifting alphabets few positions to the right. i.e. shift of 1,2,3,5..
- **PT**: larger key size means greater security
- **CT**: WKJHV JUVZO DGVQV KNOHJ VKIVJ OVPXJ DIZ
- **Initial alphabet**: ABCDEFGHIJKLMNOPQRSTUVWXYZ
- **Table 8**: 2 can be used in different ways, e.g.:

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Week 2 and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on Week 2-Classical Cryptography- part I, p.1: Week 2 
Classical Cryptography 
Part I 
1 
Hirra Anwar

> **Q: Summarize the core mechanism of LEARNING OBJECTIVES and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on Week 2-Classical Cryptography- part I, p.2: LEARNING OBJECTIVES 
- part I 
2 
 
Upon completion of this material, you 
should be able to: 
●Explain the basic 
principles of 
cryptography 
●Learn about the 
classical ciphers

> **Q: Summarize the core mechanism of LEARNING OBJECTIVES and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on Week 2-Classical Cryptography- part I, p.3: LEARNING OBJECTIVES 
- part II 
3 
 
Upon completion of this material, you 
should be able to: 
●Describe the 
operating principles 
of the most popular 
cryptographic tools 
●List and explain the 
major protocols used 
for secure 
communications

> **Q: Summarize the core mechanism of Terms and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on Week 2-Classical Cryptography- part I, p.4: Terms 
●
plaintext - original message  
●
ciphertext - coded message  
●
cipher - algorithm for transforming plaintext to ciphertext  
●
key - info used in cipher known only to sender/receiver  
●
encipher (encrypt) - converting plaintext to cipherte

---

## CS-353-Information_Security_A_2K25-BSAI-2 - CS-353-Information Security_Course_ouline_Hirra Anwar_approved.docx

### 📝 Executive Summary
No extractable text found for CS-353-Information Security_Course_ouline_Hirra Anwar_approved.docx.

### 🔑 Key Definitions

### 💡 Core Conceptual Questions
---

## CS-353-Information_Security_A_2K25-BSAI-2 - Lab 4 - IS.docx

### 📝 Executive Summary
No extractable text found for Lab 4 - IS.docx.

### 🔑 Key Definitions

### 💡 Core Conceptual Questions
---

## CS-353-Information_Security_A_2K25-BSAI-2 - DES example

### 📝 Executive Summary
This lecture on 'DES example' covers key fundamentals across 13 slides/sections. Major themes include [Email Reply], the content of data stored on various media, providing encryption of, some extra bytes at the tail end for the encryption. Once the encrypted message , Example: Let K be the hexadecimal key K = 133457799BBCDFF1. This gives us as the. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **the total message**: multiple of 8 bytes (or 16 hexadecimal digits, or 64 bits).
- **Example**: Let M be the plain text message M = 0123456789ABCDEF, where M is in
- **Step 1**: Create 16 subkeys, each of which is 48-bits long.
- **The 64**: bit key is permuted according to the following table, PC-1. Since the first entry
- **Step 2**: Encode each 64-bit block of data.
- **where each Bi**: group of six bits. We now calculate
- **Triple**: DES is just DES with two 56-bit keys applied. Given a plaintext message, the first
- **Homepage**: http://orlingrabbe.com/
- **Laissez Faire City Times**: http://zolatimes.com/

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of [Email Reply] and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on DES example, p.1: [Email Reply]
The DES Algorithm Illustrated
by J. Orlin Grabbe
The DES (Data Encryption Standard) algorithm is the most widely used encryption
algorithm in the world. For many years, and among many people, "secret code making"
and DES have been synon

> **Q: Summarize the core mechanism of the content of data stored on various media, providing encryption of and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on DES example, p.2: the content of data stored on various media, providing encryption of
adequate strength can be devised and validated and is inherently integrable
into system architecture. The National Bureau of Standards solicits proposed
techniques and algorithms fo

> **Q: Summarize the core mechanism of some extra bytes at the tail end for the encryption. Once the encrypted message  and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on DES example, p.3: some extra bytes at the tail end for the encryption. Once the encrypted message has been
decrypted, these extra bytes are thrown away. There are, of course, different padding
schemes--different ways to add extra bytes. Here we will just add 0s at the

> **Q: Summarize the core mechanism of Example: Let K be the hexadecimal key K = 133457799BBCDFF1. This gives us as the and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on DES example, p.4: Example: Let K be the hexadecimal key K = 133457799BBCDFF1. This gives us as the
binary key (setting 1 = 0001, 3 = 0011, etc., and grouping together every eight bits, of
which the last one in each group will be unused):
K = 00010011 00110100 01010111

---

## CS-353-Information_Security_A_2K25-BSAI-2 - Lab 2 - IS.docx

### 📝 Executive Summary
No extractable text found for Lab 2 - IS.docx.

### 🔑 Key Definitions

### 💡 Core Conceptual Questions
---

## CS-353-Information_Security_A_2K25-BSAI-2 - Lab 3 - IS

### 📝 Executive Summary
No extractable text found for Lab 3 - IS.

### 🔑 Key Definitions

### 💡 Core Conceptual Questions
---

## CS-353-Information_Security_A_2K25-BSAI-2 - CS353-W4-Modern Ciphers - Symmetric Cryptography-I

### 📝 Executive Summary
This lecture on 'CS353-W4-Modern Ciphers - Symmetric Cryptography-I' covers key fundamentals across 40 slides/sections. Major themes include CHAPTER 4 Block Ciphers and Data Encryption Standard (DES)

CHAPTER 6 Advanced E, LEARNING OBJECTIVES, LEARNING OBJECTIVES, Modern Block Ciphers. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Source**: William Stallings, Cryptography and Network Security: Principles and Practice, 7th Edition, published by Pearson Education, Inc., publishing as Prentice Hall, 2017.
- **A block cipher**: type of symmetric encryption which operates on blocks of data. Modern block ciphers typically use a block length of 128 bits or more
- **Confusion**: making the relationship between the key and the ciphertext as complex and involved as possible
- **Diffusion**: the property that redundancy in the statistics of the plaintext is "dissipated" in the statistics of the ciphertext
- **S-P network**: a special form of substitution-transposition product cipher
- **Substitution**: Permutation (S-P) networks form the basis of modern block ciphers.
- **Data encrypted in 64**: bit blocks using a 56-bit key (effective key); Ciphertext is of 64-bit long
- **Data**: need to be broken into 64-bit blocks; add pad bits at the last message if necessary.
- **DES operates on 64**: bit blocks of plaintext. After an initial permutation the block is broken into right half and left half, each being 32 bits long
- **Takes 32**: bit R half and 48-bit sub-key and:

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of CHAPTER 4 Block Ciphers and Data Encryption Standard (DES)

CHAPTER 6 Advanced E and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on CS353-W4-Modern Ciphers - Symmetric Cryptography-I, Slide 1: CHAPTER 4 Block Ciphers and Data Encryption Standard (DES)

CHAPTER 6 Advanced Encryption Standard (AES)
1
Source: William Stallings, Cryptography and Network Security: Principles and Practice, 7th Edition, published by Pearson Education, Inc., publi

> **Q: Summarize the core mechanism of LEARNING OBJECTIVES and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on CS353-W4-Modern Ciphers - Symmetric Cryptography-I, Slide 2: LEARNING OBJECTIVES
2
Upon completion of this material, you should be able to:
Understand the distinction between stream ciphers and block ciphers.
Present an overview of the Feistel cipher and explain how decryption is the inverse of encryption.

> **Q: Summarize the core mechanism of LEARNING OBJECTIVES and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on CS353-W4-Modern Ciphers - Symmetric Cryptography-I, Slide 3: LEARNING OBJECTIVES
3
Upon completion of this material, you should be able to:
Present an overview of Data Encryption Standard (DES).

> **Q: Summarize the core mechanism of Modern Block Ciphers and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on CS353-W4-Modern Ciphers - Symmetric Cryptography-I, Slide 4: Modern Block Ciphers
Most widely used types of cryptographic algorithms

Focus on block ciphers design principles

DES and AES
4
Source: William Stallings, Cryptography and Network Security: Principles and Practice, 7th Edition, published by Pearson 

---

## CS-353-Information_Security_A_2K25-BSAI-2 - Week 2-Classical Cryptography-part II.pdf

### 📝 Executive Summary
This lecture on 'Week 2-Classical Cryptography-part II.pdf' covers key fundamentals across 73 slides/sections. Major themes include Week 2, LEARNING OBJECTIVES, Terms, Introduction. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Source**: Whitman, M. E., & Mattord, H. J. (2018). Principles of information security (7th ed.). Cengage Learning.
- **Example**: In a “three-character substitution to the right”
- **Shift cipher**: each letter is replaced by shifting alphabets few positions to the right. i.e. shift of 1,2,3,5..
- **PT**: larger key size means greater security
- **CT**: WKJHV JUVZO DGVQV KNOHJ VKIVJ OVPXJ DIZ
- **Initial alphabet**: ABCDEFGHIJKLMNOPQRSTUVWXYZ
- **Table 8**: 2 can be used in different ways, e.g.:
- **English language**: Relative Letter Frequencies
- **The Affine cipher**: monoalphabetic substitution cipher. It is similar
- **We normally use**: A=0, B=1, C=2,…,Z=25

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Week 2 and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on Week 2-Classical Cryptography-part II.pdf, p.1: Week 2 
Classical Cryptography 
Part II 
1 
Hirra Anwar

> **Q: Summarize the core mechanism of LEARNING OBJECTIVES and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on Week 2-Classical Cryptography-part II.pdf, p.2: LEARNING OBJECTIVES 
- part I 
2 
 
Upon completion of this material, you 
should be able to: 
●Explain the basic 
principles of 
cryptography 
●Learn about the 
classical ciphers

> **Q: Summarize the core mechanism of Terms and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on Week 2-Classical Cryptography-part II.pdf, p.3: Terms 
●
plaintext - original message  
●
ciphertext - coded message  
●
cipher - algorithm for transforming plaintext to ciphertext  
●
key - info used in cipher known only to sender/receiver  
●
encipher (encrypt) - converting plaintext to cipherte

> **Q: Summarize the core mechanism of Introduction and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on Week 2-Classical Cryptography-part II.pdf, p.4: Introduction 
cryptography → the process of making and using codes 
to secure information. 
4

---

## CS-353-Information_Security_A_2K25-BSAI-2 - IS Lab Policy  Guidelines.pdf

### 📝 Executive Summary
This lecture on 'IS Lab Policy  Guidelines.pdf' covers key fundamentals across 1 slides/sections. Major themes include INFORMATION SECURITY LAB GUIDELINES & POLICY. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Use of AI**: Direct copy-pasting from AI tools is strictly prohibited and will result in zero marks. AI tools may only be
- **Plagiarism Policy**: Plagiarism is strictly not allowed. If any two lab reports are found to be similar, zero marks will be
- **INFORMATION SECURITY LAB GUIDELINES & POLICY**: INFORMATION SECURITY LAB GUIDELINES & POLICY 1. Lab Timings & Attendance : The lab starts at 9:00 AM, so all students must arrive on time. Attendance may be taken at any time betwe...

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of INFORMATION SECURITY LAB GUIDELINES & POLICY and how it applies to CS-353-Information_Security_A_2K25-BSAI-2.**
>
> *A:* Based on IS Lab Policy  Guidelines.pdf, p.1: INFORMATION SECURITY LAB GUIDELINES & POLICY
1.
Lab Timings & Attendance : The lab starts at 9:00 AM, so all students must arrive on time. Attendance may be
taken at any time between 9:15 AM to 9:30 AM or right after explaining the lab tasks.
2.
Atte

---

## CS-353-Information_Security_A_2K25-BSAI-2 - Lab 5 - IS.docx

### 📝 Executive Summary
No extractable text found for Lab 5 - IS.docx.

### 🔑 Key Definitions

### 💡 Core Conceptual Questions
---

## CS-353-Information_Security_A_2K25-BSAI-2 - Lab 1 - IS

### 📝 Executive Summary
No extractable text found for Lab 1 - IS.

### 🔑 Key Definitions

### 💡 Core Conceptual Questions
---

