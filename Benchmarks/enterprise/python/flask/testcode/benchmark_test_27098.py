# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest27098():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = forwarded_ip if forwarded_ip else 'default'
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
