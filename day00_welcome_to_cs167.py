# -*- coding: utf-8 -*-
"""Day00_Welcome_to_CS167.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/merriekay/S23-CS17-Notes/blob/main/Day00_Welcome_to_CS167.ipynb

# CS167: Day00
## Welcome to CS167

#### CS167: Machine Learning, Spring2023

Tuesday, January 24th, 2023

π [Course Schedule](https://docs.google.com/spreadsheets/d/e/2PACX-1vSvFV5Mz0_YZE1d5r3gQ8IMktE4cBAsJIlP30cl2GhEpSO0J-YWV62QokSDz-OcOCsEmxMuKpY0kVlR/pubhtml?gid=0&single=true) | π[PollEverywhere](https://pollev.com/meredithmoore011) | π [Syllabus](https://analytics.drake.edu/~moore/cs167_s23_syllabus.html)

#Title
## Heading #1
### Heading #2
#### Heading #3

Lists:
- bullet #1
- bullet #2
  - sub-item

[linky text] (then use link to site

`variable_name`

# Overview of Today:

How this is going to work:
- Introductions
- Syllabus and Logistics
- Notebook 00: Onboarding Walkthrough
- Introduction to Machine Learning

# Day 01 Admin Stuff:

## You should be working on:
- [ ] [Notebook #0](https://classroom.github.com/a/o6dY8OL6): CS167 Onboarding (intro questionniare, polleverywhere, GitHub, etc)
    - Due before class on Thursday 1/26--Classroom says by 11:59 (because both sections are merged), but the idea is to have things set up for class

# π Introductions:

Introduce yourself to your table:
- Name, year at Drake, majors, and something fun you did over break.

# Syllabus:

## Instructor:

Meredith Moore <br>
she | her <br>
meredith.moore@drake.edu <br>
325 Collier-Scrips (office) <br>


You can call me Professor Moore, Dr. Moore, or Meredith, I don't have a very strong preference. I'll always sign emails as Meredith.

## π Class Meeting Time and Place:

__Where:__ Harvey Ingham 0019

__When:__ Tuesday / Thursday:
- Section 1: 11:00 - 12:15
- Section 0: 12:15 - 1:45

## πͺ΄Office Hours

TBD based on your availability:
- [Please fill out this when2meet](https://www.when2meet.com/?18438746-oRViw)

## π§ Course Communication

The course content will be posted on the course Blackboard page. Any announcements will be sent using Blackboard's announcement feature (as well as email).

It is a personal goal of mine to respond to student emails within 24 hours of receipt. 

If you have not heard back from me within 24 hours, please send the email again--you can use one word in the email body, simply 'bump', and I'll understand that it's an email that I missed and need to take care of asap.

## Course Description:
This course introduces approaches to __developing computer programs that learn from data__. Both foundational and contemporary machine learning algorithms will be covered in the context of a variety of data and problem types. Specific topics will vary but may include:

- artificial neural networks
- k-nearest-neighbors
- decision trees
- random forests
- support vector machines
- convolutional neural networks
- recurrent neural networks
- other relevant advanced machine learning techniques

Students will develop their own implementations of the algorithms as well as utilizing modern machine learning software and programming libraries.

## Course Goals:
At the end of this course, students that have taken an active part should be able to: 
- apply a variety of modeling techniques to classification, regression, and unsupervised learning problems using data in different formats (such as typical structured data, text, and images). 
- create software which utilizes machine learning programming libraries in order to conduct machine-learning-based data analysis. 
- develop and conduct machine-learning-based data analysis experiments, and they will be able to interpret and explain the results.  
- Feel comfortable with using two industry standard tools: Google Colab and GitHub

## Names and Pronouns
Everyone has the right to be addressed by the name and pronouns that they use for themselves. 

I am committed to ensuring that I address you with your chosen name and pronouns, and expect everyone to do so. 

A studentβs chosen name and pronouns are to be respected at all times in our classroom. Please let me know in the Intro Questionnaire (part of Notebook 00) what name and pronouns we should use for you if they are not on the roster. 

Here are some resources to learn more:
- [Intro Handout on Pronouns](https://www.umass.edu/stonewall/sites/default/files/pronouns_intro.pdf)
- [Drakeβs Student Pronoun Policy](https://www.drake.edu/media/universitypolicies/academic/student-pronoun-policy.pdf)
- [Drakeβs Preferred Name Policy](https://www.drake.edu/media/universitypolicies/studentlife/Student%20Preferred%20Name.pdf)

## Grading
| **Category**  | **Percent Final Grade** | **Description**                                                     |
|:---------------|:-------------------------:|:---------------------------------------------------------------------|
| Notebooks     | 40%                     | In-class and take home assignments                                  |
| Quizzes       | 30%                     | 3 quizzes, 10% each |
| Projects      | 20%                     | 2 projects, each worth 10% of final grade                           |
| Participation | 10%                     | PollEverywhere participation, not based on correctness              |

### Letter Grade Scale
| __Final Grade__   |    |              |     |              |    |
|---------------|:----|--------------|:-----|--------------|:----|
| 93.0 - 100    | A  | 80.0 - 82.99 | B-  | 67 - 69.99   | D+ |
| 90.0 - 92.99  | A- | 77.0 - 79.99 | C+  | 63.0 - 66.99 | D  |
| 87.0 - 89.99  | B+ | 73.0 - 76.99 | C   | Below 63     | F  |
| 83.0 - 86.99  | B  | 70.0 - 72.99 | C-  |              |    |

### Notebooks (40%): 
Throughout the course, we will be learning to apply machine learning principles using Python machine learning tools. 

Machine learning code is often developed in and communicated using an interactive integrated development environment called __Jupyter Notebooks__ which support a natural interleaving of code, output/results, and mark-up documentation--what you're seeing right now is actually a Jupyter notebook.

You will regularly submit notebook files (files with the extension `.ipynb`) to demonstrate your proficiency with the Python tools we are
using. Given the long computation times of the programs you write, I will not usually be executing your code, so it is critical that the results from your executions are preserved in the notebook. You can expect to submit 6 notebooks throughout the course.

### Quizzes (30%):
There will be 3 quizzes that will be administered via Blackboard. They will not be timed, and you will have a few days to complete them. 

Quizzes should be completed individually, and will be due before class on the following Monday. There is no time limit on these quizzes, but they must be submitted before we convene for the next class. 

As in the real world, you will be allowed to use external resources like the class notes and the internet. You will be required to cite any sources that you used while completing these quizzes other than the class notes.

### Projects (20%):
The two projects in this course will emphasize the design, execution, and interpretation of machine learning experiments. 

The grading emphasis will be on how well you explain your data and experiment as well as your written interpretation. For these, you will submit Jupyter Notebooks with more extensive writing in the mark-up cells than for your regular notebook assignments.

### Participation (10%)

This is a highly interactive class. In other words, **active participation is an expectation and the norm**. You will receive credit for participating in class which will be counted towards your final grade. I will keep track of your participation using PollEverywhere. Throughout the class, I will pose questions using this polling software to get a better understanding of how the class is doing with the content. These responses will not be counted for correctness, but rather for completion. 

I respect your privacy. If you encounter challenges (physical health, mental health, of life in general) that interfere with your ability to participate in the course or complete your work, I will not require any kind of documentation. 

You also do not need to explain; you can simply inform me that you are experiencing problems and we will work together to figure out a plan that will enable you to complete the course if you want to. For example, If for some reason, you are unable to make the in-person class session, please email me and I will provide you with the zoom link for the day so you can attend class virtually.

If you are unable to participate in the course for a prolonged period, we will discuss whether an incomplete is the best option.

## Access and Success Accomodations
Accessibility is very important to me. Iβve done my best to design this course such that it is as universally designed as possibleβflexible attendance, recording lectures, removing timed exams, live captions in class, etc. However, I am more than happy to work with you if there are other accommodations that I can provide to help you succeed in this course.

 In my opinion, academic accommodations are severely underutilized. While I am committed to designing my courses to be accessible to everyone, I know that there are times when accommodations make a huge difference. Please, if you are neurodivergent, consider setting up an appointment with Access and Success to have access to accommodations. I am in your corner for this, please donβt hesitate to reach out to me if you have any questions.

### Process for Communicating Academic Accommodations: 
-  When students request accommodations, they must provide documentation to Access & Success. 
- First-year students, students new to requesting accommodations, and transfer students are required to make an appointment with Access & Success. Access & Success work together with the student to determine reasonable accommodations for each of the studentβs classes.  
- Returning students can fill out an accommodation request form, found on the Access & Success website, www.drake.edu/access-success.  The same process will be followed as above, however returning students do not need to meet with Access & Success unless their accommodations need to be changed.   

If you have a disability and require academic or physical accommodations in this course, please contact me and Access and Success Services (Michelle Laughlin, Director, Access and Success, at (515) 271-1835 or michelle.laughlin@drake.edu) in advance of the date the accommodations are needed. All requests for assistance must be received (at least) four full business days prior to the requested need.

# Blackboard Tour
Let's take a quick break and walk through the course Blackboard website.

## [Notebook 0: Onboarding](https://github.com/merriekay/CS167-Notebook-0)

__Due__: Thursday, 1/26 before class

We will be using a few helpful tools in this class:
- GitHub
- GitHub Classroom
- PollEverywhere
- Spotify 

[Notebook 00](https://github.com/merriekay/CS167-Notebook-0) will walk you through getting onboarded to these systems.

You need to respond to the 'quiz' on Blackboard to check off the steps for Notebook 0.

## Participation Cards:

It is a goal of mine to make my classrooms as __inclusive and equitable as possible__. 

Towards this goal, we will be using __participation cards__. 

How it's going to work: 
- Today, in class, we're going ot make __participation cards__
- At the start of class, I'll shuffle and draw a card. The person whose name is on that card becomes the __card bearer__ for the day. 
- The __card bearer__ is responsible for flipping cards and calling out the person whose name is on the card when I ask them to.

## Participation Cards (cont)

If your name is called out by the card bearer you have a few options: 
1. Answer the question
2. Ask what the question was (you'll be surprised how often, even I, forget what the question was). 
3. Say 'Pass', or 'I'm not sure'
4. Ask for a group 'huddle', where you can talk to your neighbors for a solution.

Participation cards are a solution to help the class participation be more equitable. They're not meant to induce anxiety, and I hope you'll find I use them in a way that is more fun than anxiety inducing.

# Arts and Crafts Time
Time to make your participation card!

> Make sure the following is neat, and clear so that the class can read your name.

What to include:
- __name__: (what you want to be called), at least first name and last initial, pronunciation help if you think it's necessary 
- __pronouns__: 
- __class name__: CS167
- Feel free to add decorations or whatever you'd like.

# Github Walkthrough

Setting up an S23-CS167 notes repository.

Accepting the Github Classroom assignment.

Changing settings to allow access to private repositories.

# π€ What is Machine Learning?

__Definition #1__: creating machines (e.g. computer programs) that improve automatically with experience

__Definition #2__: the field of study that gives computers the ability to learn without being explicitly programmed.

## How is Machine Learning different than Artificial Intelligence?

Let's play a game of chess β... 

An __artificial intelligence__ approach: 
- develop a heuristic (a way to tell which move is best)
    - Queen is 12 points
    - Rook is 8 points
    - Pawn is 1 point
    - etc...

- For any configuration of a chess board, establish the set of valid moves.
- __Search__ the set of possible moves in the future
- Select the move that maximizes the possible points

## How is Machine Learning different than Artificial Intelligence?
Let's play a game of chess β... 

A __machine learning__ approach:

- based on data
- Gather a bunch of chess game examples
- For any configuration, examine the database of moves of winning games
- Find the board configuration that is the 'closest' and make appropriate moves.

# π¬ Group Exercise:

Take 2 minutes to talk to your neighbors about the following:

### Come up with as many examples as you can of ways you interact with machine learning on a day-to-day basis.

Submit your answers to [PollEverywhere](https://PollEv.com/free_text_polls/gFVsn0AcPlNfYUmMNBz8E/respond).

## An Example: Classifying my dogs

Imagine we want to classify which of my dogs an image is of.

Our training data might look something like this: 
<div>
<img src="https://github.com/merriekay/S23-CS17-Notes/blob/main/images/ace_zo_pics.png?raw=1"/ width=600>
</div>

## An Example: Classifying my dogs
Then, when we have some new pictures of my dogs, the idea is that we can make a __prediction__ based on previous data as to whether it is Zoey or Ace in the photo. 

<div>
<img src="https://github.com/merriekay/S23-CS17-Notes/blob/main/images/ace.png?raw=1"/ width=300>
</div>

## Another Example: What species of Iris is this?
Use Polleverywhere to answer this question

- 5.1 cm petal, 7.2 cm sepal

<div>
<img src="https://github.com/merriekay/S23-CS17-Notes/blob/main/images/day0_iris_q1.png?raw=1"/>
</div>

## π¬ Group Exercise
The following image shows two models of whether or not a person is a football player based on their weight and height. 

__Which model do you think is *better* and why?__
<div>
<img src="https://github.com/merriekay/S23-CS17-Notes/blob/main/images/bias_variance_tradeoff.png?raw=1"/>
</div>

## Bias v Variance Tradeoff

### π¨ Termiology Alert!π¨ 
__Bias__ is the simplifying assumptions made by the model to make the target function easier to approximate.
- In other words, **bias** is erroneous assumptions in a learning model

__Variance__ is the amount that the estimate of the target function will change given different training data. 
- **variance** is the error from sensitivity to small fluctuations in the training set.

## β Concept Check Question
Which of the models below do you think has **high variance** (error from small fluctuations) and which one do you think has **high bias** (simplifying assumptions)?

<div>
<img src="https://github.com/merriekay/S23-CS17-Notes/blob/main/images/day01_bias_variance.png?raw=1"/>
</div>

## Machine Learning Variations

We are going to learn about a lot of different types of machine learning in CS167. Here are a few categories to look out for: 
- __classifcation__: identify which category it goes in. Examples: Spam or ham? Eric or Tim? Fish, amphibian, reptile, bird, or mammal
- __regression__: real-valued labels. Examples: price of Bitcoin, tomorrow's temperature, etc.
- __supervised learning__: data has labels, goal is to predict the labels of new instance. 
- __unsupervised learning__: data does not have a label, the goal is to analyze/cluster the examples. 
- __other issues__: missing data, sequential data, outlier anomaly detetion, and many more.
"""

