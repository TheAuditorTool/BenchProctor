# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest60771():
    raw_body = request.get_data(as_text=True)
    data = (lambda v: v.strip())(raw_body)
    return str(data), 200, {'Content-Type': 'text/html'}
