# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest53933():
    header_value = request.headers.get('X-Custom-Header', '')
    data = ' '.join(str(header_value).split())
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
