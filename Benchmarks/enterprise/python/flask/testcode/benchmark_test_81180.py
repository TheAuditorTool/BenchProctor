# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest81180():
    raw_body = request.get_data(as_text=True)
    pending = list(str(raw_body).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
