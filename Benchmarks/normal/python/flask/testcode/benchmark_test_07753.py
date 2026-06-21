# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest07753():
    referer_value = request.headers.get('Referer', '')
    parts = str(referer_value).split(',')
    data = ','.join(parts)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
