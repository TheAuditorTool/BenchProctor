# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest41821():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
