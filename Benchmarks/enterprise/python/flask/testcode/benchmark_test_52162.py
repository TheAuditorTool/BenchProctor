# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest52162():
    user_id = request.args.get('id', '')
    data = '%s' % (user_id,)
    return str(data), 200, {'Content-Type': 'text/html'}
