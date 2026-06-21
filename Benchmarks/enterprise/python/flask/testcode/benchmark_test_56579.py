# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest56579():
    cookie_value = request.cookies.get('session_token', '')
    data = bytes.fromhex(cookie_value).decode('utf-8', 'ignore')
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
