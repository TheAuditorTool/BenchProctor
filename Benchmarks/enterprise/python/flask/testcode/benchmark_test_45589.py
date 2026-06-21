# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest45589():
    cookie_value = request.cookies.get('session_token', '')
    data = '{}'.format(cookie_value)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
