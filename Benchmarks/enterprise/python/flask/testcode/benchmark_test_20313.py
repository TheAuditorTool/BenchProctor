# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest20313():
    host_value = request.headers.get('Host', '')
    prefix = ''
    data = prefix + str(host_value)
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
