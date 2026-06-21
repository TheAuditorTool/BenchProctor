# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest05585():
    user_id = request.args.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(user_id)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
