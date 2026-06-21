# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest51032():
    raw_body = request.get_data(as_text=True)
    data = str(raw_body).replace('\x00', '')
    return str(data), 200, {'Content-Type': 'text/html'}
