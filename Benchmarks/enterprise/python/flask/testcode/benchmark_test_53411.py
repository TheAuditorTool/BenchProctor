# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest53411():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = '%s' % (forwarded_ip,)
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
