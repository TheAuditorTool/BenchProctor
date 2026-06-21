# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest37686():
    raw_body = request.get_data(as_text=True)
    data = f'{raw_body:.200s}'
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
