# SPDX-License-Identifier: Apache-2.0
from flask import request


def relay_value(value):
    return value

def BenchmarkTest45382():
    ua_value = request.headers.get('User-Agent', '')
    data = relay_value(ua_value)
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
