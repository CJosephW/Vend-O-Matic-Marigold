import subprocess, sys, time
server = subprocess.Popen([sys.executable, "main.py"])
time.sleep(1)
try:
    subprocess.check_call([sys.executable, "int_tests/integration.py"])
finally: 
    time.sleep(5)
    server.terminate()