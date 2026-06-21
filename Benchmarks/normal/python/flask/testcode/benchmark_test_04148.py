# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest04148():
    user_id = request.args.get('id', '')
    data = f'{user_id}'
    return str(data), 200, {'Content-Type': 'text/html'}
