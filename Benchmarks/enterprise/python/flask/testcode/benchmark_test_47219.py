# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest47219():
    host_value = request.headers.get('Host', '')
    data = f'{host_value:.200s}'
    return str(data), 200, {'Content-Type': 'text/html'}
