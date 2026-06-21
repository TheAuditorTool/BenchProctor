# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest06077():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % str(header_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
