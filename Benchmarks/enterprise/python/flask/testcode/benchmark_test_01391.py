# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest01391():
    origin_value = request.headers.get('Origin', '')
    data = '{}'.format(origin_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
