# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest80501():
    referer_value = request.headers.get('Referer', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
