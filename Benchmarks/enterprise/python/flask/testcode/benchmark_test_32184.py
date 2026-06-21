# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest32184():
    cookie_value = request.cookies.get('session_token', '')
    kind = 'json' if str(cookie_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = cookie_value
            data = parsed
        case _:
            data = cookie_value
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
