# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest19540():
    user_id = request.args.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    return str(data), 200, {'Content-Type': 'text/html'}
