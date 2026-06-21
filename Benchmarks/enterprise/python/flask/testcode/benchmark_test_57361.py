# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request
import json


def BenchmarkTest57361():
    multipart_value = request.form.get('multipart_field', '')
    try:
        data = json.loads(multipart_value).get('value', multipart_value)
    except (json.JSONDecodeError, AttributeError):
        data = multipart_value
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
