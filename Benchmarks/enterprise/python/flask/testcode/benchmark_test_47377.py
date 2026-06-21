# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest47377():
    field_value = request.form.get('field', '')
    parts = str(field_value).split(',')
    data = ','.join(parts)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
