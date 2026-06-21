# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest68600():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
