# SPDX-License-Identifier: Apache-2.0
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest70606():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    reader = make_reader(db_value)
    data = reader()
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
