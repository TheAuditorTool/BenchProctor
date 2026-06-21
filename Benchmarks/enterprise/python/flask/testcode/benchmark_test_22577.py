# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest22577():
    field_value = request.form.get('field', '')
    with open('/var/app/data/' + str(field_value), 'r') as fh:
        content = fh.read()
    return content
