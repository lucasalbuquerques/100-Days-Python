def score_test(score):
    score = score + 1
    print(f"teste {score}")
    return score

score = 10
print(score)

score = score_test(score)
score = score_test(score)
print(score)
