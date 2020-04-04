"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random

def main():
    score = float(input("Enter score: "))
    result = check_score(score)
    print(result)
    randscore = random.randint(0, 100)
    randresult = check_score(randscore)
    print("Random score : ", randscore)
    print(randresult)

def check_score(score):
    if score < 0 or score > 100:
        output = "Invalid score"
    elif score >= 90:
        output = "Excellent"
    elif score >= 50:
        output = "Passable"
    elif score < 50:
        output = "Bad"
    return output


if __name__ == '__main__':
    main()




