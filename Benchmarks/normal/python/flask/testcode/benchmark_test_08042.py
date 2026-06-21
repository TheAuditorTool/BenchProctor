# SPDX-License-Identifier: Apache-2.0
import base64
from flask import request
import unicodedata


def BenchmarkTest08042():
    auth_header = request.headers.get('Authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
