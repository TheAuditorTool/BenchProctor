# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest26112():
    user_id = request.args.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
