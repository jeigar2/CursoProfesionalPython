from datetime import datetime

def exection_time(func):
    def wrapper():
        inital_time = datetime.now()
        func()
        final_time = datetime.now()
        time_elapsed = final_time - inital_time
        print ("Han pasado " + str(time_elapsed.total_seconds()) + " segundos")
    return wrapper 

@exection_time
def random_func():
    for i in range (1, 100000):
        pass

def run():
    random_func()


if __name__ == "__main__":
    run()
