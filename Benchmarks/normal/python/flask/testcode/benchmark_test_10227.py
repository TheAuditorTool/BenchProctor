# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest10227():
    upload_name = request.files['upload'].filename
    def normalize(value):
        return value.strip()
    data = normalize(upload_name)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
