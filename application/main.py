import datetime as dt

from rich import print as rp

import application.helpers.helpers_main as hlp_m

# variables


# main function goes here
def main() -> dt.datetime:
    _now = hlp_m.get_timestamp()
    rp(f"The current datetime is: [bold magenta]{_now}[/bold magenta]")

    # just return the timestamp for now, so we have something to test
    return _now


if __name__ == "__main__":
    print("Executing the main function ...")
    main()
