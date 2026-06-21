# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest69769():
    field_value = request.form.get('field', '')
    kind = 'json' if str(field_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = field_value
            data = parsed
        case _:
            data = field_value
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
