# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest36195():
    ua_value = request.headers.get('User-Agent', '')
    kind = 'json' if str(ua_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = ua_value
            data = parsed
        case _:
            data = ua_value
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
