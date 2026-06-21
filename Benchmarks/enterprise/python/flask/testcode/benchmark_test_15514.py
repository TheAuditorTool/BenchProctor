# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest15514():
    origin_value = request.headers.get('Origin', '')
    data = f'{origin_value:.200s}'
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
