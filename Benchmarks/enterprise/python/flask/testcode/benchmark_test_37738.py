# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest37738():
    ua_value = request.headers.get('User-Agent', '')
    data = (lambda v: v.strip())(ua_value)
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
