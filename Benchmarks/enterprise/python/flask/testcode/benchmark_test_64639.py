# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest64639():
    raw_body = request.get_data(as_text=True)
    data = (lambda v: v.strip())(raw_body)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
