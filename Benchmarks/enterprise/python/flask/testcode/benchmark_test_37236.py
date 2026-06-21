# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest37236():
    host_value = request.headers.get('Host', '')
    kind = 'json' if str(host_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = host_value
            data = parsed
        case _:
            data = host_value
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
