# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest33561():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    prefix = ''
    data = prefix + str(forwarded_ip)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
