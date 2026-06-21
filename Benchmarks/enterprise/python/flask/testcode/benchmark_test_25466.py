# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest25466():
    header_value = request.headers.get('X-Custom-Header', '')
    kind = 'json' if str(header_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = header_value
            data = parsed
        case _:
            data = header_value
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
