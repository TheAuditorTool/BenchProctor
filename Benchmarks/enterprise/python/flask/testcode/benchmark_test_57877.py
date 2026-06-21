# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest57877():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % (origin_value,)
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
