# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest65850():
    field_value = request.form.get('field', '')
    data = field_value if field_value else 'default'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
