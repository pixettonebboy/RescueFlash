# stop_server.py
import os
import signal
import subprocess

def kill_python_http_server():
    try:
        output = subprocess.check_output("tasklist", shell=True).decode()
        for line in output.splitlines():
            if "python.exe" in line.lower() or "py.exe" in line.lower():
                pid = int(line.split()[1])
                os.kill(pid, signal.SIGTERM)
                print(f"🔴 Killed Python server with PID {pid}")
                return
        print("❌ No Python HTTP server found.")
    except Exception as e:
        print("⚠️ Error:", e)

kill_python_http_server()
