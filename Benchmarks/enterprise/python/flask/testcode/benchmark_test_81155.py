# SPDX-License-Identifier: Apache-2.0
from flask import request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest81155():
    user_id = request.args.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    return str(data), 200, {'Content-Type': 'text/html'}
