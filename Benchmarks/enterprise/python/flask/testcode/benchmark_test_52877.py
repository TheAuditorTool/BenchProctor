# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest52877():
    upload_name = request.files['upload'].filename
    with open('/var/app/data/' + str(upload_name), 'r') as fh:
        content = fh.read()
    return content
