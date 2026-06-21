# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest38946():
    field_value = request.form.get('field', '')
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
