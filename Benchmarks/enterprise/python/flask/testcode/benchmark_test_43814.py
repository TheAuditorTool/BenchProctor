# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest43814():
    upload_name = request.files['upload'].filename
    return str(upload_name), 200, {'Content-Type': 'text/html'}
