# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request
import os


def BenchmarkTest21197():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
