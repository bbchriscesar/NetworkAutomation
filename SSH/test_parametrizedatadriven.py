from fabric import Connection, ThreadingGroup
import pytest
import csv

data_file = '../data/test_data.csv'


def read_data():
    data = []
    with open(data_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    return data


@pytest.mark.parametrize("host, username, password", read_data())
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
