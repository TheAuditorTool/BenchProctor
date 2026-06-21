# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest63802():
    referer_value = request.headers.get('Referer', '')
    data = ' '.join(str(referer_value).split())
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
