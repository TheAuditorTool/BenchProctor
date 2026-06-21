# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest02174():
    host_value = request.headers.get('Host', '')
    if host_value:
        data = host_value
    else:
        data = ''
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
