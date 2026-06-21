# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest01558():
    auth_header = request.headers.get('Authorization', '')
    kind = 'json' if str(auth_header).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = auth_header
            data = parsed
        case _:
            data = auth_header
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
