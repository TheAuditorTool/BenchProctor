# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest22614():
    referer_value = request.headers.get('Referer', '')
    data = (lambda v: v.strip())(referer_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
