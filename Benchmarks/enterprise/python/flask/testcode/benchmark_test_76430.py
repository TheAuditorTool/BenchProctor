# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest76430():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % (header_value,)
    return str(data), 200, {'Content-Type': 'text/html'}
