# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest73395():
    referer_value = request.headers.get('Referer', '')
    data = (lambda v: v.strip())(referer_value)
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
