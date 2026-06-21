# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest16709():
    origin_value = request.headers.get('Origin', '')
    parts = []
    for token in str(origin_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
