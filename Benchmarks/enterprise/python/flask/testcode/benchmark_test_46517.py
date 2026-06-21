# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest46517():
    ua_value = request.headers.get('User-Agent', '')
    data = '{}'.format(ua_value)
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
