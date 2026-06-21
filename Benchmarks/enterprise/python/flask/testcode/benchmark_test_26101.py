# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest26101():
    upload_name = request.files['upload'].filename
    parts = []
    for token in str(upload_name).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
