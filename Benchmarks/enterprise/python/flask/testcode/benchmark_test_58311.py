# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest58311():
    auth_header = request.headers.get('Authorization', '')
    data = bytes.fromhex(auth_header).decode('utf-8', 'ignore')
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
