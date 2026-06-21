# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest11820():
    host_value = request.headers.get('Host', '')
    data = ' '.join(str(host_value).split())
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
