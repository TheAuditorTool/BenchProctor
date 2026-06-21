# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest28333():
    user_id = request.args.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
