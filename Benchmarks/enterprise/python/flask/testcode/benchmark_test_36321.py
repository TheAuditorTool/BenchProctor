# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest36321():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % str(header_value)
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
