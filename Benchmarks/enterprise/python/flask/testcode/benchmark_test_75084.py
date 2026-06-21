# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest75084():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % (referer_value,)
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
