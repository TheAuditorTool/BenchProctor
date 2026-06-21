# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest07761():
    origin_value = request.headers.get('Origin', '')
    kind = 'json' if str(origin_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = origin_value
            data = parsed
        case _:
            data = origin_value
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
