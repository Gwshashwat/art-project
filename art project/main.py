# 50 MCQ + 50 TRUE FALSE PER CHAPTER.
# QUESTION PAPER WILL CONTAIN 50 QUESTIONS ONLY.
# USER CAN CHOSSE THE CHAPTERS HE WANTS.

from eng.eng_ch1 import *
from cs.cs_ch1 import *
from cs.cs_ch2 import *
from cs.cs_ch3 import *
from cs.cs_ch4 import *
from cs.cs_ch5 import *
from cs.cs_ch6 import *
from cs.cs_ch7 import *
from cs.cs_ch8 import *
from cs.cs_ch9 import *
from cs.cs_ch10 import *
from cs.cs_ch11 import *
from cs.cs_ch12 import *
from cs.cs_ch13 import *
from cs.cs_ch14 import *
from cs.cs_ch15 import *
from cs.cs_ch16 import *
from cs.cs_ch17 import *
import random

def question(d1,d2,d3) : #d1 = MCQ  ,d2 = TURE FALSE,d3 = OPTIONS OF MCQ

    l1 = list(d1.keys())
    random.shuffle(l1)

    l2 = list(d2.keys())
    random.shuffle(l2)

    questions = []
    for a in range(26):
        try :
            questions.append(l1[a])
            questions.append(l2[a])

        except Exception :
            break

    random.shuffle(questions)

    i = 1
    correct_ans = 0
    wrong_ans = 0
    total_questions = len(l1) + len(l2)

    for q in questions :
        if q in l1 :

            while True :
                ans = input(f"{q} \n{d3[q]}\nEnter your choice (A/B/C/D) : ").upper()
                if ans == "A" or ans == "B" or ans == "C" or ans == "D" :
                    if ans == d1[q] :
                        correct_ans += 1 
                    else : 
                        wrong_ans += 1
                    break
                else :
                    print("try using :\nA , B , C , D")

        else :

            while True :
                ans = input(f"{q} \nEnter your choice (T/F) : ").upper()
                if ans == "T" or ans == "F" :
                    if ans == d2[q] :
                        correct_ans += 1 
                    else : 
                        wrong_ans += 1
                    break
                else :
                    print("try using :\nT , F")

    percentage = (correct_ans/total_questions)*100
    print(f"RESULT - \nCORRECT ANS = {correct_ans}\nWORONG ANS = {wrong_ans}")
    print(f"PERCENTAGE = {round(percentage,2)}% ")

subject = int(input("ENTER :\n1. FOR ENGLISH\n2. FOR MATH\n3. FOR CS \nEnter your choice : "))

if subject in (1,2,3,4,5) :
    if subject == 1 :
        chapter = int(input("USE :\n1. The Portrait of a Lady \n 2. ...\nEnter the chapter you want to test : "))
        if chapter == 1 :
            TF_Q = true_false_cs_ch1
            MCQ_options = cs_ch1_mcq_options
            MCQ_answers = cs_ch1_mcq_answers

        if chapter == 2 :
            TF_Q = true_false_cs_ch2
            MCQ_options = cs_ch2_mcq_options
            MCQ_answers = cs_ch2_mcq_answers  #Replace cs with eng.

        if chapter == 3 :
            TF_Q = true_false_cs_ch3
            MCQ_options = cs_ch3_mcq_options
            MCQ_answers = cs_ch3_mcq_answers

        if chapter == 4 :
            TF_Q = true_false_cs_ch4
            MCQ_options = cs_ch4_mcq_options
            MCQ_answers = cs_ch4_mcq_answers

        if chapter == 5 :
            TF_Q = true_false_cs_ch5
            MCQ_options = cs_ch5_mcq_options
            MCQ_answers = cs_ch5_mcq_answers

        if chapter == 6 :
            TF_Q = true_false_cs_ch6
            MCQ_options = cs_ch6_mcq_options
            MCQ_answers = cs_ch6_mcq_answers

        if chapter == 7 :
            TF_Q = true_false_cs_ch7
            MCQ_options = cs_ch7_mcq_options
            MCQ_answers = cs_ch7_mcq_answers

        if chapter == 8 :
            TF_Q = true_false_cs_ch8
            MCQ_options = cs_ch8_mcq_options
            MCQ_answers = cs_ch8_mcq_answers

        if chapter == 9 :
            TF_Q = true_false_cs_ch9
            MCQ_options = cs_ch9_mcq_options
            MCQ_answers = cs_ch9_mcq_answers

        if chapter == 10 :
            TF_Q = true_false_cs_ch10
            MCQ_options = cs_ch10_mcq_options
            MCQ_answers = cs_ch10_mcq_answers

        if chapter == 11 :
            TF_Q = true_false_cs_ch11
            MCQ_options = cs_ch11_mcq_options
            MCQ_answers = cs_ch11_mcq_answers

        if chapter == 12 :
            TF_Q = true_false_cs_ch12
            MCQ_options = cs_ch12_mcq_options
            MCQ_answers = cs_ch12_mcq_answers

        if chapter == 13 :
            TF_Q = true_false_cs_ch13
            MCQ_options = cs_ch13_mcq_options
            MCQ_answers = cs_ch13_mcq_answers

        if chapter == 14 :
            TF_Q = true_false_cs_ch14
            MCQ_options = cs_ch14_mcq_options
            MCQ_answers = cs_ch14_mcq_answers

        if chapter == 15 :
            TF_Q = true_false_cs_ch15
            MCQ_options = cs_ch15_mcq_options
            MCQ_answers = cs_ch15_mcq_answers

        if chapter == 16 :
            TF_Q = true_false_cs_ch16
            MCQ_options = cs_ch16_mcq_options
            MCQ_answers = cs_ch16_mcq_answers

        if chapter == 17 :
            TF_Q = true_false_cs_ch17
            MCQ_options = cs_ch17_mcq_options
            MCQ_answers = cs_ch17_mcq_answers

    
    if subject == 3 :
        chapter = int(input("USE :\nEnter the chapter : "))
        if chapter == 1 :
            TF_Q = true_false_cs_ch1
            MCQ_options = cs_ch1_mcq_options
            MCQ_answers = cs_ch1_mcq_answers

        if chapter == 2 :
            TF_Q = true_false_cs_ch2
            MCQ_options = cs_ch2_mcq_options
            MCQ_answers = cs_ch2_mcq_answers

        if chapter == 3 :
            TF_Q = true_false_cs_ch3
            MCQ_options = cs_ch3_mcq_options
            MCQ_answers = cs_ch3_mcq_answers

        if chapter == 4 :
            TF_Q = true_false_cs_ch4
            MCQ_options = cs_ch4_mcq_options
            MCQ_answers = cs_ch4_mcq_answers

        if chapter == 5 :
            TF_Q = true_false_cs_ch5
            MCQ_options = cs_ch5_mcq_options
            MCQ_answers = cs_ch5_mcq_answers

        if chapter == 6 :
            TF_Q = true_false_cs_ch6
            MCQ_options = cs_ch6_mcq_options
            MCQ_answers = cs_ch6_mcq_answers

        if chapter == 7 :
            TF_Q = true_false_cs_ch7
            MCQ_options = cs_ch7_mcq_options
            MCQ_answers = cs_ch7_mcq_answers

        if chapter == 8 :
            TF_Q = true_false_cs_ch8
            MCQ_options = cs_ch8_mcq_options
            MCQ_answers = cs_ch8_mcq_answers

        if chapter == 9 :
            TF_Q = true_false_cs_ch9
            MCQ_options = cs_ch9_mcq_options
            MCQ_answers = cs_ch9_mcq_answers

        if chapter == 10 :
            TF_Q = true_false_cs_ch10
            MCQ_options = cs_ch10_mcq_options
            MCQ_answers = cs_ch10_mcq_answers

        if chapter == 11 :
            TF_Q = true_false_cs_ch11
            MCQ_options = cs_ch11_mcq_options
            MCQ_answers = cs_ch11_mcq_answers

        if chapter == 12 :
            TF_Q = true_false_cs_ch12
            MCQ_options = cs_ch12_mcq_options
            MCQ_answers = cs_ch12_mcq_answers

        if chapter == 13 :
            TF_Q = true_false_cs_ch13
            MCQ_options = cs_ch13_mcq_options
            MCQ_answers = cs_ch13_mcq_answers

        if chapter == 14 :
            TF_Q = true_false_cs_ch14
            MCQ_options = cs_ch14_mcq_options
            MCQ_answers = cs_ch14_mcq_answers

        if chapter == 15 :
            TF_Q = true_false_cs_ch15
            MCQ_options = cs_ch15_mcq_options
            MCQ_answers = cs_ch15_mcq_answers

        if chapter == 16 :
            TF_Q = true_false_cs_ch16
            MCQ_options = cs_ch16_mcq_options
            MCQ_answers = cs_ch16_mcq_answers

        if chapter == 17 :
            TF_Q = true_false_cs_ch17
            MCQ_options = cs_ch17_mcq_options
            MCQ_answers = cs_ch17_mcq_answers

else :
    print("TRY USING : 1,2,3,4,5.")

question(d1=MCQ_answers,d2=TF_Q,d3=MCQ_options)