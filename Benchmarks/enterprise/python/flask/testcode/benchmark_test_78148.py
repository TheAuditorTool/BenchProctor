# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest78148():
    raw_body = request.get_data(as_text=True)
    data = ' '.join(str(raw_body).split())
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
