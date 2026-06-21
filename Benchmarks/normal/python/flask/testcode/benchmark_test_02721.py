# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest02721():
    field_value = request.form.get('field', '')
    data = field_value if field_value else 'default'
    return str(data), 200, {'Content-Type': 'text/html'}
