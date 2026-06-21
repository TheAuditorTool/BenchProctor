# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest04010():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data, _sep, _rest = str(forwarded_ip).partition('\x00')
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
