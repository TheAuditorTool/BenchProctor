# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest75989():
    multipart_value = request.form.get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
