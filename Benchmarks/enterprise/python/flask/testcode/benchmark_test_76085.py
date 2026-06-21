# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest76085():
    upload_name = request.files['upload'].filename
    data = (lambda v: v.strip())(upload_name)
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
