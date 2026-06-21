# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest43979():
    multipart_value = request.form.get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    return str(data), 200, {'Content-Type': 'text/html'}
