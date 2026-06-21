# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest07713():
    user_id = request.args.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
