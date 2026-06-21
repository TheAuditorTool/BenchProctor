# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest17755():
    multipart_value = request.form.get('multipart_field', '')
    kind = 'json' if str(multipart_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = multipart_value
            data = parsed
        case _:
            data = multipart_value
    return str(data), 200, {'Content-Type': 'text/html'}
