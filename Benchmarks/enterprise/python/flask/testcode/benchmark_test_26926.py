# SPDX-License-Identifier: Apache-2.0
from flask import request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest26926():
    ua_value = request.headers.get('User-Agent', '')
    reader = make_reader(ua_value)
    data = reader()
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
