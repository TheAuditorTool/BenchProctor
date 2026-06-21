# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest49847():
    multipart_value = request.form.get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
