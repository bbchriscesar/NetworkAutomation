import paramiko

host = "192.168.1.10"
port = 22
username = "Christianne Cesar"
password = "181818"

try:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port, username, password)

    stdin, stdout, stderr = client.exec_command("dir")
    output = stdout.read().decode()
    print(output)
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    client.close()
