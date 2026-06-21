# SPDX-License-Identifier: Apache-2.0
import os
from flask import request


def BenchmarkTest56811():
    multipart_value = request.form.get('multipart_field', '')
    data = '%s' % (multipart_value,)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
