# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest79117():
    field_value = request.form.get('field', '')
    prefix = ''
    data = prefix + str(field_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
