# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest46132():
    upload_name = request.files['upload'].filename
    prefix = ''
    data = prefix + str(upload_name)
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
