# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest66760():
    referer_value = request.headers.get('Referer', '')
    if referer_value:
        data = referer_value
    else:
        data = ''
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
