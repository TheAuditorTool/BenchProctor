# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest10590():
    referer_value = request.headers.get('Referer', '')
    normalized = unicodedata.normalize('NFKC', str(referer_value))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
