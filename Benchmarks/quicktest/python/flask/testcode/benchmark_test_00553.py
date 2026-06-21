# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest00553():
    referer_value = request.headers.get('Referer', '')
    data = f'{referer_value:.200s}'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
