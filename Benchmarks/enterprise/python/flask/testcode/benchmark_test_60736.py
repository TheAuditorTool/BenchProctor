# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest60736():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data, _sep, _rest = str(forwarded_ip).partition('\x00')
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
