# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest45701():
    host_value = request.headers.get('Host', '')
    reader = make_reader(host_value)
    data = reader()
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
