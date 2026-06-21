# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest10672():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header:.200s}'
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
