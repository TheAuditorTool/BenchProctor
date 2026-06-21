# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest01954():
    referer_value = request.headers.get('Referer', '')
    return '<!-- diagnostic build token: ' + str(referer_value) + ' -->', 200, {'Content-Type': 'text/html'}
