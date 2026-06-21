# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest42447():
    field_value = request.form.get('field', '')
    prefix = ''
    data = prefix + str(field_value)
    return str(data), 200, {'Content-Type': 'text/html'}
