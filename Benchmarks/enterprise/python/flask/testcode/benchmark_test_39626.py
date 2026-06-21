# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest39626():
    user_id = request.args.get('id', '')
    data = str(user_id).replace('\x00', '')
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
