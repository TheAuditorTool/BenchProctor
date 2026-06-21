# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest72504():
    multipart_value = request.form.get('multipart_field', '')
    def normalize(value):
        return value.strip()
    data = normalize(multipart_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
