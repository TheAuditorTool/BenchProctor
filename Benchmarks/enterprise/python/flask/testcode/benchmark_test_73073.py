# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest73073():
    upload_name = request.files['upload'].filename
    data = f'{upload_name:.200s}'
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
