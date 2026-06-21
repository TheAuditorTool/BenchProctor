# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest75566():
    referer_value = request.headers.get('Referer', '')
    kind = 'json' if str(referer_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = referer_value
            data = parsed
        case _:
            data = referer_value
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
