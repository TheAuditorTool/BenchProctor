# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest36865():
    raw_body = request.get_data(as_text=True)
    if raw_body:
        data = raw_body
    else:
        data = ''
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
