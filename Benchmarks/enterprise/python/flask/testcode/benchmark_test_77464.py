# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest77464():
    field_value = request.form.get('field', '')
    parts = str(field_value).split(',')
    data = ','.join(parts)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
