# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest75946():
    field_value = request.form.get('field', '')
    data = f'{field_value}'
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
