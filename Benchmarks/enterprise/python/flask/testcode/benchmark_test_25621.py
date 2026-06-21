# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest25621():
    header_value = request.headers.get('X-Custom-Header', '')
    return '<!-- diagnostic build token: ' + str(header_value) + ' -->', 200, {'Content-Type': 'text/html'}
