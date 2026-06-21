# SPDX-License-Identifier: Apache-2.0
import requests
import base64
from flask import request


def BenchmarkTest11114():
    auth_header = request.headers.get('Authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
