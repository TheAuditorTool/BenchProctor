# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest41657():
    upload_name = request.files['upload'].filename
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
