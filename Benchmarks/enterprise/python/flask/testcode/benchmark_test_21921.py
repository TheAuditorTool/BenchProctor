# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest21921():
    header_value = request.headers.get('X-Custom-Header', '')
    if header_value:
        data = header_value
    else:
        data = ''
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
