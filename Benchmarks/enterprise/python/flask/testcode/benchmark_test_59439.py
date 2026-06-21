# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest59439():
    header_value = request.headers.get('X-Custom-Header', '')
    pending = list(str(header_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    return str(data), 200, {'Content-Type': 'text/html'}
