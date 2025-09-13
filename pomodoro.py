import time
import argparse


def countdown(label: str, seconds: int) -> None:
    """Countdown timer that prints remaining time."""
    for remaining in range(seconds, 0, -1):
        mins, secs = divmod(remaining, 60)
        print(f"{label}: {mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
    print(f"{label} complete!           ")


def pomodoro(work: int, short_break: int, long_break: int, cycles: int) -> None:
    """Run the Pomodoro timer."""
    for cycle in range(1, cycles + 1):
        countdown(f"Work {cycle}/{cycles}", work)
        if cycle < cycles:
            countdown(f"Short Break {cycle}", short_break)
    countdown("Long Break", long_break)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Pomodoro timer.")
    parser.add_argument("--work", type=int, default=25, help="Work duration in minutes (default: 25)")
    parser.add_argument("--short-break", type=int, default=5, help="Short break duration in minutes (default: 5)")
    parser.add_argument("--long-break", type=int, default=15, help="Long break duration in minutes (default: 15)")
    parser.add_argument("--cycles", type=int, default=4, help="Number of Pomodoro cycles before long break (default: 4)")
    args = parser.parse_args()

    work_seconds = args.work * 60
    short_break_seconds = args.short_break * 60
    long_break_seconds = args.long_break * 60

    pomodoro(work_seconds, short_break_seconds, long_break_seconds, args.cycles)
