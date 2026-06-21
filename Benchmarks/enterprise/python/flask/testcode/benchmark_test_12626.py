# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest12626():
    referer_value = request.headers.get('Referer', '')
    prefix = ''
    data = prefix + str(referer_value)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
