# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest13167():
    multipart_value = request.form.get('multipart_field', '')
    data = '%s' % (multipart_value,)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
