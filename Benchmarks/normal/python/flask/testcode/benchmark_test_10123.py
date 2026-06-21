# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest10123():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value}'
    return str(data), 200, {'Content-Type': 'text/html'}
