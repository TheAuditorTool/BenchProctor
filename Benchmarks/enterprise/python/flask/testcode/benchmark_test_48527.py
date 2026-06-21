# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest48527():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value:.200s}'
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
