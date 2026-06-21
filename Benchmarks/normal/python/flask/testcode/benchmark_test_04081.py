# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest04081():
    field_value = request.form.get('field', '')
    data = '%s' % str(field_value)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
