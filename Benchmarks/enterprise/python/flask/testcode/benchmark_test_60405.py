# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest60405():
    raw_body = request.get_data(as_text=True)
    def normalize(value):
        return value.strip()
    data = normalize(raw_body)
    return str(data), 200, {'Content-Type': 'text/html'}
