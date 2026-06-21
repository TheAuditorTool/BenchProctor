# SPDX-License-Identifier: Apache-2.0
from flask import request


def relay_value(value):
    return value

def BenchmarkTest33838():
    upload_name = request.files['upload'].filename
    data = relay_value(upload_name)
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
