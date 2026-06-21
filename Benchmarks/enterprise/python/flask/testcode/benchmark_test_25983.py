# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest25983():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = ' '.join(str(forwarded_ip).split())
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
