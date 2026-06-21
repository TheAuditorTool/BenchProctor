# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest32961():
    multipart_value = request.form.get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
