# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest05601():
    upload_name = request.files['upload'].filename
    data = str(upload_name).replace('\x00', '')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
