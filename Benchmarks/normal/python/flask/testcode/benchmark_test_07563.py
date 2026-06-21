# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest07563():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    return str(forwarded_ip), 200, {'Content-Type': 'text/html'}
