# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest35521():
    auth_header = request.headers.get('Authorization', '')
    def normalize(value):
        return value.strip()
    data = normalize(auth_header)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
