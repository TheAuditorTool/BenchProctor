# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest72452():
    origin_value = request.headers.get('Origin', '')
    kind = 'json' if str(origin_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = origin_value
            data = parsed
        case _:
            data = origin_value
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
