# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import unquote
from flask import request


def BenchmarkTest19437():
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
