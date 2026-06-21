# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest16716():
    cookie_value = request.cookies.get('session_token', '')
    data = '{}'.format(cookie_value)
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
