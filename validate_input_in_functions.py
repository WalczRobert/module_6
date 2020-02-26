"""
Robert Walczak
Takes in user input for test name and test score
:param name_test - the name of the test
:param score_test - the score of the test
:return op_test - Name of the test and the score
"""



def score_test_average(name_test, score_test, invalid_message):
    #print(type(score_test))
    try:
        score_test = int(score_test)
    except ValueError:
        print(invalid_message)
    if score_test >= 0 and score_test < 100:
        op_test = name_test,score_test
        return op_test
    elif score_test < 0 or score_test > 100:
        op_test = name_test,invalid_message
        return op_test



if __name__ == '__main__':
    print('Name of test: ')
    name_test = input()

    print('test score: ')
    score_test = input()
    score_test = int(score_test)

    invalid_message = 'Invalid test score, try again!'
    #print (type(score_test))
    print(score_test_average(name_test, score_test, invalid_message))