# POTD 19 skel

import sys

def get_factors(n, m):
    """ Return a dictionary with the integers from 2 to N (inclusive) as keys.
    The value associated with a key k is a list of the positive integer factors
    (divisors) of that number, in ascending order.
    Precondition: N is an integer >= 2 """
    
    dic = {
            
            }
    
    nums = []
    answers = []
    
    if m == 0:
        for num in range(n, 1, -1):
            nums.append(num)
            
        for key in nums:
            dic[key] = ''
            
        for key in dic:
            for num in range(1, n + 1):
                ans = (key % num)
                if ans == 0:
                    answers.append(num)
            dic[key] = answers
            answers = []
        
        return dic
    else:
        for num in range(1, m + 1):
            ans = (m % num)
            if ans == 0:
                answers.append(num)
            dic[m] = answers

        return dic

    

if __name__ == "__main__":
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
    except:
        num1 = int(sys.argv[1])
        
    if len(sys.argv[1:]) > 1:
        print("more than one")
        print(get_factors(num1, num2))
    else:
        print("only one")
        print(get_factors(num1, 0))
        