# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest68696():
    auth_header = request.headers.get('Authorization', '')
    kind = 'json' if str(auth_header).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = auth_header
            data = parsed
        case _:
            data = auth_header
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
