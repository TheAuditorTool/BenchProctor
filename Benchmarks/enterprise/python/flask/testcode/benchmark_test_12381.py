# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request
import json


def BenchmarkTest12381():
    upload_name = request.files['upload'].filename
    try:
        data = json.loads(upload_name).get('value', upload_name)
    except (json.JSONDecodeError, AttributeError):
        data = upload_name
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
