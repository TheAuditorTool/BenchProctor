# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest48132():
    host_value = request.headers.get('Host', '')
    parts = str(host_value).split(',')
    data = ','.join(parts)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
