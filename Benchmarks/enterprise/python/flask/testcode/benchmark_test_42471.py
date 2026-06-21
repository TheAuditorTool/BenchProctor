# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest42471():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % str(auth_header)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
