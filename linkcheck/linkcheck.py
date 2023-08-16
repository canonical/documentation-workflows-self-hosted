import subprocess

def run_command(command):
    subprocess.run(command, check=True, shell=True)

try:
    # Install the doc framework and run link checker
    run_command('make install')
    run_command('make linkcheck')
except subprocess.CalledProcessError as e:
    print(f"Command '{e.cmd}' returned non-zero exit status {e.returncode}.")
    exit(1)