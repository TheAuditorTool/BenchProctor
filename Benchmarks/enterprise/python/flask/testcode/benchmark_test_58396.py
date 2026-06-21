# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest58396():
    field_value = request.form.get('field', '')
    data = f'{field_value:.200s}'
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
