# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest39987():
    upload_name = request.files['upload'].filename
    if upload_name:
        data = upload_name
    else:
        data = ''
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
