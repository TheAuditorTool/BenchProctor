# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest37810():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header:.200s}'
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
