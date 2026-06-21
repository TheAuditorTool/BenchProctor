# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest62549():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    reader = make_reader(forwarded_ip)
    data = reader()
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
