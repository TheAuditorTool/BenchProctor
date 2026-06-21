# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest17279():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % str(referer_value)
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
