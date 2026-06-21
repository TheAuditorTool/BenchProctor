# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest67697():
    raw_body = request.get_data(as_text=True)
    data = str(raw_body).replace('\x00', '')
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
