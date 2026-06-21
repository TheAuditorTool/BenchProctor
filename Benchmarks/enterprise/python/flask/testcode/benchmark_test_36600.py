# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest36600():
    field_value = request.form.get('field', '')
    data = str(field_value).replace('\x00', '')
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
