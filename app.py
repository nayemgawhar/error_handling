import error_message

def my_cal(a,b):
    try:
        c = a/b
        print(c)
    except Exception as e:
        error_message.error_message(e.__class__.__name__)
    finally:
        print('This is finally block.')

my_cal(5,'2')