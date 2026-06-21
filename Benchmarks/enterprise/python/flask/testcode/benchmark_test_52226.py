# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest52226():
    upload_name = request.files['upload'].filename
    return '<script src="' + str(upload_name) + '"></script>', 200, {'Content-Type': 'text/html'}
