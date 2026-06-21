# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest71399():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value:.200s}'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
