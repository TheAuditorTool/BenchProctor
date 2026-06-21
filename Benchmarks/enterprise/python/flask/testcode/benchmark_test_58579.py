# SPDX-License-Identifier: Apache-2.0
import os
from flask import request


def BenchmarkTest58579():
    field_value = request.form.get('field', '')
    data = (lambda v: v.strip())(field_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
