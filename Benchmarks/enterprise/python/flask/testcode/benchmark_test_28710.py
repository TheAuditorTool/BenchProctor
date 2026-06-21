# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest28710():
    host_value = request.headers.get('Host', '')
    with open('/var/app/data/' + str(host_value), 'r') as fh:
        content = fh.read()
    return content
