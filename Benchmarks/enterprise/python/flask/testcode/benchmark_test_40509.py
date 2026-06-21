# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest40509():
    raw_body = request.get_data(as_text=True)
    data = '%s' % (raw_body,)
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
