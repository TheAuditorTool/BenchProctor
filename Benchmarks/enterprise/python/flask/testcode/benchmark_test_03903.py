# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest03903():
    origin_value = request.headers.get('Origin', '')
    return '<script src="' + str(origin_value) + '"></script>', 200, {'Content-Type': 'text/html'}
