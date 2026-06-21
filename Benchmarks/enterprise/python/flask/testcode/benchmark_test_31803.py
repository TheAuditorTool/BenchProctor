# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest31803():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = '%s' % str(json_value)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
