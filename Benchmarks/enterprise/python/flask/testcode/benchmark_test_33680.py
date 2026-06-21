# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest33680():
    host_value = request.headers.get('Host', '')
    pending = list(str(host_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    return str(data), 200, {'Content-Type': 'text/html'}
