from fabric import Connection, ThreadingGroup
import pytest


@pytest.mark.parametrize("host, username, password", [
    ("192.168.1.10", "Christianne Cesar", "181818"),
    ("192.168.1.10", "Christianne Cesar", "181818")
    # add more host, username, password tuples here
])
def test_connection(host, username, password):
    try:
        c = Connection(host, user=username, connect_kwargs={"password": password})
        result = c.run("dir")
        print(result.stdout)
    except Exception as e:
        print(f"An error occurred: {e}")


def parallel_test_connection(hosts, usernames, passwords):
    group = ThreadingGroup(*hosts, user=usernames, connect_kwargs={"password": passwords})
    results = group.run("dir")
    for connection, result in results.items():
        print(f"{connection.host}: {result.stdout}")


