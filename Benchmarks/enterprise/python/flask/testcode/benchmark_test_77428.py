# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest77428():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
