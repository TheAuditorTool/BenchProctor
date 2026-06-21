# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest27106():
    referer_value = request.headers.get('Referer', '')
    def normalize(value):
        return value.strip()
    data = normalize(referer_value)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
