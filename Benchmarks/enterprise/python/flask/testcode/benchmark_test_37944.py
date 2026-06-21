# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest37944():
    ua_value = request.headers.get('User-Agent', '')
    data = '%s' % str(ua_value)
    return str(data), 200, {'Content-Type': 'text/html'}
