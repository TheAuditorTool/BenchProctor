# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest01480():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = f'{forwarded_ip:.200s}'
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
