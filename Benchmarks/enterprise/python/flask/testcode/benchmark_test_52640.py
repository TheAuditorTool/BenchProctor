# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest52640():
    origin_value = request.headers.get('Origin', '')
    def normalize(value):
        return value.strip()
    data = normalize(origin_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
