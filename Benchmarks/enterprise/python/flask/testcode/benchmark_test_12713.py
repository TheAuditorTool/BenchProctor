# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest12713():
    field_value = request.form.get('field', '')
    data = f'{field_value}'
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
