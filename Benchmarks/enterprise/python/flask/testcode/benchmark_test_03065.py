# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest03065():
    host_value = request.headers.get('Host', '')
    data = ' '.join(str(host_value).split())
    return str(data), 200, {'Content-Type': 'text/html'}
