import psutil
import curses

def display_processes(screen):
    # Set up screen and colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    screen.nodelay(1)

    while True:
        screen.clear()

        # Display header
        screen.addstr(0, 0, "PID".ljust(8) + "Name".ljust(25) + "CPU%".ljust(10) + "Memory%", curses.color_pair(1))

        # Fetch and display processes
        for idx, process in enumerate(psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent'])):
            screen.addstr(idx + 1, 0, str(process.info['pid']).ljust(8) + str(process.info['name']).ljust(25) +
                          str(process.info['cpu_percent']).ljust(10) + str(process.info['memory_percent']))

        screen.refresh()

        # Refresh every 2 seconds
        curses.napms(2000)

curses.wrapper(display_processes)
