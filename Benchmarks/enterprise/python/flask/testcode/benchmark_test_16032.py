# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest16032():
    cookie_value = request.cookies.get('session_token', '')
    data = str(cookie_value).replace('\x00', '')
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
