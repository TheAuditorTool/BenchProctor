# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest00131():
    header_value = request.headers.get('X-Custom-Header', '')
    kind = 'json' if str(header_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = header_value
            data = parsed
        case _:
            data = header_value
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
