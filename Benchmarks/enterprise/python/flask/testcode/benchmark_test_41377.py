# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest41377():
    multipart_value = request.form.get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
