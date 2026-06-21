# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest15691():
    origin_value = request.headers.get('Origin', '')
    data = origin_value if origin_value else 'default'
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
