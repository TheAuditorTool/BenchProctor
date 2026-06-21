# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest42179():
    host_value = request.headers.get('Host', '')
    data = f'{host_value:.200s}'
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
