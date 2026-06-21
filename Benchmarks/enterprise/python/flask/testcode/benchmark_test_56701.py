# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest56701():
    auth_header = request.headers.get('Authorization', '')
    data = (lambda v: v.strip())(auth_header)
    return str(data), 200, {'Content-Type': 'text/html'}
