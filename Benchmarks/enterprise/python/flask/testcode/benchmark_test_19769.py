# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest19769():
    multipart_value = request.form.get('multipart_field', '')
    data = '%s' % (multipart_value,)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
