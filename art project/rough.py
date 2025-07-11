# 50 MCQ + 50 TRUE FALSE PER CHAPTER.
# QUESTION PAPER WILL CONTAIN 50 QUESTIONS ONLY.
# USER CAN CHOSSE THE CHAPTERS HE WANTS.

from eng.eng_ch1 import eng_mcq_answers, eng_mcq_options, eng_tf
from cs.cs_ch1 import cs_mcq_answers, cs_mcq_options, cs_tf
import random

def question(d1,d2,d3) : #d1 = MCQ  ,d2 = TURE FALSE,d3 = OPTIONS OF MCQ

    l1 = list(d1.keys())
    random.shuffle(l1)

    l2 = list(d2.keys())
    random.shuffle(l2)

    i = 1
    correct_ans = 0
    wrong_ans = 0
    total_questions = len(l1) + len(l2)

    for mcq in l1 :
        while True :
            ans = input(f"{mcq} \n{d3[mcq]}\nEnter your choice (A/B/C/D) : ").upper()
            if ans == "A" or ans == "B" or ans == "C" or ans == "D" :
                if ans == d1[mcq] :
                    correct_ans += 1 
                else : 
                    wrong_ans += 1
                break
            else :
                print("try using :\nA , B , C , D")

    for t_f in l2 :
        while True :
            ans = input(f"{t_f} \nEnter your choice (T/F) : ").upper()
            if ans == "T" or ans == "F" :
                if ans == d2[t_f] :
                    correct_ans += 1 
                else : 
                    wrong_ans += 1
                break
            else :
                print("try using :\nT , F")

    percentage = (correct_ans/total_questions)*100
    print(f"RESULT - \nCORRECT ANS = {correct_ans}\nWORONG ANS = {wrong_ans}")
    print(f"PERCENTAGE = {round(percentage,2)}% ")

subject = int(input("ENTER :\n1. FOR ENGLISH\n2. FOR MATH\n3. FOR CS"))

if subject in (1,2,3,4,5) :
    if subject == 1 :
        chapter = int(input("USE :\n1. The Portrait of a Lady \n 2. ...\nEnter the chapter you want to test : "))
        TF_Q = getattr(true_false_eng_ch1,f"true_false_eng_ch{chapter}")
    if subject == 3 :
        chapter = int(input("USE :\n1. Computer Systems and Organisation \n 2. ...\nEnter the chapter you want to test : "))

else :
    print("TRY USING : 1,2,3,4,5.")