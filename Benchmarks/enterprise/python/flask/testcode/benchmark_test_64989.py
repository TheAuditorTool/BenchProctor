# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest64989():
    auth_header = request.headers.get('Authorization', '')
    data = '{}'.format(auth_header)
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
