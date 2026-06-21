# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest64442():
    header_value = request.headers.get('X-Custom-Header', '')
    data = str(header_value).replace('\x00', '')
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
