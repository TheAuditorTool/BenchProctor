# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest66884():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = '%s' % (forwarded_ip,)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
