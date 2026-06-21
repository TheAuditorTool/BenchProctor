# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest19448():
    field_value = request.form.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    return str(data), 200, {'Content-Type': 'text/html'}
