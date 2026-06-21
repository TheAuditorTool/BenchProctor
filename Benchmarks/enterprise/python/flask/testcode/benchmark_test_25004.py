# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest25004():
    upload_name = request.files['upload'].filename
    data = upload_name if upload_name else 'default'
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
