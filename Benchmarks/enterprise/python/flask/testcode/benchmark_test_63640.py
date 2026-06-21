# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest63640():
    field_value = request.form.get('field', '')
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
