# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest71191():
    auth_header = request.headers.get('Authorization', '')
    if auth_header:
        data = auth_header
    else:
        data = ''
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
