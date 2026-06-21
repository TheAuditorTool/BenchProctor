# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest07339():
    auth_header = request.headers.get('Authorization', '')
    data = (lambda v: v.strip())(auth_header)
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
