# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest00082():
    referer_value = request.headers.get('Referer', '')
    with open('/var/app/data/' + str(referer_value), 'r') as fh:
        content = fh.read()
    return content
