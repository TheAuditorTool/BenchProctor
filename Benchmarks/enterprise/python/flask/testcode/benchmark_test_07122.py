# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest07122():
    referer_value = request.headers.get('Referer', '')
    return str(referer_value), 200, {'Content-Type': 'text/html'}
