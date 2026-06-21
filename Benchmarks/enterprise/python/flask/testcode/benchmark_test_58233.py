# SPDX-License-Identifier: Apache-2.0
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest58233():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    with open('/var/app/data/' + str(processed), 'r') as fh:
        content = fh.read()
    return content
