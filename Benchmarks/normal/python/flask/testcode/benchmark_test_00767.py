# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request


def BenchmarkTest00767():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
