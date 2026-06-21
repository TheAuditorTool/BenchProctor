# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest46700():
    raw_body = request.get_data(as_text=True)
    data = f'{raw_body}'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
