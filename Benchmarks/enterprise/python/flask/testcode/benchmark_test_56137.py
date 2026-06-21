# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest56137():
    origin_value = request.headers.get('Origin', '')
    parts = str(origin_value).split(',')
    data = ','.join(parts)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
