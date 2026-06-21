# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest80946():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value:.200s}'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
