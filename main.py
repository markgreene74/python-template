# imports
import datetime as dt
import helpers.helpers_main as hlp_m

# global vars

# main function goes here
def main() -> dt.datetime:
    _now = hlp_m.get_timestamp()
    print(f"The current datetime is: {_now}")

    # just return the timestamp for now, so we have something
    # to test
    return _now


if __name__ == '__main__':
    print("Executing the main function ...")
    main()
