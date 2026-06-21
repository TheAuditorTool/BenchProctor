# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest09130():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header:.200s}'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
