# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest21323():
    upload_name = request.files['doc'].filename
    data = ' '.join(str(upload_name).split())
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
