# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest62572():
    referer_value = request.headers.get('Referer', '')
    if referer_value:
        data = referer_value
    else:
        data = ''
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
