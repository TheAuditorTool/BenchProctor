# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest19982():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % (referer_value,)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
