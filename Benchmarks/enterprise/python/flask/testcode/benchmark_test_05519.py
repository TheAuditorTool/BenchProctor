# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest05519():
    host_value = request.headers.get('Host', '')
    prefix = ''
    data = prefix + str(host_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
