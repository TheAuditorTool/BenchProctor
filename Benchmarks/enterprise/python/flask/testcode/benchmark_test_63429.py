# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest63429():
    origin_value = request.headers.get('Origin', '')
    return str(origin_value), 200, {'Content-Type': 'text/html'}
