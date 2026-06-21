# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest04463():
    multipart_value = request.form.get('multipart_field', '')
    data, _sep, _rest = str(multipart_value).partition('\x00')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
