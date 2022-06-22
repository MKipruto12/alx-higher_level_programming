#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div_result = a / b
    except:
        div_result = None
    finally:
        print("inside result: {}".format(div_result))
    return (div_result)
