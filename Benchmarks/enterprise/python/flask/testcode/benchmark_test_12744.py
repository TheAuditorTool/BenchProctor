# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest12744():
    referer_value = request.headers.get('Referer', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    return str(data), 200, {'Content-Type': 'text/html'}
