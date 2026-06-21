# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest67319():
    field_value = request.form.get('field', '')
    data = str(field_value).replace('\x00', '')
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
