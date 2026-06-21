# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest50748():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
