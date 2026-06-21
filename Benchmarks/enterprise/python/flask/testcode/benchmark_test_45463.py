# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest45463():
    referer_value = request.headers.get('Referer', '')
    data = f'{referer_value}'
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
