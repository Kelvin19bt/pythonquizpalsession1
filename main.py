for each in range(1,101):
    if each % 3 == 0 and each % 5 == 0:
        print('fizzbuzz')
    elif each % 5 == 0:
        print('buzz')
    elif each % 3 == 0:
        print('fizz')
    else:print(each)

