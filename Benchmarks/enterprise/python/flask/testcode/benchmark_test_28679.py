# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest28679():
    raw_body = request.get_data(as_text=True)
    return '<!-- diagnostic build token: ' + str(raw_body) + ' -->', 200, {'Content-Type': 'text/html'}
