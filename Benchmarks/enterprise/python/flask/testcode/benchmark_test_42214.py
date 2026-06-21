# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest42214():
    auth_header = request.headers.get('Authorization', '')
    data = str(auth_header).replace('\x00', '')
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
