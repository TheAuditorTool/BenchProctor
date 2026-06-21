# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest69702():
    ua_value = request.headers.get('User-Agent', '')
    return '<!-- diagnostic build token: ' + str(ua_value) + ' -->', 200, {'Content-Type': 'text/html'}
