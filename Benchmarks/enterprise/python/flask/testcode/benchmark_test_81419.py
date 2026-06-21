# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest81419():
    field_value = request.form.get('field', '')
    parts = str(field_value).split(',')
    data = ','.join(parts)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
