# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest32043():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
