# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request


def BenchmarkTest09525():
    multipart_value = request.form.get('multipart_field', '')
    data = unquote(multipart_value)
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
