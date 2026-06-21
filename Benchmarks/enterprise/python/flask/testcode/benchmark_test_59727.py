# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest59727():
    cookie_value = request.cookies.get('session_token', '')
    data = (lambda v: v.strip())(cookie_value)
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
