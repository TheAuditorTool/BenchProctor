# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest69762():
    upload_name = request.files['upload'].filename
    parts = []
    for token in str(upload_name).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
