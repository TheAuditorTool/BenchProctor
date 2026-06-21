# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest10530():
    host_value = request.headers.get('Host', '')
    data = (lambda v: v.strip())(host_value)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
