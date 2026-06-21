# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest42036():
    raw_body = request.get_data(as_text=True)
    parts = str(raw_body).split(',')
    data = ','.join(parts)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
