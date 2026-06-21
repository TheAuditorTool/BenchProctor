# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest08866():
    field_value = request.form.get('field', '')
    data = '%s' % (field_value,)
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
