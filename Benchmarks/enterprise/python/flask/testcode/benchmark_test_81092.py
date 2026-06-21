# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest81092():
    host_value = request.headers.get('Host', '')
    data = '{}'.format(host_value)
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
