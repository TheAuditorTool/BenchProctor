# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest30444():
    user_id = request.args.get('id', '')
    data = user_id if user_id else 'default'
    return str(data), 200, {'Content-Type': 'text/html'}
