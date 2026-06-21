# SPDX-License-Identifier: Apache-2.0
import os
from flask import request


def BenchmarkTest48083():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
