# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest03102():
    user_id = request.args.get('id', '')
    kind = 'json' if str(user_id).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = user_id
            data = parsed
        case _:
            data = user_id
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
