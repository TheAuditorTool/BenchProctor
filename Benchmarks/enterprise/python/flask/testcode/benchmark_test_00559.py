# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest00559():
    header_value = request.headers.get('X-Custom-Header', '')
    def normalize(value):
        return value.strip()
    data = normalize(header_value)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
