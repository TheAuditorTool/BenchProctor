# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request


def BenchmarkTest58276():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    return str(data), 200, {'Content-Type': 'text/html'}
