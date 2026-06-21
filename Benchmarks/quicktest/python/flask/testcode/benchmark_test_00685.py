# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest00685():
    multipart_value = request.form.get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
