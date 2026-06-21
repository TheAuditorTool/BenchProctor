# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest51640():
    origin_value = request.headers.get('Origin', '')
    reader = make_reader(origin_value)
    data = reader()
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
