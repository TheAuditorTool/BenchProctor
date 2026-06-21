# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest16388():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '{}'.format(header_value)
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
