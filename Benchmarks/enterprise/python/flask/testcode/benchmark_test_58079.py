# SPDX-License-Identifier: Apache-2.0
from app_runtime import db


def BenchmarkTest58079():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(db_value)
    data = collected
    processed = data[:64]
    with open('/var/app/data/' + str(processed), 'r') as fh:
        content = fh.read()
    return content
