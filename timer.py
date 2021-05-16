import time
# import json


def now():
    """Returns timestamp rounded to seconds."""
    return int(time.time())


def min_sec(seconds):
    """Turns seconds into minutes and seconds."""
    minutes, seconds = divmod(seconds, 60)
    return minutes, seconds


def set_and_start():
    """Sets the start time to now and starts the timer."""
    pass


def continue_timer():
    """Continues the timer from where it should be.

    This means that the timer continues as if it had
    never stopped, skipping the time that it was not
    running."""
    pass


def add_remove_time():
    """Adds or removes time from the timer.

    The unit of time is seconds."""
    pass


def menu():
    """Asks the user what to do.

    The four options are:
     1. Set start to now and start timer
     2. Continue timer
     3. Add or remove time
     q. Quit
    These options then get executed.
    """
    choice = None
    options = ["1", "2", "3", "q"]
    options_str = "What do you want to do?\n"\
                  "\t1. Set timer to 0 and start\n"\
                  "\t2. Continue timer\n"\
                  "\t3. Add or remove time\n"\
                  "\tq. Quit\n\n\t"
    while True:
        choice = input(options_str)
        if choice not in options:
            print("\n\tPlease choose one of the available",
                  "options: 1, 2, 3, q.\n")
            continue
        elif choice == "1":
            set_and_start()
        elif choice == "2":
            continue_timer()
        elif choice == "3":
            add_remove_time()
        else:
            break


def main():
    menu()


if __name__ == "__main__":
    main()
