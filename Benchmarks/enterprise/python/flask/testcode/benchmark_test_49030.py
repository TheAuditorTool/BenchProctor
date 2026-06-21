# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest49030():
    referer_value = request.headers.get('Referer', '')
    data = str(referer_value).replace('\x00', '')
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
