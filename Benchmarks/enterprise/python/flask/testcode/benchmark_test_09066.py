# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest09066():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
