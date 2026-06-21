# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest42401():
    multipart_value = request.form.get('multipart_field', '')
    parts = []
    for token in str(multipart_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
