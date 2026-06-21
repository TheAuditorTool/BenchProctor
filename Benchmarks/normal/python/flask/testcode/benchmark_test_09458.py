# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest09458():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    with open('/var/app/data/' + str(forwarded_ip), 'r') as fh:
        content = fh.read()
    return content
