# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest09326():
    origin_value = request.headers.get('Origin', '')
    data = (lambda v: v.strip())(origin_value)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
