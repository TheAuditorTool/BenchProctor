# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest26668():
    raw_body = request.get_data(as_text=True)
    data, _sep, _rest = str(raw_body).partition('\x00')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
