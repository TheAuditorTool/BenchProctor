# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest43519():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = f'{forwarded_ip}'
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
