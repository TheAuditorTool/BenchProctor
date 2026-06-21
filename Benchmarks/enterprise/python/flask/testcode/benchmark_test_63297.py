# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest63297():
    multipart_value = request.form.get('multipart_field', '')
    data, _sep, _rest = str(multipart_value).partition('\x00')
    return str(data), 200, {'Content-Type': 'text/html'}
