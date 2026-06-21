# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest03523():
    referer_value = request.headers.get('Referer', '')
    data = ' '.join(str(referer_value).split())
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
