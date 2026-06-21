# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest36452():
    raw_body = request.get_data(as_text=True)
    parts = str(raw_body).split(',')
    data = ','.join(parts)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
