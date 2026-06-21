# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest27234():
    host_value = request.headers.get('Host', '')
    data = '{}'.format(host_value)
    return str(data), 200, {'Content-Type': 'text/html'}
