# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest35729():
    raw_body = request.get_data(as_text=True)
    data = raw_body if raw_body else 'default'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
