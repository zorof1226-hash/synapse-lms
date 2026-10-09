# 📚 Study Knowledge Base: All Courses

*Auto-generated from LMS lecture notes. Compatible with Obsidian & Notion.*

---

## MATH-361-Probability_and_Statistics_D_2K25-BSCS-15 - 2. Representation of Data- Frequency Distribution

### 📝 Executive Summary
The provided lecture series focuses on the essential initial step in descriptive statistics: the representation and organization of collected data, specifically through frequency distributions. It highlights that the primary goal after data collection is to simplify and organize data to gain a general overview of results. A frequency distribution is introduced as a fundamental method for achieving this, involving the listing of all possible values or categories a variable can take, along with their respective frequencies.

### 🔑 Key Definitions
- **Frequency**: The count, or number of observations, within a specific category or class.
- **Frequency Distribution**: A listing of all the values (e.g., categories) that a variable can take, together with their corresponding frequencies, or an organization of data in a table showing distribution into classes/groups with observation counts.
- **Categorical Distribution**: A type of frequency distribution where data are grouped according to some quality or attribute.
- **Class Boundaries**: Points calculated from class limits that define the precise cut-off for each class interval.
- **Class Marks**: The midpoint of a class interval.
- **Class Interval**: The range or width of values covered by each class.
- **Cumulative Frequency**: A running total of frequencies, indicating the number of observations less than or equal to a certain point.

### 💡 Core Conceptual Questions
> **Q: Explain the primary purpose of constructing a frequency distribution immediately after collecting data, and elaborate on the core definition of what a frequency distribution represents.**
>
> *A:* The primary purpose of constructing a frequency distribution immediately after collecting data is to organize and simplify the raw data. This simplification allows the researcher to gain a general overview of the results, which is a key goal of descriptive statistical techniques. A frequency distribution itself represents an organized set of data, typically presented in a table, that shows how the data are distributed into various classes or groups, along with the corresponding number of observations (frequencies) found within each class or category.

> **Q: Discuss the considerations and trade-offs involved when determining the number of classes to form for a frequency distribution.**
>
> *A:* When determining the number of classes for a frequency distribution, there is no fixed rule; rather, a trade-off must be made. One consideration is to avoid choosing too few classes, as this can lead to losing too much information about the actual data values contained within each class. Conversely, choosing too many classes can be problematic because it may defeat the fundamental purpose of grouping data, which is to simplify and make it easier to interpret. The ideal number of classes strikes a balance between these two extremes, providing a clear yet informative overview of the data's distribution.

---

## MATH-361-Probability_and_Statistics_D_2K25-BSCS-15 - Course outline MATH-361 Probability and Statistics.docx

### 📝 Executive Summary
No extractable text found for Course outline MATH-361 Probability and Statistics.docx.

### 🔑 Key Definitions

### 💡 Core Conceptual Questions
---

## MATH-361-Probability_and_Statistics_D_2K25-BSCS-15 - 8. Sample space and Events.pptx

### 📝 Executive Summary
This lecture introduces fundamental concepts in probability theory, beginning with the definition of a random experiment and its constituent outcomes, sample points, and the comprehensive sample space. It then elaborates on various types of events, distinguishing between simple and compound events, and defining impossible and sure events. Key relationships between events are explained, including union, intersection, complement, mutually exclusive, and equally likely events, supported by illustrative examples from coin tosses, dice rolls, and real-world scenarios.

### 🔑 Key Definitions
- **Sample Point**: A single outcome of a random experiment.
- **Sample Space**: The set of all possible outcomes of a random experiment.
- **Event**: An outcome of an experiment OR a subset of a sample space.
- **Simple Event**: An event that contains exactly one sample point and cannot be further decomposed.
- **Compound Event**: An event that contains more than one sample point, and is produced by the union of simple events.
- **Impossible Event**: An event that contains no sample points of the sample space.
- **Sure Event**: An event that contains all the sample points of the sample space.
- **Union of Two Events (A ∪ B)**: The event that either A or B or both occur when the experiment is performed.
- **Intersection of Two Events (A ∩ B)**: The event that both A and B occur when the experiment is performed.
- **Complement of an Event (AC)**: Consists of all outcomes of the experiment that do not result in event A.
- **Mutually Exclusive Events**: Two events A and B of a single experiment are said to be mutually exclusive or disjoint if and only if they cannot both occur at the same time, meaning they have no points in common (A ∩ B = 0).
- **Equally Likely Events**: Two events A and B are said to be equally likely when one event is as likely to occur as the other, meaning each event should occur in equal number in repeated trials.
- **Counting Rule for Multiplication**: If an experiment is performed in two stages, with m ways to accomplish the first stage and n ways to accomplish the second stage, then there are mn ways to accomplish the experiment. This rule extends to k stages as n1 n2 n3 … nk.
- **Permutation**: Any ordered subset from a set of n distinct objects.
- **Combination**: Any subset of r objects, selected without regard to their order, from a subset of n distinct objects.

### 💡 Core Conceptual Questions
> **Q: Consider an experiment where a student is selected from a classroom, and their hair color and gender are recorded. Let event B be 'student is female' and event C be 'student is male.' Describe the relationship between events B and C, and what B ∪ C represents.**
>
> *A:* Events B ('student is female') and C ('student is male') are mutually exclusive because a student cannot be both male and female simultaneously (B ∩ C = ∅). They are also exhaustive events, as every student must be either male or female. B ∪ C represents the event that a student is either male or female, which encompasses all students in the sample space (B ∪ C = S).

> **Q: Explain when it is appropriate to use permutations versus combinations in counting problems, providing an example for each where order is the distinguishing factor.**
>
> *A:* Permutations are used when the order of selection or arrangement of objects is important. For instance, arranging 3 distinct books on a shelf from a set of 5 involves permutations, because 'ABC' is a different arrangement from 'BAC'. Combinations are used when the order of selection does not matter, and we are only concerned with the unique group or subset formed. For example, choosing 3 members from a 5-person committee to form a subcommittee is a combination problem, as the order in which the members are chosen does not change the composition of the subcommittee itself.

> **Q: A test consists of 12 true-false questions. Using the counting rule for multiplication, determine how many different ways a student can mark the test paper with one answer to each question. Explain your reasoning.**
>
> *A:* For each true-false question, there are 2 possible outcomes: 'True' or 'False'. Since there are 12 such questions, and each question's answer is an independent stage of the experiment, we apply the counting rule for multiplication. The total number of ways to mark the test paper is the product of the number of outcomes for each question. Therefore, the total number of ways is 2 × 2 × ... (12 times) = 2^12 = 4096.

---

## MATH-361-Probability_and_Statistics_D_2K25-BSCS-15 - Book-Probability and Statistics for Engineers by Richard A. Johnson

### 📝 Executive Summary
This lecture material introduces Miller & Freund’s Probability and Statistics for Engineers, Ninth Edition, authored by Richard A. Johnson. The book is applications-focused, designed for engineering and physical science students, and integrates modern statistical software like R and MINITAB. It emphasizes understanding confidence intervals, the logic of hypothesis testing, and the interpretation of P-values, building on previous editions with new examples and data-based exercises.

Chapter 1, 'Introduction,' defines statistics broadly as the collection, processing, analysis, and interpretation of numerical data, highlighting its crucial role in engineering for understanding and controlling phenomena subject to variation. It traces the origins of statistics to games of chance and political science, noting a significant shift in modern statistics from descriptive methods to statistical inference—making generalizations from sample data. The chapter outlines four crucial steps for information collection and stresses the importance of statistical thinking in quality improvement, a philosophy championed by W. Edwards Deming. A case study on ceramic part manufacturing illustrates how an X-bar chart can visually inspect data to improve product quality, underscoring that effective statistical procedures require corresponding action, not just observation.

The text also covers the book's structure, including chapter components like introductory statements, statistical guidelines, and key term checklists. It provides an overview of advanced topics covered in later chapters, such as probability distributions, sampling, hypothesis testing, regression analysis, experimental design, and quality-improvement programs, indicating a calculus background is expected for some sections.

### 🔑 Key Definitions
- **Statistics**: Everything dealing with the collection, processing, analysis, and interpretation of numerical data.
- **Descriptive Statistics**: The presentation of data in tables and charts, and the summarization of data by means of numerical descriptions and graphs.
- **Statistical Inference**: Generalizations based on sample data, used for problems like estimating average emissions or testing manufacturer claims.
- **Quality Improvement**: A philosophy based on 'make it right the first time' and a continuous commitment to improving processes and products, instrumental in modern competitive markets.
- **X-bar chart**: A graphical procedure that consists of plotting sample averages versus time order to indicate when changes have occurred and actions need to be taken to correct a process.
- **W. Edwards Deming**: A figure instrumental in the rejuvenation of Japanese industry, stressing American industry's need for a continuing commitment to quality improvement, attributing 85% or more of quality problems to the system.

### 💡 Core Conceptual Questions
> **Q: Explain the importance of statistical inference and the caution one must exercise when making such inferences.**
>
> *A:* Statistical inference is crucial because it allows for generalizations based on sample data, addressing problems such as estimating engine emissions or testing manufacturer claims when it's impractical to examine an entire population. However, caution must always be exercised when making statistical inferences because they go beyond the information contained in the collected data. One must carefully decide the extent of generalization, assess its reasonableness, and consider whether more data is needed. This includes appraising the risks and consequences of making generalizations, such as the probabilities of making wrong decisions, incorrect predictions, or obtaining estimates that do not adequately reflect the true situation.

> **Q: Describe the four crucial steps suggested by statistical ideas for the information collection process.**
>
> *A:* According to statistical ideas, the information collection process involves four crucial steps: 
1. **Set clearly defined goals for the investigation:** This establishes the purpose and direction of the study.
2. **Make a plan of what data to collect and how to collect it:** This involves designing the experiment or survey to gather relevant information efficiently.
3. **Apply appropriate statistical methods to efficiently extract information from the data:** This step uses analytical tools to process and interpret the collected data.
4. **Interpret the information and draw conclusions:** This involves making sense of the statistical findings and formulating actionable insights.

> **Q: Discuss the role of engineers and scientists in quality improvement programs, referencing W. Edwards Deming's philosophy.**
>
> *A:* Engineers and scientists play a main role in quality improvement programs, especially given the international revolution in competitive world markets. W. Edwards Deming emphasized a continuing commitment to quality improvement, advocating for the philosophy of 'make it right the first time' and continuous process enhancement. He claimed that 85% or more of quality problems reside in the 'system,' not with individual operators. Therefore, engineers and scientists, with their technical knowledge combined with basic statistical skills in data collection and graphical display, are key participants in attaining the goal of quality improvement from design through production. They are essential in identifying system-level issues and implementing the necessary changes, which often require authority beyond that of day-to-day operators.

---

## MATH-361-Probability_and_Statistics_D_2K25-BSCS-15 - 1. Introduction (ProbStats).pptx

### 📝 Executive Summary
This lecture on '1. Introduction (ProbStats).pptx' covers key fundamentals across 35 slides/sections. Major themes include Probability and Statistics (MATH-361)Introduction, Slide 3, LMs Self-Enrollment Key, Course Description. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Statistics**: a discipline that includes procedures and techniques used to
- **Marketing**: Developing market surveys and strategies for marketing new products
- **Economics**: Formation of economic policies
- **Finance**: Helps in value at risk, stock market-derivative
- **Public Health**: Identifying sources of diseases and ways to treat them
- **Population**: The collection or set of all objects or measurements that are of interest to the experimenter
- **Sample**: The subset or representative part of the population
- **Parameter**: A numerical measurement or quantity describing some characteristic of a population
- **Statistic**: A numerical measurement or quantity describing some characteristics of a sample
- **Class standings**: freshman, sophomore, junior, senior

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Probability and Statistics (MATH-361)Introduction and how it applies to MATH-361-Probability_and_Statistics_D_2K25-BSCS-15.**
>
> *A:* Based on 1. Introduction (ProbStats).pptx, Slide 1: Probability and Statistics (MATH-361)Introduction
Dr. Hina Dutt                                                                                       hina.dutt@seecs.edu.pk
SEECS-NUST

> **Q: Summarize the core mechanism of Slide 3 and how it applies to MATH-361-Probability_and_Statistics_D_2K25-BSCS-15.**
>
> *A:* Based on 1. Introduction (ProbStats).pptx, Slide 3: Course Logistics

> **Q: Summarize the core mechanism of LMs Self-Enrollment Key and how it applies to MATH-361-Probability_and_Statistics_D_2K25-BSCS-15.**
>
> *A:* Based on 1. Introduction (ProbStats).pptx, Slide 5: LMs Self-Enrollment Key
Enrollment Code : 109746258

> **Q: Summarize the core mechanism of Course Description and how it applies to MATH-361-Probability_and_Statistics_D_2K25-BSCS-15.**
>
> *A:* Based on 1. Introduction (ProbStats).pptx, Slide 6: Course Description
This course covers probability theory and various descriptive statistical techniques for collecting, analyzing and interpreting data. 
The course also covers inferential statistics that includes sampling, estimation of parameters a

---

## MATH-361-Probability_and_Statistics_D_2K25-BSCS-15 - 4. Measure of Central tendency.pptx

### 📝 Executive Summary
This lecture on '4. Measure of Central tendency.pptx' covers key fundamentals across 37 slides/sections. Major themes include Measure of Central tendency, Measures of Central Tendency, Measures of Central Tendency, Slide 4. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **The**: scores and the number of students in three sections of a statistics class are given in the table.
- **Median**: a value which divides an ordered data into two equal parts, one part comprising of observations greater than and the other part smaller than it.
- **Reference Book**: Probability and Statistics for Engineers, 9th  edition by Richard A. Johnson
- **Measure of Central tendency**: Measure of Central tendency Dr. Hina Dutt                                                                                       hina.dutt@seecs.edu.pk SEECS-NUST...
- **Measures of Central Tendency**: Measures of Central Tendency The tendency of observations to cluster in the central part of the data is called Central Tendency.  The value of data that summarizes the central tend...
- **Measures of Central Tendency**: Measures of Central Tendency...
- **Slide 4**: Mean...
- **Mean; Example 1 (Ungrouped Data)**: Mean; Example 1 (Ungrouped Data)...
- **Mean as a Balancing Point**: Mean as a Balancing Point Mean...
- **Weighted Mean**: Weighted Mean...

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Measure of Central tendency and how it applies to MATH-361-Probability_and_Statistics_D_2K25-BSCS-15.**
>
> *A:* Based on 4. Measure of Central tendency.pptx, Slide 1: Measure of Central tendency
Dr. Hina Dutt                                                                                       hina.dutt@seecs.edu.pk
SEECS-NUST

> **Q: Summarize the core mechanism of Measures of Central Tendency and how it applies to MATH-361-Probability_and_Statistics_D_2K25-BSCS-15.**
>
> *A:* Based on 4. Measure of Central tendency.pptx, Slide 2: Measures of Central Tendency
The tendency of observations to cluster in the central part of the data is called Central Tendency. 
The value of data that summarizes the central tendency or locate in the middle of the data (in some sense) is called Mea

> **Q: Summarize the core mechanism of Measures of Central Tendency and how it applies to MATH-361-Probability_and_Statistics_D_2K25-BSCS-15.**
>
> *A:* Based on 4. Measure of Central tendency.pptx, Slide 3: Measures of Central Tendency

> **Q: Summarize the core mechanism of Slide 4 and how it applies to MATH-361-Probability_and_Statistics_D_2K25-BSCS-15.**
>
> *A:* Based on 4. Measure of Central tendency.pptx, Slide 4: Mean

---

## MATH-361-Probability_and_Statistics_D_2K25-BSCS-15 - 5. Measure of Non-Central tendency

### 📝 Executive Summary
This lecture on '5. Measure of Non-Central tendency' covers key fundamentals across 13 slides/sections. Major themes include Measure of Non-Central tendency, Quantiles, How to Calculate Quantiles (For Individual Observations), Quantiles; Example 1 (Individual Observations). Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Reference Book**: Probability and Statistics for Engineers, 9th  edition by Richard A. Johnson
- **Measure of Non-Central tendency**: Measure of Non-Central tendency Dr. Hina Dutt                                                                                       hina.dutt@seecs.edu.pk SEECS-NUST...
- **Quantiles**: Quantiles...
- **How to Calculate Quantiles (For Individual Observations)**: How to Calculate Quantiles (For Individual Observations)...
- **Quantiles; Example 1 (Individual Observations)**: Quantiles; Example 1 (Individual Observations) The wheat production (in kgs) of 20 acres is given as: 1120 1240 1320 1040 1080 1200 1440 1360 1680 1730 1785 1342 1960 1880 1755 172...
- **Quantiles; Example 2 (Ungrouped frequency Distribution)**: Quantiles; Example 2 (Ungrouped frequency Distribution) The following distribution relates to the number of assistants in 50 retail establishments....
- **Quantiles; Example 2 (Ungrouped frequency Distribution)**: Quantiles; Example 2 (Ungrouped frequency Distribution)...
- **How to Calculate Quantiles (Grouped Data)**: How to Calculate Quantiles (Grouped Data)...
- **Quantiles; Example 3 (Grouped Data)**: Quantiles; Example 3 (Grouped Data) Calculate upper quartile and 63th percentile for the distribution of examination marks given below:...
- **Quantiles; Example 3 (Grouped Data)**: Quantiles; Example 3 (Grouped Data)...

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Measure of Non-Central tendency and how it applies to MATH-361-Probability_and_Statistics_D_2K25-BSCS-15.**
>
> *A:* Based on 5. Measure of Non-Central tendency, Slide 1: Measure of Non-Central tendency
Dr. Hina Dutt                                                                                       hina.dutt@seecs.edu.pk
SEECS-NUST

> **Q: Summarize the core mechanism of Quantiles and how it applies to MATH-361-Probability_and_Statistics_D_2K25-BSCS-15.**
>
> *A:* Based on 5. Measure of Non-Central tendency, Slide 2: Quantiles

> **Q: Summarize the core mechanism of How to Calculate Quantiles (For Individual Observations) and how it applies to MATH-361-Probability_and_Statistics_D_2K25-BSCS-15.**
>
> *A:* Based on 5. Measure of Non-Central tendency, Slide 9: How to Calculate Quantiles (For Individual Observations)

> **Q: Summarize the core mechanism of Quantiles; Example 1 (Individual Observations) and how it applies to MATH-361-Probability_and_Statistics_D_2K25-BSCS-15.**
>
> *A:* Based on 5. Measure of Non-Central tendency, Slide 10: Quantiles; Example 1 (Individual Observations)
The wheat production (in kgs) of 20 acres is given as: 1120 1240 1320 1040 1080 1200 1440 1360 1680 1730 1785 1342 1960 1880 1755 1720 1600 1470 1750 1885. Find the lower quartile and the seventh decile.

---

## MATH-361-Probability_and_Statistics_D_2K25-BSCS-15 - 3. Graphical Representation of Data.pptx

### 📝 Executive Summary
This lecture on '3. Graphical Representation of Data.pptx' covers key fundamentals across 40 slides/sections. Major themes include Graphical Representation of Data, Presentation Of Data, Slide 3, Bar Chart. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **A bar graph**: graph that displays the frequency or numerical distribution of a categorical variable, showing values for each bar next to each other for easy comparison.
- **A frequency polygon**: line graph to display and compare the distribution of quantitative data.
- **An Ogive**: graph obtained by plotting the cumulative frequencies of a distribution against the upper and lower class boundaries depending upon whether the cumulative frequency is of less than or more than type a
- **A dot diagram**: graph that is constructed by placing a dot for each observation above its value on a number line.
- **Stem and leaf display**: technique for simultaneously sorting and displaying data sets in which each number (value) in the data is divided into two parts; a Stem and a Leaf.
- **Make a stem and**: leaf table for the following data.
- **Double**: stem Display; Example 7
- **Construct a double**: stem display for the following data
- **Five**: Stem Display; Exercise 7

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Graphical Representation of Data and how it applies to MATH-361-Probability_and_Statistics_D_2K25-BSCS-15.**
>
> *A:* Based on 3. Graphical Representation of Data.pptx, Slide 1: Graphical Representation of Data
Dr. Hina Dutt                                                                                       hina.dutt@seecs.edu.pk
SEECS-NUST

> **Q: Summarize the core mechanism of Presentation Of Data and how it applies to MATH-361-Probability_and_Statistics_D_2K25-BSCS-15.**
>
> *A:* Based on 3. Graphical Representation of Data.pptx, Slide 2: Presentation Of Data

> **Q: Summarize the core mechanism of Slide 3 and how it applies to MATH-361-Probability_and_Statistics_D_2K25-BSCS-15.**
>
> *A:* Based on 3. Graphical Representation of Data.pptx, Slide 3: Bar Chart

> **Q: Summarize the core mechanism of Bar Chart and how it applies to MATH-361-Probability_and_Statistics_D_2K25-BSCS-15.**
>
> *A:* Based on 3. Graphical Representation of Data.pptx, Slide 4: Bar Chart
A bar graph is a graph that displays the frequency or numerical distribution of a categorical variable, showing values for each bar next to each other for easy comparison.

---

## MATH-361-Probability_and_Statistics_D_2K25-BSCS-15 - 7. Box Plot, Skewness, Kurtosis

### 📝 Executive Summary
This lecture on '7. Box Plot, Skewness, Kurtosis' covers key fundamentals across 16 slides/sections. Major themes include Box Plot, skewness, kurtosis, Box Plot, Slide 4, Slide 5. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Skewness**: measure of symmetry, or more precisely, the lack of symmetry. A distribution, or data set, is symmetric if it looks the same to the left and right of the center point.
- **Box Plot, skewness, kurtosis**: Box Plot, skewness, kurtosis Dr. Hina Dutt                                                                                       hina.dutt@seecs.edu.pk SEECS-NUST...
- **Box Plot**: Box Plot...
- **Slide 4**: Box Plot...
- **Slide 5**: Box Plot 50% 50%...
- **How to Construct Box Plot**: How to Construct Box Plot...
- **Example 1; Box Plot**: Example 1; Box Plot The wheat production (in kgs) of 20 acres is given as: 1120 1240 1320 1040 1080 1200 1440 1360 1680 1730 1785 1342 1960 1880 1755 1720 1600 1470 1750 1885. Cons...
- **Example 2; (Box Plot)**: Example 2; (Box Plot) Construct the box plot for the distribution of the marks given below....
- **Comparison of Box Plots of Two Data Sets**: Comparison of Box Plots of Two Data Sets A:  Min = 50             Q1 = 65             Med = 70             Q3 = 80             Max = 100 B:   Min = 40             Q1 = 60          ...
- **Box Plot Vs Histogram**: Box Plot Vs Histogram...

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Box Plot, skewness, kurtosis and how it applies to MATH-361-Probability_and_Statistics_D_2K25-BSCS-15.**
>
> *A:* Based on 7. Box Plot, Skewness, Kurtosis, Slide 1: Box Plot, skewness, kurtosis
Dr. Hina Dutt                                                                                       hina.dutt@seecs.edu.pk
SEECS-NUST

> **Q: Summarize the core mechanism of Box Plot and how it applies to MATH-361-Probability_and_Statistics_D_2K25-BSCS-15.**
>
> *A:* Based on 7. Box Plot, Skewness, Kurtosis, Slide 3: Box Plot

> **Q: Summarize the core mechanism of Slide 4 and how it applies to MATH-361-Probability_and_Statistics_D_2K25-BSCS-15.**
>
> *A:* Based on 7. Box Plot, Skewness, Kurtosis, Slide 4: Box Plot

> **Q: Summarize the core mechanism of Slide 5 and how it applies to MATH-361-Probability_and_Statistics_D_2K25-BSCS-15.**
>
> *A:* Based on 7. Box Plot, Skewness, Kurtosis, Slide 5: Box Plot
50%
50%

---

## MATH-361-Probability_and_Statistics_D_2K25-BSCS-15 - 6. Measure of Dispersion.pptx

### 📝 Executive Summary
This lecture on '6. Measure of Dispersion.pptx' covers key fundamentals across 27 slides/sections. Major themes include Measure of dispersion, Mean, Why study Dispersion?, What is Dispersion. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Consider these**: for hours worked each day:
- **Reference Book**: Probability and Statistics for Engineers, 9th  edition by Richard A. Johnson
- **Measure of dispersion**: Measure of dispersion Dr. Hina Dutt                                                                                       hina.dutt@seecs.edu.pk SEECS-NUST...
- **Why study Dispersion?**: Why study Dispersion?...
- **What is Dispersion**: What is Dispersion...
- **Dispersion**: Dispersion...
- **Significance of Measuring Dispersion**: Significance of Measuring Dispersion...
- **Measures of Dispersion**: Measures of Dispersion...
- **Range**: Range...
- **Variance**: Variance...

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Measure of dispersion and how it applies to MATH-361-Probability_and_Statistics_D_2K25-BSCS-15.**
>
> *A:* Based on 6. Measure of Dispersion.pptx, Slide 1: Measure of dispersion
Dr. Hina Dutt                                                                                       hina.dutt@seecs.edu.pk
SEECS-NUST

> **Q: Summarize the core mechanism of Mean and how it applies to MATH-361-Probability_and_Statistics_D_2K25-BSCS-15.**
>
> *A:* Based on 6. Measure of Dispersion.pptx, Slide 2: Mean
Consider these means for hours worked each day:
X = {7, 8, 6, 7, 7, 6, 8, 7}
X = 7
Notice that all the data values are bunched near the mean.
Thus, 7 would be a pretty good prediction of the average hours worked each day.
X = {12, 2, 0, 14, 10, 

> **Q: Summarize the core mechanism of Why study Dispersion? and how it applies to MATH-361-Probability_and_Statistics_D_2K25-BSCS-15.**
>
> *A:* Based on 6. Measure of Dispersion.pptx, Slide 3: Why study Dispersion?

> **Q: Summarize the core mechanism of What is Dispersion and how it applies to MATH-361-Probability_and_Statistics_D_2K25-BSCS-15.**
>
> *A:* Based on 6. Measure of Dispersion.pptx, Slide 4: What is Dispersion

---

## MATH-361-Probability_and_Statistics_D_2K25-BSCS-15 - 4. Measure of Central tendency.pptx

### 📝 Executive Summary
The lecture provides an introduction to Measures of Central Tendency, which quantify the tendency of observations to cluster in the central part of a dataset. It explores three fundamental measures: Mean, Median, and Mode, each serving to locate the middle of the data in a distinct sense. The Mean is introduced as a balancing point, with methods for calculation covering ungrouped, weighted, combined, and grouped data, including adjustments for change of origin and scale.

The Median is defined as the value that divides an ordered dataset into two equal parts, and its calculation for individual observations, ungrouped frequency distributions, and grouped data, as well as graphically from an Ogive, is outlined. The Mode, characterized by potentially not being unique, is discussed for ungrouped frequency distributions, grouped data, and its identification from a Histogram. A significant portion of the lecture is dedicated to comparing these three measures based on critical properties such as stability, reliance on all observations, sensitivity to extreme values, existence as a data point, applicability to different data types (qualitative vs. quantitative), and appropriateness for skewed distributions.

### 🔑 Key Definitions
- **Central Tendency**: The tendency of observations to cluster in the central part of the data.
- **Measure of Central Tendency**: The value of data that summarizes the central tendency or locates in the middle of the data (in some sense). Also known as a Measure of Location or Position.
- **Mean**: A measure of central tendency often described as a balancing point, calculated for various data types including ungrouped, weighted, combined, and grouped data.
- **Weighted Mean**: A type of mean where each data point's contribution to the average is not equal, but rather weighted by a certain factor.
- **Combined Mean**: A mean calculated when combining multiple datasets, each with its own mean and number of observations.
- **Median**: A value which divides an ordered data into two equal parts, one part comprising of observations greater than and the other part smaller than it.
- **Mode**: The value that appears most frequently in a data set. It may not be unique or may not exist.
- **Median Class**: The class interval in a frequency distribution where the median is located.
- **Modal Class**: The class interval in a frequency distribution that contains the mode.

### 💡 Core Conceptual Questions
> **Q: Explain why the Median is considered a more appropriate measure of average than the Mean for a highly skewed data set, based on the properties discussed in the lecture.**
>
> *A:* The Median is a more appropriate measure for highly skewed data because it is 'unaffected by the extreme values' that often characterize skewed distributions. In contrast, the Mean is 'affected by the extreme values' and is therefore 'not an appropriate measure of average for a highly skewed data,' as these extreme values can pull the mean significantly in one direction, potentially misrepresenting the central tendency of the bulk of the data.

> **Q: Discuss the applicability of Mean, Median, and Mode to qualitative and quantitative data, citing specific details from the lecture.**
>
> *A:* According to the lecture, the Mean is 'calculated only for the quantitative data,' meaning it cannot be used for qualitative (categorical) data. The Median 'can be calculated for the ranked qualitative data,' indicating it has applicability to qualitative data that can be ordered. The Mode, however, 'can be calculated for the qualitative data,' making it the most versatile in terms of data type applicability, as it can be used for both qualitative (ranked or unranked) and quantitative data.

> **Q: Describe two key characteristics of the Mode as a measure of central tendency, as highlighted in the lecture, particularly concerning its existence and sensitivity to extreme values.**
>
> *A:* Two key characteristics of the Mode are its insensitivity to extreme values and its guaranteed existence as a data point in the set. The lecture explicitly states that the Mode is 'unaffected by the extreme values,' meaning outliers or unusually large/small values do not distort its value. Furthermore, unlike the Mean and Median, the Mode 'exist as a data point in the set,' implying that it is always one of the actual observations present in the dataset. Additionally, the lecture notes that the Mode 'may have more than one value' and 'May not exist' (though the latter contradicts 'exist as a data point in the set' on the same slide, 'may not be unique' is also mentioned on slide 31, hence for this question, focusing on the primary characteristics of existence *as a data point* and *unaffected by extreme values* is best based on the comparative slide).

---

## HU-101-Islamic_Studies_A_2K25-BSAI-2 - Assignment Cover Page.docx

### 📝 Executive Summary
No extractable text found for Assignment Cover Page.docx.

### 🔑 Key Definitions

### 💡 Core Conceptual Questions
---

## HU-101-Islamic_Studies_A_2K25-BSAI-2 - Slide 2 Thematic study of Quran and Ethics.pdf

### 📝 Executive Summary
This lecture on 'Slide 2 Thematic study of Quran and Ethics.pdf' covers key fundamentals across 34 slides/sections. Major themes include Thematic Study of Quran, Oneness of Allah (التوحيد), Prophets (The Messengers), Responsibilities of Prophets. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Total Number of Prophets**: (There are 25 names of Prophets
- **Prophet pbuh said**: “whoever takes bath five
- **Conditions of Salah**: Islam, Mentality, Puberty,
- **Obligations of Salah**: Intention, first takbeer,
- **Fard**: Fasting in the month of Ramzan, fasting as
- **Nafl**: fasting in the month of shawwal, ‘Arafa (عرفة, the
- **Status of dowry**: It’s an obligatory on husband to give it
- **Quran**: “Say to the believing men to turn away their eyes (from what is unlawful) and to restrain their
- **Allah says in Quran**: “Let there arise out of you a group of people
- **Specific Tauba**: i.e., to ask forgiveness of the

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Thematic Study of Quran and how it applies to HU-101-Islamic_Studies_A_2K25-BSAI-2.**
>
> *A:* Based on Slide 2 Thematic study of Quran and Ethics.pdf, p.1: Thematic Study of Quran
General division of Quran
The whole Quran is divided into three major topics:
• Islamic doctrine (عقيدة اإلسالم)
• Obligations and rulings (أحكام القرآن)
• Proverbs (أمثال القرآن) & Stories of Previous 
nations (قصص القرآن)
Is

> **Q: Summarize the core mechanism of Oneness of Allah (التوحيد) and how it applies to HU-101-Islamic_Studies_A_2K25-BSAI-2.**
>
> *A:* Based on Slide 2 Thematic study of Quran and Ethics.pdf, p.2: Oneness of Allah (التوحيد)
Tawheed ar-Ruboobeeyah
“Maintaining the oneness of Lordship” i.e. 
affirming that Allah is one, without partners in his 
sovereignty)
Tawheed al-Asmaa’ wa-Sifaat
“Maintaining the unity of Allah’s Names and 
Attributes” i.e.

> **Q: Summarize the core mechanism of Prophets (The Messengers) and how it applies to HU-101-Islamic_Studies_A_2K25-BSAI-2.**
>
> *A:* Based on Slide 2 Thematic study of Quran and Ethics.pdf, p.3: Prophets (The Messengers)
Difference between “Nabi & Rasool”:
Every Rasool is a Nabi but not every Nabi 
is a Rasool.
Rasool is the one who receives the new 
law (sharia) and the Nabi is the one who is 
sent to confirm the law (sharia) of the one 


> **Q: Summarize the core mechanism of Responsibilities of Prophets and how it applies to HU-101-Islamic_Studies_A_2K25-BSAI-2.**
>
> *A:* Based on Slide 2 Thematic study of Quran and Ethics.pdf, p.5: Responsibilities of Prophets
• Conveying the message & Calling People 
towards Allah 
• Bringing glad tidings and warnings
• Reforming and purifying people’s soul
• Correction deviant ideas & Directing the 
affairs of the Ummah
• Establishing Proof
•

---

## HU-101-Islamic_Studies_A_2K25-BSAI-2 - Slide 1

### 📝 Executive Summary
This lecture on 'Slide 1' covers key fundamentals across 22 slides/sections. Major themes include HU-101, • Why we need to study Islam?, Why we need to, Guidelines & Rules. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Sirat-ul**: Nabi (Peace and Blessings be upon Him)
- **Linguistic Meaning**: The word “Quran,” a verbal noun, is equivalent in meaning to “qira’ah,” as both come
- **Literal Meaning**: It’s the last sacred book revealed by Allah swt on His beloved Prophet Muhammad (peace
- **For example**: the shortest revelation is:
- **HU-101**: HU-101 Islamic Studies Instructor Dr. Ammar Ahmed HOD GE-JSPPL...
- **• Why we need to study Islam?**: • Why we need to study Islam? • Guidelines and Rules to follow • Course contents • Assessment methods • Take Away Introduction Session...
- **Why we need to**: Why we need to  study Islam? Purpose of Life in the World Why need for Divine Guidance Informal and Formal way of Learning Attitude of ours towards this subject Dominance of L...
- **Guidelines & Rules**: Guidelines & Rules • Change of Intention • Show Respect to the subject • Time management • Sitting arrangement • Be Righteous in your life...
- **HU-101**: HU-101  Islamic Studies Course Contents CLO/PLO Mapping Course Learning  Outcomes Discuss the basic beliefs of Islam and the purpose of life. C2 Explain Islamic ethical and social ...
- **Quizzes = 4 x 10           [10 %]**: Quizzes = 4 x 10           [10 %] Assignments = 2 x 10   [5%] Class Participation [5%] Midterm = 1 x 50 [30 %] ESE = 1 x 100 [50 %] Semester Assessments...

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of HU-101 and how it applies to HU-101-Islamic_Studies_A_2K25-BSAI-2.**
>
> *A:* Based on Slide 1, p.1: HU-101
Islamic Studies
Instructor
Dr. Ammar Ahmed
HOD GE-JSPPL

> **Q: Summarize the core mechanism of • Why we need to study Islam? and how it applies to HU-101-Islamic_Studies_A_2K25-BSAI-2.**
>
> *A:* Based on Slide 1, p.2: • Why we need to study Islam?
• Guidelines and Rules to follow
• Course contents
• Assessment methods
• Take Away
Introduction Session

> **Q: Summarize the core mechanism of Why we need to and how it applies to HU-101-Islamic_Studies_A_2K25-BSAI-2.**
>
> *A:* Based on Slide 1, p.4: Why we need to 
study Islam?
Purpose of Life in the World
Why need for Divine Guidance
Informal and Formal way of Learning
Attitude of ours towards this subject
Dominance of Logical Reasoning
Muslim Atheist mindset

> **Q: Summarize the core mechanism of Guidelines & Rules and how it applies to HU-101-Islamic_Studies_A_2K25-BSAI-2.**
>
> *A:* Based on Slide 1, p.5: Guidelines & Rules
• Change of Intention
• Show Respect to the subject
• Time management
• Sitting arrangement
• Be Righteous in your life

---

## HU-101-Islamic_Studies_A_2K25-BSAI-2 - Course Outline.pdf

### 📝 Executive Summary
This lecture on 'Course Outline.pdf' covers key fundamentals across 6 slides/sections. Major themes include Islamic Studies, For NCEAC Accreditation, •​, challenges faced by. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Hadith**: while also understanding Islam’s contributions to civilization, governance, and modern
- **Living by the Quran**: Etiquette and its Daily
- **Self**: Accountability and the Belief in the
- **Sirat-un**: Nabi (Peace and Blessings be upon
- **Digital Ethics**: Islamic Guidelines for Social
- **End**: Semester Exam (40-50%)
- **Lost Islamic History**: Reclaiming Muslim Civilisation from the Past by Firas Alkhateeb
- **Group**: based presentations in which students identify and analyze a pressing social issue they observe in their
- **Quiz Policy**: The quizzes will be unannounced and normally last for ten minutes. The question framed is to test the
- **Project Policy**: Students will be required to develop a project during the course which should be completed towards

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Islamic Studies and how it applies to HU-101-Islamic_Studies_A_2K25-BSAI-2.**
>
> *A:* Based on Course Outline.pdf, p.1: Islamic Studies 
 
Department 
General Education - JSPPL 
Knowledge Group 
 
Program 
AI/DS/SE 
Class 
 
Course code 
HU-101 
Academic Session/Semester 
Fall 2026 
Course name 
Islamic Studies 
Prerequisite (course name and 
code, if applicable): 
Ni

> **Q: Summarize the core mechanism of For NCEAC Accreditation and how it applies to HU-101-Islamic_Studies_A_2K25-BSAI-2.**
>
> *A:* Based on Course Outline.pdf, p.2: For NCEAC Accreditation 
 
Academi
c 
Educatio
n 
Knowle
dge for 
Solving 
Computi
ng 
Problem
s 
Problem 
Analysis 
Design/
Develop
ment of 
Solution
s 
Modern 
Tool 
Usage 
Individual 
and 
Teamwork 
Communi
cation 
Individual 
and 
Collaborati
ve 

> **Q: Summarize the core mechanism of •​ and how it applies to HU-101-Islamic_Studies_A_2K25-BSAI-2.**
>
> *A:* Based on Course Outline.pdf, p.3: •​
The Perfection of His Political and Military 
Leadership. 
•​
The Relation of the Ummah with the Holy 
Prophet (Peace and Blessings be upon Him). 
9 
Midterm Exam 
10-11 
Family and Society in Islam 
•​
Honoring and Maintaining the Family. 
•​
Gen

> **Q: Summarize the core mechanism of challenges faced by and how it applies to HU-101-Islamic_Studies_A_2K25-BSAI-2.**
>
> *A:* Based on Course Outline.pdf, p.4: challenges faced by 
Muslim. 
18 
End Semester Exam 
 
Assessment Methods: 
Assessment 
Percentage 
 
1 
Quizzes (10-15%) 
10 
2 
Assignments (5-10%) 
5 
3 
Class participation (5-10%) 
5 
4 
Term Project Report 
- 
5 
Mid-Term Exam (25-35%) 
30 
6 


---

## HU-101-Islamic_Studies_A_2K25-BSAI-2 - HU-101 Islamic Studies Students notes.pdf

### 📝 Executive Summary
This lecture on 'HU-101 Islamic Studies Students notes.pdf' covers key fundamentals across 137 slides/sections. Major themes include 1, 2, 3, 4. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Allah saying**: Allah swt wrote the decrees of His creation fifty thousand years before He
- **on qadar**: part of Iman, without it, a person’s belief is incomplete. This qadar concept
- **also**: that every good and bad moment, beneficial and harmful thing that happens to
- **Belief in pre**: destination is an undisputed article of faith in Islam. For some people, this
- **Imam Ahmad has said**: Qadar (pre-estimation) is the power of Allah. It is one of the secrets
- **know that there**: difference between the things that happen without our will and those
- **Companions said**: “O Prophet of Allah! Should we then not do and just depend?”
- **He said**: “Do and everything that was created for you will be made easy.” The
- **Prophet added**: “Do O my brother, do and what was created for you will be
- **Al-Aswad al**: Duwali in the rein of Ali r.a. For the zabar a dot above the letter, for the zair

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of 1 and how it applies to HU-101-Islamic_Studies_A_2K25-BSAI-2.**
>
> *A:* Based on HU-101 Islamic Studies Students notes.pdf, p.1: 1 
 
 
 
 
NATIONAL UNIVERSITY OF SCIENCES AND 
TECHNOLOGY 
 
HU-101 
Islamic Studies 
 (Student Reading Notes) 
 
 
 
Dr. Ammar Ahmed 
HOD Department of Islamic Studies 
General Education

> **Q: Summarize the core mechanism of 2 and how it applies to HU-101-Islamic_Studies_A_2K25-BSAI-2.**
>
> *A:* Based on HU-101 Islamic Studies Students notes.pdf, p.2: 2 
 
Table of contents 
 
Introduction to Quran and Prophetic Hadith; the Divine Guidance ................................................ 3 
Fundamental Theological Principles of Islam ................................................................

> **Q: Summarize the core mechanism of 3 and how it applies to HU-101-Islamic_Studies_A_2K25-BSAI-2.**
>
> *A:* Based on HU-101 Islamic Studies Students notes.pdf, p.3: 3 
 
Introduction to Quran and Prophetic Hadith; the Divine Guidance 
 
Introduction to Islam 
Islam (Arabic: اإلسالم) is a verbal noun originating from the tri-literal root S-L-M which 
forms a large class of words mostly relating to concepts of who

> **Q: Summarize the core mechanism of 4 and how it applies to HU-101-Islamic_Studies_A_2K25-BSAI-2.**
>
> *A:* Based on HU-101 Islamic Studies Students notes.pdf, p.4: 4 
 
Faith in Predestination (Qadr): Qadar means decree, judgment, ultimate destiny and to 
sort things out. Literally it means “Allah has the knowledge of everything, how and when 
things will happen before its occurrence.” Abdullah bin Amr r.a said

---

## EE-347-Computer_Networks_A_2K25-BSAI-2 - Lecture 2 - Network Core, Performance  Protocol Layers - Copy.pptx

### 📝 Executive Summary
This lecture on 'Lecture 2 - Network Core, Performance  Protocol Layers - Copy.pptx' covers key fundamentals across 59 slides/sections. Major themes include EE-347 Computer networks, Chapter 1: roadmap, The network core, Two key network-core functions. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Network edge**: hosts, access network, physical media
- **Network core**: packet/circuit switching, internet structure
- **Performance**: loss, delay, throughput
- **Packet-switching**: hosts break application-layer messages into packets
- **Local action**: move arriving packets from router’s input link to appropriate router output link
- **Global action**: determine source-destination paths taken by packets
- **Packet**: switching: store-and-forward
- **Packet queuing and loss**: if arrival rate (in bps) to link exceeds transmission rate (bps) of link for some period of time:
- **End-to**: end resources allocated to, reserved for “call” between source and destination
- **Excessive congestion possible**: packet delay and loss due to buffer overflow

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of EE-347 Computer networks and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture 2 - Network Core, Performance  Protocol Layers - Copy.pptx, Slide 1: EE-347 Computer networks
Instructor: 
Asst Prof Mobeena shahzad
Network Core, Performance & Protocol Layers

> **Q: Summarize the core mechanism of Chapter 1: roadmap and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture 2 - Network Core, Performance  Protocol Layers - Copy.pptx, Slide 2: Chapter 1: roadmap
What is the Internet?
What is a protocol?
Network edge: hosts, access network, physical media
Network core: packet/circuit switching, internet structure
Performance: loss, delay, throughput
Protocol layers, service models
History
2

> **Q: Summarize the core mechanism of The network core and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture 2 - Network Core, Performance  Protocol Layers - Copy.pptx, Slide 3: The network core
Mesh of interconnected Routers

Packet-switching: hosts break application-layer messages into packets

Network forwards packets from one router to the next, across links on path from source to destination
mobile network
home network


> **Q: Summarize the core mechanism of Two key network-core functions and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture 2 - Network Core, Performance  Protocol Layers - Copy.pptx, Slide 4: Two key network-core functions
Forwarding: 
“switching”
Local action: move arriving packets from router’s input link to appropriate router output link
Routing: 
Global action: determine source-destination paths taken by packets
Routing algorithms
Rou

---

## EE-347-Computer_Networks_A_2K25-BSAI-2 - Lab 3 TCP

### 📝 Executive Summary
No extractable text found for Lab 3 TCP.

### 🔑 Key Definitions

### 💡 Core Conceptual Questions
---

## EE-347-Computer_Networks_A_2K25-BSAI-2 - Lab 4 UDP Analysis (1)

### 📝 Executive Summary
No extractable text found for Lab 4 UDP Analysis (1).

### 🔑 Key Definitions

### 💡 Core Conceptual Questions
---

## EE-347-Computer_Networks_A_2K25-BSAI-2 - Lecture 3 - Application Layer - 1.pptx

### 📝 Executive Summary
This lecture on 'Lecture 3 - Application Layer - 1.pptx' covers key fundamentals across 53 slides/sections. Major themes include EE-347 Computer networks, Application layer: overview, Application Layer: overview, Some network apps. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Real**: time video conferencing (e.g., Zoom)
- **P2P**: students exchange notes among themselves.]
- **Process**: program running within a host
- **Note**: Applications with P2P architectures have client processes & server processes
- **UDP**: quickly dropping individually addressed postcards into the mail system.]
- **HTTP**: HyperText Transfer Protocol
- **Non**: persistent HTTP: example
- **Host**: www-net.cs.umass.edu\r\n
- **User-Agent**: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:80.0) Gecko/20100101 Firefox/80.0 \r\n
- **Accept**: text/html,application/xhtml+xml\r\n

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of EE-347 Computer networks and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture 3 - Application Layer - 1.pptx, Slide 1: EE-347 Computer networks
Instructor: 
Asst Prof Mobeena shahzad
Application Layer – 1

> **Q: Summarize the core mechanism of Application layer: overview and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture 3 - Application Layer - 1.pptx, Slide 2: Application layer: overview
Principles of network applications
Web and HTTP

E-mail, SMTP, IMAP
The Domain Name System DNS
P2P applications
video streaming and content distribution networks
socket programming with UDP and TCP
2

> **Q: Summarize the core mechanism of Application Layer: overview and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture 3 - Application Layer - 1.pptx, Slide 3: Application Layer: overview
Our goals: 
conceptual and implementation aspects of application-layer protocols
transport-layer service models
client-server paradigm
peer-to-peer paradigm
learn about protocols by examining popular application-layer prot

> **Q: Summarize the core mechanism of Some network apps and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture 3 - Application Layer - 1.pptx, Slide 4: Some network apps
Social networking
Web
Text messaging
E-mail
Multi-user network games
Streaming stored video (YouTube, Hulu, Netflix) 
P2P file sharing
Voice over IP (e.g., Skype)
Real-time video conferencing (e.g., Zoom)
Internet search
Remote logi

---

## EE-347-Computer_Networks_A_2K25-BSAI-2 - Lecture 1 - Introduction

### 📝 Executive Summary
This lecture on 'Lecture 1 - Introduction' covers key fundamentals across 25 slides/sections. Major themes include EE-347 Computer networks, Overview, Slide 3, Slide 4. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Network edge**: hosts, access network, physical media
- **Network core**: packet/circuit switching, internet structure
- **Performance**: loss, delay, throughput
- **The Internet**: a “nuts and bolts” view
- **Internet**: “network of networks”
- **RFC**: Request for Comments
- **IETF**: Internet Engineering Task Force
- **Access networks**: digital subscriber line (DSL)
- **Ethernet**: wired access at 100Mbps, 1Gbps, 10Gbps
- **WiFi**: wireless access points at 11, 54, 450 Mbps

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of EE-347 Computer networks and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture 1 - Introduction, Slide 1: EE-347 Computer networks
Instructor: 
Asst Prof Mobeena shahzad
Introduction - Internet

> **Q: Summarize the core mechanism of Overview and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture 1 - Introduction, Slide 2: Overview
What is the Internet? What is a protocol?
Network edge: hosts, access network, physical media
Network core: packet/circuit switching, internet structure
Performance: loss, delay, throughput
Protocol layers, service models

> **Q: Summarize the core mechanism of Slide 3 and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture 1 - Introduction, Slide 3: Internet
The Internet: a “nuts and bolts” view

> **Q: Summarize the core mechanism of Slide 4 and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture 1 - Introduction, Slide 4: Internet: “network of networks”
Interconnected ISPs
mobile network
home network
enterprise
          network
national or global ISP
local or regional ISP
datacenter 
network
content 
provider 
network
protocols are everywhere
control sending, receivi

---

## EE-347-Computer_Networks_A_2K25-BSAI-2 - Lecture 4 - Application Layer - 2.pptx

### 📝 Executive Summary
This lecture on 'Lecture 4 - Application Layer - 2.pptx' covers key fundamentals across 38 slides/sections. Major themes include EE-347 Computer networks, Application layer: overview, Slide 3, E-mail: mail servers. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Scenario**: Alice sends e-mail to Bob
- **SMTP**: Comparison with HTTP
- **Body**: the “message” , ASCII characters only
- **Retrieving email**: mail access protocols
- **IMAP**: Internet Mail Access Protocol [RFC 3501]:
- **Application-layer protocol**: hosts, DNS servers communicate to resolve names (address/name translation)
- **Note**: core Internet function, implemented as application-layer protocol
- **DNS**: translating host names to IP addresses
- **Comcast DNS servers alone**: 600B DNS queries/day
- **Akamai DNS servers alone**: 2.2T DNS queries/day

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of EE-347 Computer networks and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture 4 - Application Layer - 2.pptx, Slide 1: EE-347 Computer networks
Instructor: 
Asst Prof Mobeena shahzad
Application Layer – Part 2

> **Q: Summarize the core mechanism of Application layer: overview and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture 4 - Application Layer - 2.pptx, Slide 2: Application layer: overview
Principles of network applications
Web and HTTP

E-mail, SMTP, IMAP
The Domain Name System DNS
Socket programming with UDP and TCP
2

> **Q: Summarize the core mechanism of Slide 3 and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture 4 - Application Layer - 2.pptx, Slide 3: 3
E-mail
Three major components: 
user agents 
mail servers 
Simple Mail Transfer Protocol: SMTP

User Agent
“mail reader”
composing, editing, reading mail messages
e.g., Outlook, iPhone mail client
outgoing, incoming messages stored on server

> **Q: Summarize the core mechanism of E-mail: mail servers and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture 4 - Application Layer - 2.pptx, Slide 4: E-mail: mail servers
Mail servers:
mailbox contains incoming messages for user
message queue of outgoing mail messages

SMTP protocol 
between mail servers to send email messages

client: sending mail server
server: receiving mail server
4

---

## EE-347-Computer_Networks_A_2K25-BSAI-2 - Course Outline Computer Network (BS-AI, Fall 2026) Mobeena Shahzad.pdf

### 📝 Executive Summary
This lecture on 'Course Outline Computer Network (BS-AI, Fall 2026) Mobeena Shahzad.pdf' covers key fundamentals across 4 slides/sections. Major themes include COURSE OUTLINE, CLO 4, Lab Experiments (if applicable):, Textbook: Computer Networking: A Top-Down Approach 8th Edition, Jim Kurose and K. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **BSAI**: 2 [CR-23-Acad Block]
- **Conducted through in**: class or lab activities.
- **Topic 0 and 1**: Introduction (Chapter 1)
- **Topic 1**: Standardization and Layering (Chapter 1)
- **Topic 2**: Application Layer [DNS] (Chapter 2)
- **Topic 3**: Transport Layer [UDP] (Chapter 3)
- **Topic 4**: Network Layer [IP addressing, Sub-netting] (Chapter 4)
- **Topic 5**: Data Link Layer [Framing, Addressing, ARP] (Chapter 6)
- **End**: Semester Exam (40-50%)
- **Textbook**: Computer Networking: A Top-Down Approach 8th Edition, Jim Kurose and Keith Ross, 2022

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of COURSE OUTLINE and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Course Outline Computer Network (BS-AI, Fall 2026) Mobeena Shahzad.pdf, p.1: COURSE OUTLINE 
 
 Department: 
Faculty of Computing 
Knowledge Group: 
Computer Networks 
 Programme: 
BS Artificial Intelligence 
Class: 
BSAI-2 [CR-23-Acad Block] 
 Course code: 
EE-347 
Academic Session/Semester: 
Fall 2026 
 Course name: 
Comput

> **Q: Summarize the core mechanism of CLO 4 and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Course Outline Computer Network (BS-AI, Fall 2026) Mobeena Shahzad.pdf, p.2: CLO 4 
Implement various networking 
functions using modern tools and 
hands-on programming. 
5 
P-4 
Psychomotor 
Lab Reports, Final 
Project 
 
*GA (CS)  
*1 (Academic Education), *2 (Knowledge for Solving Computing Problems), *3 (Problem Analysis)

> **Q: Summarize the core mechanism of Lab Experiments (if applicable): and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Course Outline Computer Network (BS-AI, Fall 2026) Mobeena Shahzad.pdf, p.3: Lab Experiments (if applicable): 
 
Lab 1 
Socket Programming in Linux/ GNU C (Part 1) 
Lab 2 
Socket Programming in Linux/ GNU C (Part 2) 
Lab 3 
Network Programming (Client/Server) Using Python (Part 3) 
Lab 4 
Wireshark – HTTP (Hypertext Transfer 

> **Q: Summarize the core mechanism of Textbook: Computer Networking: A Top-Down Approach 8th Edition, Jim Kurose and K and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Course Outline Computer Network (BS-AI, Fall 2026) Mobeena Shahzad.pdf, p.4: Textbook: Computer Networking: A Top-Down Approach 8th Edition, Jim Kurose and Keith Ross, 2022 
Reference: 
• 
“Computer Networks” (5th Edition) by Andrew S. Tenanbaum and David Wetherall [T&W] 
• 
“TCP/IP Protocol Suite” (4th Edition) by Behrouz A.

---

## EE-347-Computer_Networks_A_2K25-BSAI-2 - Lecture 0 - Course Introduction.pptx

### 📝 Executive Summary
This lecture on 'Lecture 0 - Course Introduction.pptx' covers key fundamentals across 13 slides/sections. Major themes include EE-347 Computer networks, COURSE Introduction, Course Description, Course Learning Outcomes (CLO). Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **The Internet**: a “nuts and bolts” view
- **Computer Networking**: A Top-Down Approach
- **EE-347 Computer networks**: EE-347 Computer networks Instructor:  Asst Prof Mobeena shahzad Course Introduction...
- **COURSE Introduction**: COURSE Introduction [Presenter Notes: CS:  Enrollment Code : 064978123  AI: Enrollment Code : 960837421]...
- **Course Description**: Course Description The field of computer networking is evolving rapidly, making it crucial to understand not just the current state of networks, but also the underlying principles ...
- **Course Learning Outcomes (CLO)**: Course Learning Outcomes (CLO)...
- **Focus of the subject**: Focus of the subject Focus on conceptual introduction of computer networks and more importantly their underlying design principles  A top-down approach Architectures Algorithms Pro...
- **Focus of the subject**: Focus of the subject What happens “under the hood” when you browse the Internet?  Suppose you are on a SEECS lab machine. You type “www.example.com” on your browser.  Can you expla...
- **Slide 8**: Internet The Internet: a “nuts and bolts” view...
- **Slide 9**: Internet-connected devices Web-enabled toaster + weather forecaster Others?...

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of EE-347 Computer networks and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture 0 - Course Introduction.pptx, Slide 1: EE-347 Computer networks
Instructor: 
Asst Prof Mobeena shahzad
Course Introduction

> **Q: Summarize the core mechanism of COURSE Introduction and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture 0 - Course Introduction.pptx, Slide 2: COURSE Introduction
[Presenter Notes: CS: 
Enrollment Code : 064978123

AI:
Enrollment Code : 960837421]

> **Q: Summarize the core mechanism of Course Description and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture 0 - Course Introduction.pptx, Slide 3: Course Description
The field of computer networking is evolving rapidly, making it crucial to understand not just the current state of networks, but also the underlying principles and reasoning behind their design. 

This course aims to introduce the

> **Q: Summarize the core mechanism of Course Learning Outcomes (CLO) and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture 0 - Course Introduction.pptx, Slide 4: Course Learning Outcomes (CLO)

---

## EE-347-Computer_Networks_A_2K25-BSAI-2 - Lab 2 HTTP

### 📝 Executive Summary
No extractable text found for Lab 2 HTTP.

### 🔑 Key Definitions

### 💡 Core Conceptual Questions
---

## EE-347-Computer_Networks_A_2K25-BSAI-2 - Lab 05

### 📝 Executive Summary
No extractable text found for Lab 05.

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

## MATH-361-Probability_and_Statistics_D_2K25-BSCS-15 - 5. Measure of Non-Central tendency

### 📝 Executive Summary
This lecture segment focuses on 'Measures of Non-Central tendency,' with a primary emphasis on 'Quantiles.' The material outlines how to calculate quantiles for different types of data presentations: individual observations, ungrouped frequency distributions, and grouped data. Through various examples, the lecture demonstrates the process of finding specific quantiles, including lower quartiles, upper quartiles, deciles (e.g., the seventh decile), and percentiles (e.g., the 63rd percentile).

The lecture also includes exercises that require the calculation of these measures, such as finding the median, upper, and lower quartiles from given data. Dr. Hina Dutt from SEECS-NUST delivers the lecture, and the recommended reference book for further study is 'Probability and Statistics for Engineers, 9th edition by Richard A. Johnson.'

### 🔑 Key Definitions
- **Measure of Non-Central tendency**: The overarching topic of the lecture, introduced by Dr. Hina Dutt, focusing on statistical measures that describe the position of a value in a data set relative to other values, rather than its central tendency.
- **Quantiles**: A key concept discussed within the 'Measure of Non-Central tendency' topic, representing points in a distribution that divide the data into equal-sized subgroups.
- **Individual Observations**: A type of data presentation where each data point is listed separately, for which quantiles can be calculated, as exemplified in 'Quantiles; Example 1'.
- **Ungrouped frequency Distribution**: A type of data presentation where distinct values are listed along with their frequencies, for which quantiles can be calculated, as exemplified in 'Quantiles; Example 2'.
- **Grouped Data**: A type of data presentation where data is organized into classes or intervals along with their frequencies, for which quantiles can be calculated, as exemplified in 'Quantiles; Example 3'.
- **Lower Quartile**: A specific type of quantile that is exemplified for calculation with individual observations and mentioned in 'Exercise 2' alongside the upper quartile.
- **Seventh Decile**: A specific type of quantile, equivalent to the 70th percentile, whose calculation is exemplified for individual observations in 'Quantiles; Example 1'.
- **Upper Quartile**: A specific type of quantile that is exemplified for calculation with grouped data and mentioned in 'Exercise 2' alongside the lower quartile.
- **63rd Percentile**: A specific type of quantile, which divides the data such that 63% of the data falls below it, whose calculation is exemplified for grouped data in 'Quantiles; Example 3'.
- **Median**: A statistical measure listed in 'Exercise 2' along with upper and lower quartiles, to be calculated from data.

### 💡 Core Conceptual Questions
> **Q: Identify and briefly describe the three distinct types of data distributions for which the lecture explicitly discusses how to calculate quantiles.**
>
> *A:* The lecture explicitly covers three types of data distributions for quantile calculation:
1.  **Individual Observations:** This refers to raw, unorganized data where each data point is listed separately (e.g., wheat production in Example 1).
2.  **Ungrouped frequency Distribution:** This involves data presented with distinct values and their corresponding frequencies (e.g., number of assistants in Example 2).
3.  **Grouped Data:** This refers to data organized into classes or intervals, along with their frequencies (e.g., examination marks in Example 3).

Key Grading Criteria:
*   Mention all three types: Individual Observations, Ungrouped frequency Distribution, and Grouped Data.
*   Provide a brief, accurate description or example for each, grounding it in the lecture's context.

> **Q: List the specific types of quantiles that are exemplified or explicitly mentioned for calculation within the lecture's examples and exercises.**
>
> *A:* The lecture exemplifies or explicitly mentions the calculation of several specific types of quantiles:
*   **Lower Quartile:** Exemplified for individual observations in Example 1 and mentioned in Exercise 2.
*   **Seventh Decile:** Exemplified for individual observations in Example 1.
*   **Upper Quartile:** Exemplified for grouped data in Example 3 and mentioned in Exercise 2.
*   **63rd Percentile:** Exemplified for grouped data in Example 3.
*   **Median:** Mentioned in Exercise 2 alongside upper and lower quartiles.

Key Grading Criteria:
*   Include Lower Quartile, Seventh Decile, Upper Quartile, 63rd Percentile, and Median.
*   Reference their appearance in examples or exercises where applicable.

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

## MATH-361-Probability_and_Statistics_D_2K25-BSCS-15 - 3. Graphical Representation of Data.pptx

### 📝 Executive Summary
This lecture provides a comprehensive overview of various graphical methods used for data representation, emphasizing their unique characteristics and applications. It introduces fundamental graphical tools starting with the Bar Chart, which is designed to display the frequency or numerical distribution of categorical variables, allowing for easy comparison between different categories. The lecture also covers the concept of multiple category bar charts.

Following this, the lecture delves into methods for representing quantitative data, including Histograms, Frequency Polygons, and Ogives. A Histogram uses bars centered above scores or class intervals, where the height represents frequency and adjacent bars touch. Frequency Polygons offer an alternative to histograms by using straight line segments to connect points representing class frequencies and midpoints. Ogives are presented as graphs for cumulative frequencies plotted against class boundaries. The lecture further explores less common but useful tools like Dot Diagrams, which place a dot for each observation on a number line, and the Stem and Leaf Display, a technique for simultaneously sorting and displaying data by dividing each number into a 'stem' and a 'leaf'. Variations such as Double-stem and Five-stem displays are also introduced, highlighting the versatility of these graphical representations in statistical analysis.

### 🔑 Key Definitions
- **Bar Chart**: A graph that displays the frequency or numerical distribution of a categorical variable, showing values for each bar next to each other for easy comparison.
- **Histogram**: A graph where a bar is centered above each score (or class interval) so that the height of the bar corresponds to the frequency and the width extends to the real limits, so that adjacent bars touch.
- **Frequency Polygon**: A line graph used to display and compare the distribution of quantitative data, using straight line segments to connect points that represent class frequencies and midpoints instead of rectangular bars.
- **Ogive**: A graph obtained by plotting the cumulative frequencies of a distribution against the upper and lower class boundaries, with points joined by straight line segments.
- **Dot Diagram**: A graph constructed by placing a dot for each observation above its value on a number line.
- **Stem and Leaf Display**: A technique for simultaneously sorting and displaying data sets in which each number (value) in the data is divided into two parts: a Stem and a Leaf.
- **Stem (Stem and Leaf Display)**: The leading digit(s) of each number in a Stem and Leaf Display, used in sorting.
- **Leaf (Stem and Leaf Display)**: The rest of the number or the trailing digit(s) in a Stem and Leaf Display.

### 💡 Core Conceptual Questions
> **Q: Based on the lecture's definitions, differentiate between a Bar Chart and a Histogram, highlighting their distinct characteristics.**
>
> *A:* A Bar Chart displays the frequency or numerical distribution of a *categorical variable*, showing values for each bar next to each other for easy comparison. In contrast, a Histogram is used for displaying numerical distribution (typically of a quantitative variable), where a bar is centered above each score or class interval, and crucially, the height corresponds to the frequency while the width extends to the real limits, causing *adjacent bars to touch*. The primary distinction lies in the type of variable they represent (categorical vs. typically quantitative) and the physical spacing between the bars (separated vs. touching).

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

## MATH-361-Probability_and_Statistics_D_2K25-BSCS-15 - 7. Box Plot, Skewness, Kurtosis

### 📝 Executive Summary
This lecture introduces fundamental concepts in descriptive statistics, focusing on data visualization and characterization. The first major topic covered is the Box Plot, a graphical tool used for visualizing data distributions, with examples demonstrating its construction and application in comparing two different datasets. The lecture also briefly mentions the comparison between Box Plots and Histograms as alternative visualization methods.

The second core theme is the characterization of a distribution's shape using Skewness and Kurtosis. Skewness is defined as a measure of symmetry, or lack thereof, distinguishing between symmetric, positively-skewed, and negatively-skewed distributions based on the relative positions of the mean, median, and mode. Kurtosis, on the other hand, characterizes the relative peakedness or flatness of a distribution when compared to a normal distribution. The lecture touches upon the existence of 'Measures of Skewness' and 'Measures of Kurtosis' but does not detail their calculation.

### 🔑 Key Definitions
- **Box Plot**: A graphical method for displaying data distribution, examples provided for constructing and comparing data sets.
- **Skewness**: A measure of symmetry, or more precisely, the lack of symmetry in a distribution or data set.
- **Symmetric Distribution**: A distribution or data set that looks the same to the left and right of its center point, where Mean = Median = Mode.
- **Positively-Skewed Distribution**: A distribution where the mean is greater than the median, which is greater than the mode (Mean > Median > Mode).
- **Negatively-Skewed Distribution**: A distribution where the mode is greater than the median, which is greater than the mean (Mode > Median > Mean).
- **Kurtosis**: Characterizes the relative peakedness or flatness of a distribution compared to the normal distribution.

### 💡 Core Conceptual Questions
> **Q: Explain the concept of skewness and differentiate between positively and negatively skewed distributions based on the relationship between mean, median, and mode.**
>
> *A:* Skewness is a measure of symmetry, or more precisely, the lack of symmetry, in a distribution or data set. A distribution is symmetric if it looks the same to the left and right of its center point, in which case the Mean = Median = Mode.

For a positively-skewed distribution, the mean is typically greater than the median, which is greater than the mode (Mean > Median > Mode). This usually indicates a tail extending towards the right.

For a negatively-skewed distribution, the mode is typically greater than the median, which is greater than the mean (Mode > Median > Mean). This usually indicates a tail extending towards the left.

> **Q: Briefly describe what kurtosis measures in a distribution.**
>
> *A:* Kurtosis characterizes the relative peakedness or flatness of a distribution. This measurement is typically made in comparison to the normal distribution, indicating how concentrated the data is around the mean and how heavy the tails are.

> **Q: Based on the provided data for Data Set A and B (Slide 9), compare their medians and maximum values.**
>
> *A:* For Data Set A:
Median (Med) = 70
Maximum (Max) = 100

For Data Set B:
Median (Med) = 70
Maximum (Max) = 100

Based on this information, both Data Set A and Data Set B have the same median value of 70 and the same maximum value of 100.

---

## MATH-361-Probability_and_Statistics_D_2K25-BSCS-15 - 6. Measure of Dispersion.pptx

### 📝 Executive Summary
This lecture on '6. Measure of Dispersion.pptx' covers key fundamentals across 27 slides/sections. Major themes include Measure of dispersion, Mean, Why study Dispersion?, What is Dispersion. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Consider these**: for hours worked each day:
- **Reference Book**: Probability and Statistics for Engineers, 9th  edition by Richard A. Johnson
- **Measure of dispersion**: Measure of dispersion Dr. Hina Dutt                                                                                       hina.dutt@seecs.edu.pk SEECS-NUST...
- **Why study Dispersion?**: Why study Dispersion?...
- **What is Dispersion**: What is Dispersion...
- **Dispersion**: Dispersion...
- **Significance of Measuring Dispersion**: Significance of Measuring Dispersion...
- **Measures of Dispersion**: Measures of Dispersion...
- **Range**: Range...
- **Variance**: Variance...

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Measure of dispersion and how it applies to MATH-361-Probability_and_Statistics_D_2K25-BSCS-15.**
>
> *A:* Based on 6. Measure of Dispersion.pptx, Slide 1: Measure of dispersion
Dr. Hina Dutt                                                                                       hina.dutt@seecs.edu.pk
SEECS-NUST

> **Q: Summarize the core mechanism of Mean and how it applies to MATH-361-Probability_and_Statistics_D_2K25-BSCS-15.**
>
> *A:* Based on 6. Measure of Dispersion.pptx, Slide 2: Mean
Consider these means for hours worked each day:
X = {7, 8, 6, 7, 7, 6, 8, 7}
X = 7
Notice that all the data values are bunched near the mean.
Thus, 7 would be a pretty good prediction of the average hours worked each day.
X = {12, 2, 0, 14, 10, 

> **Q: Summarize the core mechanism of Why study Dispersion? and how it applies to MATH-361-Probability_and_Statistics_D_2K25-BSCS-15.**
>
> *A:* Based on 6. Measure of Dispersion.pptx, Slide 3: Why study Dispersion?

> **Q: Summarize the core mechanism of What is Dispersion and how it applies to MATH-361-Probability_and_Statistics_D_2K25-BSCS-15.**
>
> *A:* Based on 6. Measure of Dispersion.pptx, Slide 4: What is Dispersion

---

## HU-101-Islamic_Studies_A_2K25-BSAI-2 - Assignment Cover Page.docx

### 📝 Executive Summary
No extractable text found for Assignment Cover Page.docx.

### 🔑 Key Definitions

### 💡 Core Conceptual Questions
---

## HU-101-Islamic_Studies_A_2K25-BSAI-2 - Slide 2 Thematic study of Quran and Ethics.pdf

### 📝 Executive Summary
This lecture on 'Slide 2 Thematic study of Quran and Ethics.pdf' covers key fundamentals across 34 slides/sections. Major themes include Thematic Study of Quran, Oneness of Allah (التوحيد), Prophets (The Messengers), Responsibilities of Prophets. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Total Number of Prophets**: (There are 25 names of Prophets
- **Prophet pbuh said**: “whoever takes bath five
- **Conditions of Salah**: Islam, Mentality, Puberty,
- **Obligations of Salah**: Intention, first takbeer,
- **Fard**: Fasting in the month of Ramzan, fasting as
- **Nafl**: fasting in the month of shawwal, ‘Arafa (عرفة, the
- **Status of dowry**: It’s an obligatory on husband to give it
- **Quran**: “Say to the believing men to turn away their eyes (from what is unlawful) and to restrain their
- **Allah says in Quran**: “Let there arise out of you a group of people
- **Specific Tauba**: i.e., to ask forgiveness of the

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Thematic Study of Quran and how it applies to HU-101-Islamic_Studies_A_2K25-BSAI-2.**
>
> *A:* Based on Slide 2 Thematic study of Quran and Ethics.pdf, p.1: Thematic Study of Quran
General division of Quran
The whole Quran is divided into three major topics:
• Islamic doctrine (عقيدة اإلسالم)
• Obligations and rulings (أحكام القرآن)
• Proverbs (أمثال القرآن) & Stories of Previous 
nations (قصص القرآن)
Is

> **Q: Summarize the core mechanism of Oneness of Allah (التوحيد) and how it applies to HU-101-Islamic_Studies_A_2K25-BSAI-2.**
>
> *A:* Based on Slide 2 Thematic study of Quran and Ethics.pdf, p.2: Oneness of Allah (التوحيد)
Tawheed ar-Ruboobeeyah
“Maintaining the oneness of Lordship” i.e. 
affirming that Allah is one, without partners in his 
sovereignty)
Tawheed al-Asmaa’ wa-Sifaat
“Maintaining the unity of Allah’s Names and 
Attributes” i.e.

> **Q: Summarize the core mechanism of Prophets (The Messengers) and how it applies to HU-101-Islamic_Studies_A_2K25-BSAI-2.**
>
> *A:* Based on Slide 2 Thematic study of Quran and Ethics.pdf, p.3: Prophets (The Messengers)
Difference between “Nabi & Rasool”:
Every Rasool is a Nabi but not every Nabi 
is a Rasool.
Rasool is the one who receives the new 
law (sharia) and the Nabi is the one who is 
sent to confirm the law (sharia) of the one 


> **Q: Summarize the core mechanism of Responsibilities of Prophets and how it applies to HU-101-Islamic_Studies_A_2K25-BSAI-2.**
>
> *A:* Based on Slide 2 Thematic study of Quran and Ethics.pdf, p.5: Responsibilities of Prophets
• Conveying the message & Calling People 
towards Allah 
• Bringing glad tidings and warnings
• Reforming and purifying people’s soul
• Correction deviant ideas & Directing the 
affairs of the Ummah
• Establishing Proof
•

---

## HU-101-Islamic_Studies_A_2K25-BSAI-2 - Slide 1

### 📝 Executive Summary
This lecture on 'Slide 1' covers key fundamentals across 22 slides/sections. Major themes include HU-101, • Why we need to study Islam?, Why we need to, Guidelines & Rules. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Sirat-ul**: Nabi (Peace and Blessings be upon Him)
- **Linguistic Meaning**: The word “Quran,” a verbal noun, is equivalent in meaning to “qira’ah,” as both come
- **Literal Meaning**: It’s the last sacred book revealed by Allah swt on His beloved Prophet Muhammad (peace
- **For example**: the shortest revelation is:
- **HU-101**: HU-101 Islamic Studies Instructor Dr. Ammar Ahmed HOD GE-JSPPL...
- **• Why we need to study Islam?**: • Why we need to study Islam? • Guidelines and Rules to follow • Course contents • Assessment methods • Take Away Introduction Session...
- **Why we need to**: Why we need to  study Islam? Purpose of Life in the World Why need for Divine Guidance Informal and Formal way of Learning Attitude of ours towards this subject Dominance of L...
- **Guidelines & Rules**: Guidelines & Rules • Change of Intention • Show Respect to the subject • Time management • Sitting arrangement • Be Righteous in your life...
- **HU-101**: HU-101  Islamic Studies Course Contents CLO/PLO Mapping Course Learning  Outcomes Discuss the basic beliefs of Islam and the purpose of life. C2 Explain Islamic ethical and social ...
- **Quizzes = 4 x 10           [10 %]**: Quizzes = 4 x 10           [10 %] Assignments = 2 x 10   [5%] Class Participation [5%] Midterm = 1 x 50 [30 %] ESE = 1 x 100 [50 %] Semester Assessments...

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of HU-101 and how it applies to HU-101-Islamic_Studies_A_2K25-BSAI-2.**
>
> *A:* Based on Slide 1, p.1: HU-101
Islamic Studies
Instructor
Dr. Ammar Ahmed
HOD GE-JSPPL

> **Q: Summarize the core mechanism of • Why we need to study Islam? and how it applies to HU-101-Islamic_Studies_A_2K25-BSAI-2.**
>
> *A:* Based on Slide 1, p.2: • Why we need to study Islam?
• Guidelines and Rules to follow
• Course contents
• Assessment methods
• Take Away
Introduction Session

> **Q: Summarize the core mechanism of Why we need to and how it applies to HU-101-Islamic_Studies_A_2K25-BSAI-2.**
>
> *A:* Based on Slide 1, p.4: Why we need to 
study Islam?
Purpose of Life in the World
Why need for Divine Guidance
Informal and Formal way of Learning
Attitude of ours towards this subject
Dominance of Logical Reasoning
Muslim Atheist mindset

> **Q: Summarize the core mechanism of Guidelines & Rules and how it applies to HU-101-Islamic_Studies_A_2K25-BSAI-2.**
>
> *A:* Based on Slide 1, p.5: Guidelines & Rules
• Change of Intention
• Show Respect to the subject
• Time management
• Sitting arrangement
• Be Righteous in your life

---

## HU-101-Islamic_Studies_A_2K25-BSAI-2 - Course Outline.pdf

### 📝 Executive Summary
This lecture on 'Course Outline.pdf' covers key fundamentals across 6 slides/sections. Major themes include Islamic Studies, For NCEAC Accreditation, •​, challenges faced by. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Hadith**: while also understanding Islam’s contributions to civilization, governance, and modern
- **Living by the Quran**: Etiquette and its Daily
- **Self**: Accountability and the Belief in the
- **Sirat-un**: Nabi (Peace and Blessings be upon
- **Digital Ethics**: Islamic Guidelines for Social
- **End**: Semester Exam (40-50%)
- **Lost Islamic History**: Reclaiming Muslim Civilisation from the Past by Firas Alkhateeb
- **Group**: based presentations in which students identify and analyze a pressing social issue they observe in their
- **Quiz Policy**: The quizzes will be unannounced and normally last for ten minutes. The question framed is to test the
- **Project Policy**: Students will be required to develop a project during the course which should be completed towards

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of Islamic Studies and how it applies to HU-101-Islamic_Studies_A_2K25-BSAI-2.**
>
> *A:* Based on Course Outline.pdf, p.1: Islamic Studies 
 
Department 
General Education - JSPPL 
Knowledge Group 
 
Program 
AI/DS/SE 
Class 
 
Course code 
HU-101 
Academic Session/Semester 
Fall 2026 
Course name 
Islamic Studies 
Prerequisite (course name and 
code, if applicable): 
Ni

> **Q: Summarize the core mechanism of For NCEAC Accreditation and how it applies to HU-101-Islamic_Studies_A_2K25-BSAI-2.**
>
> *A:* Based on Course Outline.pdf, p.2: For NCEAC Accreditation 
 
Academi
c 
Educatio
n 
Knowle
dge for 
Solving 
Computi
ng 
Problem
s 
Problem 
Analysis 
Design/
Develop
ment of 
Solution
s 
Modern 
Tool 
Usage 
Individual 
and 
Teamwork 
Communi
cation 
Individual 
and 
Collaborati
ve 

> **Q: Summarize the core mechanism of •​ and how it applies to HU-101-Islamic_Studies_A_2K25-BSAI-2.**
>
> *A:* Based on Course Outline.pdf, p.3: •​
The Perfection of His Political and Military 
Leadership. 
•​
The Relation of the Ummah with the Holy 
Prophet (Peace and Blessings be upon Him). 
9 
Midterm Exam 
10-11 
Family and Society in Islam 
•​
Honoring and Maintaining the Family. 
•​
Gen

> **Q: Summarize the core mechanism of challenges faced by and how it applies to HU-101-Islamic_Studies_A_2K25-BSAI-2.**
>
> *A:* Based on Course Outline.pdf, p.4: challenges faced by 
Muslim. 
18 
End Semester Exam 
 
Assessment Methods: 
Assessment 
Percentage 
 
1 
Quizzes (10-15%) 
10 
2 
Assignments (5-10%) 
5 
3 
Class participation (5-10%) 
5 
4 
Term Project Report 
- 
5 
Mid-Term Exam (25-35%) 
30 
6 


---

## HU-101-Islamic_Studies_A_2K25-BSAI-2 - HU-101 Islamic Studies Students notes.pdf

### 📝 Executive Summary
This lecture on 'HU-101 Islamic Studies Students notes.pdf' covers key fundamentals across 137 slides/sections. Major themes include 1, 2, 3, 4. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Allah saying**: Allah swt wrote the decrees of His creation fifty thousand years before He
- **on qadar**: part of Iman, without it, a person’s belief is incomplete. This qadar concept
- **also**: that every good and bad moment, beneficial and harmful thing that happens to
- **Belief in pre**: destination is an undisputed article of faith in Islam. For some people, this
- **Imam Ahmad has said**: Qadar (pre-estimation) is the power of Allah. It is one of the secrets
- **know that there**: difference between the things that happen without our will and those
- **Companions said**: “O Prophet of Allah! Should we then not do and just depend?”
- **He said**: “Do and everything that was created for you will be made easy.” The
- **Prophet added**: “Do O my brother, do and what was created for you will be
- **Al-Aswad al**: Duwali in the rein of Ali r.a. For the zabar a dot above the letter, for the zair

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of 1 and how it applies to HU-101-Islamic_Studies_A_2K25-BSAI-2.**
>
> *A:* Based on HU-101 Islamic Studies Students notes.pdf, p.1: 1 
 
 
 
 
NATIONAL UNIVERSITY OF SCIENCES AND 
TECHNOLOGY 
 
HU-101 
Islamic Studies 
 (Student Reading Notes) 
 
 
 
Dr. Ammar Ahmed 
HOD Department of Islamic Studies 
General Education

> **Q: Summarize the core mechanism of 2 and how it applies to HU-101-Islamic_Studies_A_2K25-BSAI-2.**
>
> *A:* Based on HU-101 Islamic Studies Students notes.pdf, p.2: 2 
 
Table of contents 
 
Introduction to Quran and Prophetic Hadith; the Divine Guidance ................................................ 3 
Fundamental Theological Principles of Islam ................................................................

> **Q: Summarize the core mechanism of 3 and how it applies to HU-101-Islamic_Studies_A_2K25-BSAI-2.**
>
> *A:* Based on HU-101 Islamic Studies Students notes.pdf, p.3: 3 
 
Introduction to Quran and Prophetic Hadith; the Divine Guidance 
 
Introduction to Islam 
Islam (Arabic: اإلسالم) is a verbal noun originating from the tri-literal root S-L-M which 
forms a large class of words mostly relating to concepts of who

> **Q: Summarize the core mechanism of 4 and how it applies to HU-101-Islamic_Studies_A_2K25-BSAI-2.**
>
> *A:* Based on HU-101 Islamic Studies Students notes.pdf, p.4: 4 
 
Faith in Predestination (Qadr): Qadar means decree, judgment, ultimate destiny and to 
sort things out. Literally it means “Allah has the knowledge of everything, how and when 
things will happen before its occurrence.” Abdullah bin Amr r.a said

---

## EE-347-Computer_Networks_A_2K25-BSAI-2 - Lecture 2 - Network Core, Performance  Protocol Layers - Copy.pptx

### 📝 Executive Summary
This lecture on 'Lecture 2 - Network Core, Performance  Protocol Layers - Copy.pptx' covers key fundamentals across 59 slides/sections. Major themes include EE-347 Computer networks, Chapter 1: roadmap, The network core, Two key network-core functions. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Network edge**: hosts, access network, physical media
- **Network core**: packet/circuit switching, internet structure
- **Performance**: loss, delay, throughput
- **Packet-switching**: hosts break application-layer messages into packets
- **Local action**: move arriving packets from router’s input link to appropriate router output link
- **Global action**: determine source-destination paths taken by packets
- **Packet**: switching: store-and-forward
- **Packet queuing and loss**: if arrival rate (in bps) to link exceeds transmission rate (bps) of link for some period of time:
- **End-to**: end resources allocated to, reserved for “call” between source and destination
- **Excessive congestion possible**: packet delay and loss due to buffer overflow

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of EE-347 Computer networks and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture 2 - Network Core, Performance  Protocol Layers - Copy.pptx, Slide 1: EE-347 Computer networks
Instructor: 
Asst Prof Mobeena shahzad
Network Core, Performance & Protocol Layers

> **Q: Summarize the core mechanism of Chapter 1: roadmap and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture 2 - Network Core, Performance  Protocol Layers - Copy.pptx, Slide 2: Chapter 1: roadmap
What is the Internet?
What is a protocol?
Network edge: hosts, access network, physical media
Network core: packet/circuit switching, internet structure
Performance: loss, delay, throughput
Protocol layers, service models
History
2

> **Q: Summarize the core mechanism of The network core and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture 2 - Network Core, Performance  Protocol Layers - Copy.pptx, Slide 3: The network core
Mesh of interconnected Routers

Packet-switching: hosts break application-layer messages into packets

Network forwards packets from one router to the next, across links on path from source to destination
mobile network
home network


> **Q: Summarize the core mechanism of Two key network-core functions and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture 2 - Network Core, Performance  Protocol Layers - Copy.pptx, Slide 4: Two key network-core functions
Forwarding: 
“switching”
Local action: move arriving packets from router’s input link to appropriate router output link
Routing: 
Global action: determine source-destination paths taken by packets
Routing algorithms
Rou

---

## EE-347-Computer_Networks_A_2K25-BSAI-2 - Lab 3 TCP

### 📝 Executive Summary
No extractable text found for Lab 3 TCP.

### 🔑 Key Definitions

### 💡 Core Conceptual Questions
---

## EE-347-Computer_Networks_A_2K25-BSAI-2 - Lab 4 UDP Analysis (1)

### 📝 Executive Summary
No extractable text found for Lab 4 UDP Analysis (1).

### 🔑 Key Definitions

### 💡 Core Conceptual Questions
---

## EE-347-Computer_Networks_A_2K25-BSAI-2 - Lecture 3 - Application Layer - 1.pptx

### 📝 Executive Summary
This lecture on 'Lecture 3 - Application Layer - 1.pptx' covers key fundamentals across 53 slides/sections. Major themes include EE-347 Computer networks, Application layer: overview, Application Layer: overview, Some network apps. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Real**: time video conferencing (e.g., Zoom)
- **P2P**: students exchange notes among themselves.]
- **Process**: program running within a host
- **Note**: Applications with P2P architectures have client processes & server processes
- **UDP**: quickly dropping individually addressed postcards into the mail system.]
- **HTTP**: HyperText Transfer Protocol
- **Non**: persistent HTTP: example
- **Host**: www-net.cs.umass.edu\r\n
- **User-Agent**: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:80.0) Gecko/20100101 Firefox/80.0 \r\n
- **Accept**: text/html,application/xhtml+xml\r\n

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of EE-347 Computer networks and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture 3 - Application Layer - 1.pptx, Slide 1: EE-347 Computer networks
Instructor: 
Asst Prof Mobeena shahzad
Application Layer – 1

> **Q: Summarize the core mechanism of Application layer: overview and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture 3 - Application Layer - 1.pptx, Slide 2: Application layer: overview
Principles of network applications
Web and HTTP

E-mail, SMTP, IMAP
The Domain Name System DNS
P2P applications
video streaming and content distribution networks
socket programming with UDP and TCP
2

> **Q: Summarize the core mechanism of Application Layer: overview and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture 3 - Application Layer - 1.pptx, Slide 3: Application Layer: overview
Our goals: 
conceptual and implementation aspects of application-layer protocols
transport-layer service models
client-server paradigm
peer-to-peer paradigm
learn about protocols by examining popular application-layer prot

> **Q: Summarize the core mechanism of Some network apps and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture 3 - Application Layer - 1.pptx, Slide 4: Some network apps
Social networking
Web
Text messaging
E-mail
Multi-user network games
Streaming stored video (YouTube, Hulu, Netflix) 
P2P file sharing
Voice over IP (e.g., Skype)
Real-time video conferencing (e.g., Zoom)
Internet search
Remote logi

---

## EE-347-Computer_Networks_A_2K25-BSAI-2 - Lecture 1 - Introduction

### 📝 Executive Summary
This lecture on 'Lecture 1 - Introduction' covers key fundamentals across 25 slides/sections. Major themes include EE-347 Computer networks, Overview, Slide 3, Slide 4. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Network edge**: hosts, access network, physical media
- **Network core**: packet/circuit switching, internet structure
- **Performance**: loss, delay, throughput
- **The Internet**: a “nuts and bolts” view
- **Internet**: “network of networks”
- **RFC**: Request for Comments
- **IETF**: Internet Engineering Task Force
- **Access networks**: digital subscriber line (DSL)
- **Ethernet**: wired access at 100Mbps, 1Gbps, 10Gbps
- **WiFi**: wireless access points at 11, 54, 450 Mbps

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of EE-347 Computer networks and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture 1 - Introduction, Slide 1: EE-347 Computer networks
Instructor: 
Asst Prof Mobeena shahzad
Introduction - Internet

> **Q: Summarize the core mechanism of Overview and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture 1 - Introduction, Slide 2: Overview
What is the Internet? What is a protocol?
Network edge: hosts, access network, physical media
Network core: packet/circuit switching, internet structure
Performance: loss, delay, throughput
Protocol layers, service models

> **Q: Summarize the core mechanism of Slide 3 and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture 1 - Introduction, Slide 3: Internet
The Internet: a “nuts and bolts” view

> **Q: Summarize the core mechanism of Slide 4 and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture 1 - Introduction, Slide 4: Internet: “network of networks”
Interconnected ISPs
mobile network
home network
enterprise
          network
national or global ISP
local or regional ISP
datacenter 
network
content 
provider 
network
protocols are everywhere
control sending, receivi

---

## EE-347-Computer_Networks_A_2K25-BSAI-2 - Lecture 4 - Application Layer - 2.pptx

### 📝 Executive Summary
This lecture on 'Lecture 4 - Application Layer - 2.pptx' covers key fundamentals across 38 slides/sections. Major themes include EE-347 Computer networks, Application layer: overview, Slide 3, E-mail: mail servers. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **Scenario**: Alice sends e-mail to Bob
- **SMTP**: Comparison with HTTP
- **Body**: the “message” , ASCII characters only
- **Retrieving email**: mail access protocols
- **IMAP**: Internet Mail Access Protocol [RFC 3501]:
- **Application-layer protocol**: hosts, DNS servers communicate to resolve names (address/name translation)
- **Note**: core Internet function, implemented as application-layer protocol
- **DNS**: translating host names to IP addresses
- **Comcast DNS servers alone**: 600B DNS queries/day
- **Akamai DNS servers alone**: 2.2T DNS queries/day

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of EE-347 Computer networks and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture 4 - Application Layer - 2.pptx, Slide 1: EE-347 Computer networks
Instructor: 
Asst Prof Mobeena shahzad
Application Layer – Part 2

> **Q: Summarize the core mechanism of Application layer: overview and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture 4 - Application Layer - 2.pptx, Slide 2: Application layer: overview
Principles of network applications
Web and HTTP

E-mail, SMTP, IMAP
The Domain Name System DNS
Socket programming with UDP and TCP
2

> **Q: Summarize the core mechanism of Slide 3 and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture 4 - Application Layer - 2.pptx, Slide 3: 3
E-mail
Three major components: 
user agents 
mail servers 
Simple Mail Transfer Protocol: SMTP

User Agent
“mail reader”
composing, editing, reading mail messages
e.g., Outlook, iPhone mail client
outgoing, incoming messages stored on server

> **Q: Summarize the core mechanism of E-mail: mail servers and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture 4 - Application Layer - 2.pptx, Slide 4: E-mail: mail servers
Mail servers:
mailbox contains incoming messages for user
message queue of outgoing mail messages

SMTP protocol 
between mail servers to send email messages

client: sending mail server
server: receiving mail server
4

---

## EE-347-Computer_Networks_A_2K25-BSAI-2 - Course Outline Computer Network (BS-AI, Fall 2026) Mobeena Shahzad.pdf

### 📝 Executive Summary
This lecture on 'Course Outline Computer Network (BS-AI, Fall 2026) Mobeena Shahzad.pdf' covers key fundamentals across 4 slides/sections. Major themes include COURSE OUTLINE, CLO 4, Lab Experiments (if applicable):, Textbook: Computer Networking: A Top-Down Approach 8th Edition, Jim Kurose and K. Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **BSAI**: 2 [CR-23-Acad Block]
- **Conducted through in**: class or lab activities.
- **Topic 0 and 1**: Introduction (Chapter 1)
- **Topic 1**: Standardization and Layering (Chapter 1)
- **Topic 2**: Application Layer [DNS] (Chapter 2)
- **Topic 3**: Transport Layer [UDP] (Chapter 3)
- **Topic 4**: Network Layer [IP addressing, Sub-netting] (Chapter 4)
- **Topic 5**: Data Link Layer [Framing, Addressing, ARP] (Chapter 6)
- **End**: Semester Exam (40-50%)
- **Textbook**: Computer Networking: A Top-Down Approach 8th Edition, Jim Kurose and Keith Ross, 2022

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of COURSE OUTLINE and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Course Outline Computer Network (BS-AI, Fall 2026) Mobeena Shahzad.pdf, p.1: COURSE OUTLINE 
 
 Department: 
Faculty of Computing 
Knowledge Group: 
Computer Networks 
 Programme: 
BS Artificial Intelligence 
Class: 
BSAI-2 [CR-23-Acad Block] 
 Course code: 
EE-347 
Academic Session/Semester: 
Fall 2026 
 Course name: 
Comput

> **Q: Summarize the core mechanism of CLO 4 and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Course Outline Computer Network (BS-AI, Fall 2026) Mobeena Shahzad.pdf, p.2: CLO 4 
Implement various networking 
functions using modern tools and 
hands-on programming. 
5 
P-4 
Psychomotor 
Lab Reports, Final 
Project 
 
*GA (CS)  
*1 (Academic Education), *2 (Knowledge for Solving Computing Problems), *3 (Problem Analysis)

> **Q: Summarize the core mechanism of Lab Experiments (if applicable): and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Course Outline Computer Network (BS-AI, Fall 2026) Mobeena Shahzad.pdf, p.3: Lab Experiments (if applicable): 
 
Lab 1 
Socket Programming in Linux/ GNU C (Part 1) 
Lab 2 
Socket Programming in Linux/ GNU C (Part 2) 
Lab 3 
Network Programming (Client/Server) Using Python (Part 3) 
Lab 4 
Wireshark – HTTP (Hypertext Transfer 

> **Q: Summarize the core mechanism of Textbook: Computer Networking: A Top-Down Approach 8th Edition, Jim Kurose and K and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Course Outline Computer Network (BS-AI, Fall 2026) Mobeena Shahzad.pdf, p.4: Textbook: Computer Networking: A Top-Down Approach 8th Edition, Jim Kurose and Keith Ross, 2022 
Reference: 
• 
“Computer Networks” (5th Edition) by Andrew S. Tenanbaum and David Wetherall [T&W] 
• 
“TCP/IP Protocol Suite” (4th Edition) by Behrouz A.

---

## EE-347-Computer_Networks_A_2K25-BSAI-2 - Lecture 0 - Course Introduction.pptx

### 📝 Executive Summary
This lecture on 'Lecture 0 - Course Introduction.pptx' covers key fundamentals across 13 slides/sections. Major themes include EE-347 Computer networks, COURSE Introduction, Course Description, Course Learning Outcomes (CLO). Mastery of these concepts is crucial for upcoming course assessments.

### 🔑 Key Definitions
- **The Internet**: a “nuts and bolts” view
- **Computer Networking**: A Top-Down Approach
- **EE-347 Computer networks**: EE-347 Computer networks Instructor:  Asst Prof Mobeena shahzad Course Introduction...
- **COURSE Introduction**: COURSE Introduction [Presenter Notes: CS:  Enrollment Code : 064978123  AI: Enrollment Code : 960837421]...
- **Course Description**: Course Description The field of computer networking is evolving rapidly, making it crucial to understand not just the current state of networks, but also the underlying principles ...
- **Course Learning Outcomes (CLO)**: Course Learning Outcomes (CLO)...
- **Focus of the subject**: Focus of the subject Focus on conceptual introduction of computer networks and more importantly their underlying design principles  A top-down approach Architectures Algorithms Pro...
- **Focus of the subject**: Focus of the subject What happens “under the hood” when you browse the Internet?  Suppose you are on a SEECS lab machine. You type “www.example.com” on your browser.  Can you expla...
- **Slide 8**: Internet The Internet: a “nuts and bolts” view...
- **Slide 9**: Internet-connected devices Web-enabled toaster + weather forecaster Others?...

### 💡 Core Conceptual Questions
> **Q: Summarize the core mechanism of EE-347 Computer networks and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture 0 - Course Introduction.pptx, Slide 1: EE-347 Computer networks
Instructor: 
Asst Prof Mobeena shahzad
Course Introduction

> **Q: Summarize the core mechanism of COURSE Introduction and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture 0 - Course Introduction.pptx, Slide 2: COURSE Introduction
[Presenter Notes: CS: 
Enrollment Code : 064978123

AI:
Enrollment Code : 960837421]

> **Q: Summarize the core mechanism of Course Description and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture 0 - Course Introduction.pptx, Slide 3: Course Description
The field of computer networking is evolving rapidly, making it crucial to understand not just the current state of networks, but also the underlying principles and reasoning behind their design. 

This course aims to introduce the

> **Q: Summarize the core mechanism of Course Learning Outcomes (CLO) and how it applies to EE-347-Computer_Networks_A_2K25-BSAI-2.**
>
> *A:* Based on Lecture 0 - Course Introduction.pptx, Slide 4: Course Learning Outcomes (CLO)

---

## EE-347-Computer_Networks_A_2K25-BSAI-2 - Lab 2 HTTP

### 📝 Executive Summary
No extractable text found for Lab 2 HTTP.

### 🔑 Key Definitions

### 💡 Core Conceptual Questions
---

## EE-347-Computer_Networks_A_2K25-BSAI-2 - Lab 05

### 📝 Executive Summary
No extractable text found for Lab 05.

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

