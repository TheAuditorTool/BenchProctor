# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest30722():
    header_value = request.headers.get('X-Custom-Header', '')
    normalized = unicodedata.normalize('NFKC', str(header_value))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
