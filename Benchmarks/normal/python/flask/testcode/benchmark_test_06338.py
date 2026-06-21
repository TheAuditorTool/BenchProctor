# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest06338():
    upload_name = request.files['upload'].filename
    return str(upload_name), 200, {'Content-Type': 'text/html'}
