# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest12040():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    kind = 'json' if str(forwarded_ip).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = forwarded_ip
            data = parsed
        case _:
            data = forwarded_ip
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
