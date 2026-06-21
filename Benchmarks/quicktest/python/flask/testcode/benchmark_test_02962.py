# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest02962():
    origin_value = request.headers.get('Origin', '')
    data = f'{origin_value:.200s}'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
