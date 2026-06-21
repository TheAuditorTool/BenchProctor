# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest40988():
    upload_name = request.files['upload'].filename
    if upload_name:
        data = upload_name
    else:
        data = ''
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
