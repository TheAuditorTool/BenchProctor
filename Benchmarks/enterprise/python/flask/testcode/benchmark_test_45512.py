# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest45512():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = '%s' % str(forwarded_ip)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
