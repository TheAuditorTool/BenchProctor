# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest00842():
    upload_name = request.files['doc'].filename
    data, _sep, _rest = str(upload_name).partition('\x00')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
