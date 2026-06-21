# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest11985():
    host_value = request.headers.get('Host', '')
    return str(host_value), 200, {'Content-Type': 'text/html'}
