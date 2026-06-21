# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest38521():
    host_value = request.headers.get('Host', '')
    return '<!-- diagnostic build token: ' + str(host_value) + ' -->', 200, {'Content-Type': 'text/html'}
