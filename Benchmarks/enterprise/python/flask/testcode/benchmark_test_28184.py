# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest28184():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    pending = list(str(forwarded_ip).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
