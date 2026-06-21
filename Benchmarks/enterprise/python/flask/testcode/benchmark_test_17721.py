# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest17721():
    multipart_value = request.form.get('multipart_field', '')
    data = multipart_value if multipart_value else 'default'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
