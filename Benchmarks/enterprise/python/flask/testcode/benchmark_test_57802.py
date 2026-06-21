# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest57802():
    field_value = request.form.get('field', '')
    data = ' '.join(str(field_value).split())
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
