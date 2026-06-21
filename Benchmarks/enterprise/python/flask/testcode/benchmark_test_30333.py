# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest30333():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = '{}'.format(forwarded_ip)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
