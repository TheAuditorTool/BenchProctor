# SPDX-License-Identifier: Apache-2.0
from flask import request


def to_text(value):
    return str(value).strip()

def BenchmarkTest56840():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = to_text(forwarded_ip)
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
