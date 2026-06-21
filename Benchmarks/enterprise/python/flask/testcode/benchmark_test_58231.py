# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest58231():
    referer_value = request.headers.get('Referer', '')
    data = (lambda v: v.strip())(referer_value)
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
