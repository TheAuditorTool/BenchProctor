# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest76061():
    user_id = request.args.get('id', '')
    data = f'{user_id:.200s}'
    return str(data), 200, {'Content-Type': 'text/html'}
