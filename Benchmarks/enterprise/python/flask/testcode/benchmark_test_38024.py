# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest38024():
    field_value = request.form.get('field', '')
    data = f'{field_value:.200s}'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
