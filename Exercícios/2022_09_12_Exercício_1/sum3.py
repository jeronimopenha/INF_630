import time
import traceback

def sum3_brute(vec):
    start = time.time_ns()
    sum3 = []
    end = time.time_ns()
    return sum3, end - start
    

def sum3_bisect():
    start = time.time_ns()
    sum3 = []
    end = time.time_ns()
    return sum3, end - start

def sum3_optimized():
    start = time.time_ns()
    sum3 = []
    end = time.time_ns()
    return sum3, end - start

def main():
    pass


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
        traceback.print_exc()
