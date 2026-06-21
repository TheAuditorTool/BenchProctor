# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest10324():
    auth_header = request.headers.get('Authorization', '')
    data = (lambda v: v.strip())(auth_header)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
