import time
import json
from time import sleep
import os


def now():
    """Returns timestamp rounded down to seconds."""
    return int(time.time())


def min_sec(seconds):
    """Turns seconds into minutes and seconds.

    The return is a string with the format:
        minutes:seconds
    For example:
        12:17 = 12 minutes, 17 seconds"""
    minutes, seconds = divmod(seconds, 60)
    # Pads the seconds with a 0 if < 10
    seconds = str(seconds).zfill(2)
    min_sec_string = f"{minutes}:{seconds}"
    return min_sec_string


def set_and_start():
    """Sets the start time to now and starts the timer."""
    start_time = now()
    with open("timer.json", "w") as timer_settings_file:
        json.dump(start_time, timer_settings_file)
    continue_timer(start_time)


def continue_timer(start_time=None):
    """Continues the timer from where it should be.

    This means that the timer continues as if it had
    never stopped, skipping the time that it was not
    running."""
    if not start_time:
        with open("timer.json") as timer_settings_file:
            start_time = json.load(timer_settings_file)
    last_time = now()
    while True:
        current_time = now()
        if current_time != last_time:
            with open("timer.txt", "w") as timer_file:
                timer_string = min_sec(current_time - start_time)
                timer_file.write(timer_string)
                last_time = current_time


def clear():
    """Clears the terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')


def add_remove_time():
    """Adds or removes time from the timer.

    The unit of time is seconds."""
    clear()
    print()
    choice = None
    options = ["1", "2", "q"]
    options_str = "What do you want to do?\n"\
                  "\t1. Add time\n"\
                  "\t2. Remove time\n"\
                  "\tq. Go back\n\n\t\t"
    while True:
        choice = input(options_str)
        if choice not in options:
            print("\n\tPlease choose one of the available",
                  "options: 1, 2, q.\n")
            continue
        elif choice == "1":
            seconds = None
            while not seconds:
                try:
                    input_str = "How many seconds do you want to add?"
                    seconds = -int(input(f"\n\t{input_str} "))
                except Exception:
                    print("Please enter a valid number of seconds.\n")
        elif choice == "2":
            seconds = None
            while not seconds:
                try:
                    input_str = "How many seconds do you want to remove?"
                    seconds = int(input(f"\n\t{input_str} "))
                except Exception:
                    print("Please enter a valid number of seconds.\n")
        else:
            print("\nReturning to main menu...")
            sleep(1)
            break
        with open("timer.json") as timer_settings_file:
            start_time = json.load(timer_settings_file)
        start_time += seconds
        with open("timer.json", "w") as timer_settings_file:
            json.dump(start_time, timer_settings_file)
        print("\n\tTimer has been adjusted, returning to main menu...")
        sleep(1)
        break


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
                  "\tq. Quit\n\n\t\t"
    clear()
    print()
    while True:
        choice = input(options_str)
        if choice not in options:
            print("\n\tPlease choose one of the available",
                  "options: 1, 2, 3, q.\n")
            continue
        elif choice == "1":
            print("\nStarting timer at 0...")
            set_and_start()
        elif choice == "2":
            print("\nContinuing timer...")
            continue_timer()
        elif choice == "3":
            print("\nChanging timer...\n\n")
            sleep(1)
            add_remove_time()
        else:
            print("\nQuitting...")
            break


def main():
    menu()


if __name__ == "__main__":
    main()
