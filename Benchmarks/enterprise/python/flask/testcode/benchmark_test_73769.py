# SPDX-License-Identifier: Apache-2.0
import os
from flask import request


def BenchmarkTest73769():
    multipart_value = request.form.get('multipart_field', '')
    checked_path = os.path.join('/var/app/data', os.path.basename(multipart_value))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
