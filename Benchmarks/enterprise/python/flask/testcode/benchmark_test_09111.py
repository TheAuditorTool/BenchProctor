# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest09111():
    upload_name = request.files['upload'].filename
    return '<!-- diagnostic build token: ' + str(upload_name) + ' -->', 200, {'Content-Type': 'text/html'}
