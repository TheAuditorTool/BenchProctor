# SPDX-License-Identifier: Apache-2.0
from flask import request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest60649():
    host_value = request.headers.get('Host', '')
    reader = make_reader(host_value)
    data = reader()
    return str(data), 200, {'Content-Type': 'text/html'}
