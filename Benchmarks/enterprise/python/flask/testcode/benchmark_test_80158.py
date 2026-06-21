# SPDX-License-Identifier: Apache-2.0
from flask import request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest80158():
    host_value = request.headers.get('Host', '')
    reader = make_reader(host_value)
    data = reader()
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
