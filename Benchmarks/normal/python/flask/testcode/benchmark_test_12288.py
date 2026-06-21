# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest12288():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
