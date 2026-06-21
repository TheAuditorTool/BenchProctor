# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest50710():
    cookie_value = request.cookies.get('session_token', '')
    parts = str(cookie_value).split(',')
    data = ','.join(parts)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
