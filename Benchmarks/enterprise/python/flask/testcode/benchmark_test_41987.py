# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest41987():
    raw_body = request.get_data(as_text=True)
    kind = 'json' if str(raw_body).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = raw_body
            data = parsed
        case _:
            data = raw_body
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
