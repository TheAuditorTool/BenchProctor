# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest66529():
    multipart_value = request.form.get('multipart_field', '')
    with open('/var/app/data/' + str(multipart_value), 'r') as fh:
        content = fh.read()
    return content
