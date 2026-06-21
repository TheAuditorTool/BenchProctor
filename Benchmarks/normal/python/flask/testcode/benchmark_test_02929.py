# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest02929():
    upload_name = request.files['upload'].filename
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    return str(data), 200, {'Content-Type': 'text/html'}
