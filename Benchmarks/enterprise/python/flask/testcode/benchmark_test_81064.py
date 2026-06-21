# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest81064():
    raw_body = request.get_data(as_text=True)
    data = raw_body if raw_body else 'default'
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
