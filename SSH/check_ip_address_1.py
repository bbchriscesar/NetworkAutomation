from fabric import Connection

host = "192.168.1.10"
username = "Christianne Cesar"
password = "181818"

try:
    c = Connection(host, user=username, connect_kwargs={"password": password})
    result = c.run("dir")
    print(result.stdout)
except Exception as e:
    print(f"An error occurred: {e}")
