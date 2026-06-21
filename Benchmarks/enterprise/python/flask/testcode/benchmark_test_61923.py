# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest61923():
    host_value = request.headers.get('Host', '')
    data = str(host_value).replace('\x00', '')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
