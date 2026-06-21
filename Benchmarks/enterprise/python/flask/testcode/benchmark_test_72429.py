# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest72429():
    multipart_value = request.form.get('multipart_field', '')
    return '<script src="' + str(multipart_value) + '"></script>', 200, {'Content-Type': 'text/html'}
