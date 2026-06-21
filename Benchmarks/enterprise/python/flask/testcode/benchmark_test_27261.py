# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest27261():
    user_id = request.args.get('id', '')
    data = '%s' % str(user_id)
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
