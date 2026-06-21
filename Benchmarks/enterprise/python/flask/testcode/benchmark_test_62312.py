# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest62312():
    auth_header = request.headers.get('Authorization', '')
    reader = make_reader(auth_header)
    data = reader()
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
