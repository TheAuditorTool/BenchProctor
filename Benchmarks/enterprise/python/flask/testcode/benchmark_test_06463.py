# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest06463():
    field_value = request.form.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
