# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest27522():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data, _sep, _rest = str(forwarded_ip).partition('\x00')
    return str(data), 200, {'Content-Type': 'text/html'}
