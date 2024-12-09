
#Exercise 9: Simple Quiz Game


def main():
    
    user_score = 0
    
    # First question
    print("Question 1: Which force is the primary force that maintains the motion of the planets around the sun?")
    print("A. Friction")
    print("B. Gravitational force")
    print("C. Electromagnetic force")
    answer_1 = str(input("Enter your answer(multiple): ").strip().upper())
    #Check the answer and give the score, for all the selections if corret + 20, if not - 10
    for i in answer_1:
        if i == "B":
            user_score += 20
        else:
            user_score -= 10
    print("Answer is B. Gravitational force, now your scoere is: " + str(user_score) + "\n\n")
            
    # Second question
    print("Question 2: At the end of a star's life, what structure might it form?")
    print("A. Black hole")
    print("B. White dwarf star")
    print("C. Neutron star ")
    answer_2 = str(input("Enter your answer(multiple): ").strip().upper())
    #Check the answer and give the score, for all the slections if correct + 20, if lose answer - 10
    for i in answer_2:
        if i == "A" or i == "B" or i == "C":
            user_score += 20
    if len(answer_2) != 3:
        user_score -= (3 - len(answer_2)) * 10
    print("Answer is A, B, C, now your scoere is: " + str(user_score) + "\n\n")
        
    # Third question
    print("Question 3: Which planets are called ‘Earth-like planets’?")
    print("A. Mars")
    print("B. Jupiter")
    print("C. Venus")
    answer_3 = str(input("Enter your answer(multiple): ").strip().upper())
    #Check the answer and give the score, for all the slections if correct + 20, if lose answer - 10，if not correct -10
    for i in answer_3:
        if i == "A" or i == "C":
            user_score += 20
        else:
            user_score -= 10
    if len(answer_2) < 2:
        user_score -= 10
    print("Answer is A, C, now your scoere is: " + str(user_score) + "\n\n")
    
        
    print("Your final score is: " + str(user_score))
        

if __name__ == "__main__":
    main()
            
        
                
            
        