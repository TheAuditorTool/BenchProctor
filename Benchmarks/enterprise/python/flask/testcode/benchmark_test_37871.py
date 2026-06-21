# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest37871():
    auth_header = request.headers.get('Authorization', '')
    data, _sep, _rest = str(auth_header).partition('\x00')
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
