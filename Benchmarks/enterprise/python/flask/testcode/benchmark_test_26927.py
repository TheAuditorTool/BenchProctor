# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest26927():
    upload_name = request.files['upload'].filename
    def normalize(value):
        return value.strip()
    data = normalize(upload_name)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
