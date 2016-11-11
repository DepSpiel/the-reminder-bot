"""
@author Tyler Lambert
This file is the start script. It initializes the database and the main
function in parallel. It contains a SIGINT (ctrl+c) handler that will
gracefully kill the two processes and stop the database.
"""


import subprocess, signal, sys


def signal_handler(signal, frame):
    database_p.kill()
    main_p.kill()
    subprocess.run(["sudo", "service", "mysql", "stop"])
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
subprocess.run(["sudo", "service", "mysql", "start"])
database_p = subprocess.Popen(["python3", "database.py"])
main_p = subprocess.Popen(["python3", "main.py"])