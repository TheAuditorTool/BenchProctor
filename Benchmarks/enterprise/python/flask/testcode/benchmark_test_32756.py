# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest32756():
    user_id = request.args.get('id', '')
    data = (lambda v: v.strip())(user_id)
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
