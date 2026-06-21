# SPDX-License-Identifier: Apache-2.0
from flask import request


def relay_value(value):
    return value

def BenchmarkTest07060():
    multipart_value = request.form.get('multipart_field', '')
    data = relay_value(multipart_value)
    return str(data), 200, {'Content-Type': 'text/html'}
