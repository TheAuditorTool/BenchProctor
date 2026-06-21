# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest76882():
    field_value = request.form.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
