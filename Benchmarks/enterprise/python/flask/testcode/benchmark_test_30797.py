# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest30797():
    host_value = request.headers.get('Host', '')
    data = f'{host_value:.200s}'
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
