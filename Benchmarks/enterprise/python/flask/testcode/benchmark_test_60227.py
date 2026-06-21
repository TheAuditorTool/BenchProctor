# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest60227():
    upload_name = request.files['upload'].filename
    data = '%s' % (upload_name,)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
