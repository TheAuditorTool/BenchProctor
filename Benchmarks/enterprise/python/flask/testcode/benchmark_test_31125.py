# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest31125():
    field_value = request.form.get('field', '')
    data = field_value if field_value else 'default'
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
