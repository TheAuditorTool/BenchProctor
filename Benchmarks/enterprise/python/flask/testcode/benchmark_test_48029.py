# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest48029():
    referer_value = request.headers.get('Referer', '')
    pending = list(str(referer_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    return str(data), 200, {'Content-Type': 'text/html'}
