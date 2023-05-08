# This script install marvin service and starts it

import os
from dotenv import load_dotenv
from subprocess import Popen, PIPE


def sudo_cmd(cmd):
    proc = Popen(f"sudo {cmd}".split(),
                 stdin=PIPE, stdout=PIPE, stderr=PIPE,
                 universal_newlines=True)
    proc.stdin.write('password\n')
    proc.stdin.flush()

    counter = 1
    for line in proc.stdout:
        print('{:02d}: {}'.format(counter, line), end='')
        counter += 1


cwd = os.getcwd()
marvin_py_path = "/usr/local/bin/marvin"
marvin_service_path = "/etc/systemd/system/marvin.service"

# Copy src to bin path
sudo_cmd(f"cp -TR {cwd}/src/ {marvin_py_path}")

# Copy and modify service file
load_dotenv()
user = os.getlogin()
replaces = {"<user>": user, "<group>": user,
            "<MARVIN_TOKEN>": os.getenv('MARVIN_TOKEN'),
            "<OPENAI_API_KEY>": os.getenv('OPENAI_API_KEY')}

with open(f"{cwd}/marvin.service", 'r') as file:
    data = file.read()
    for replace_word in replaces:
        data = data.replace(replace_word, replaces[replace_word])

with open(f"{cwd}/tmp_marvin.service", 'w') as file:
    file.write(data)

sudo_cmd(f"mv -f {cwd}/tmp_marvin.service {marvin_service_path}")

# Enable and start the service
sudo_cmd("systemctl stop marvin.service")
sudo_cmd(f"chcon system_u:object_r:systemd_unit_file_t:s0 {marvin_service_path}")
sudo_cmd("systemctl daemon-reload")
sudo_cmd("systemctl enable marvin.service")
sudo_cmd("systemctl start marvin.service")
