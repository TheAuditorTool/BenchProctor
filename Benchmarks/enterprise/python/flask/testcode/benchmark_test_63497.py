# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest63497():
    upload_name = request.files['upload'].filename
    data = f'{upload_name:.200s}'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
