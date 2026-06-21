# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest03972():
    cookie_value = request.cookies.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
