# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request
import json


def BenchmarkTest00356():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    try:
        data = json.loads(forwarded_ip).get('value', forwarded_ip)
    except (json.JSONDecodeError, AttributeError):
        data = forwarded_ip
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
