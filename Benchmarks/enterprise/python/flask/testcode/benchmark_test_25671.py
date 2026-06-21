# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest25671():
    referer_value = request.headers.get('Referer', '')
    return '<script src="' + str(referer_value) + '"></script>', 200, {'Content-Type': 'text/html'}
