# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest13351():
    host_value = request.headers.get('Host', '')
    data, _sep, _rest = str(host_value).partition('\x00')
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
