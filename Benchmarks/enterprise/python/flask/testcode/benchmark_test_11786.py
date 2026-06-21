# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest11786():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
