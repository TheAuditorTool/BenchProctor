# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest64228():
    host_value = request.headers.get('Host', '')
    data = f'{host_value:.200s}'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
