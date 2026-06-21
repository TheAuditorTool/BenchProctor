# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest40433():
    raw_body = request.get_data(as_text=True)
    return str(raw_body), 200, {'Content-Type': 'text/html'}
