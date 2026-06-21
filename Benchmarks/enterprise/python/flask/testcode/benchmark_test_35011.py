# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest35011():
    host_value = request.headers.get('Host', '')
    data = str(host_value).replace('\x00', '')
    return str(data), 200, {'Content-Type': 'text/html'}
