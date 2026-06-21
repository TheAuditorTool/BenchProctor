# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest54750():
    referer_value = request.headers.get('Referer', '')
    data = ' '.join(str(referer_value).split())
    return str(data), 200, {'Content-Type': 'text/html'}
