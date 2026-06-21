# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest74851():
    user_id = request.args.get('id', '')
    data = user_id if user_id else 'default'
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
