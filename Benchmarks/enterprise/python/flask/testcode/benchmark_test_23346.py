# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest23346():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = ' '.join(str(forwarded_ip).split())
    return str(data), 200, {'Content-Type': 'text/html'}
