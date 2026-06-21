# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest19529():
    cookie_value = request.cookies.get('session_token', '')
    pending = list(str(cookie_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    return str(data), 200, {'Content-Type': 'text/html'}
