# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest32735():
    user_id = request.args.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    return str(data), 200, {'Content-Type': 'text/html'}
