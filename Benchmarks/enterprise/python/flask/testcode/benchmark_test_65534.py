# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest65534():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = f'{forwarded_ip:.200s}'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
