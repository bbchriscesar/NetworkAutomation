import paramiko

host = "10.10.20.48"
port = 22
username = "developer"
password = "C1sco12345"

try:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port, username, password)
    print("Successfully connected to the SSH server.")
except Exception as e:
    print(f"Failed to connect to the SSH server: {e}")
finally:
    client.close()
