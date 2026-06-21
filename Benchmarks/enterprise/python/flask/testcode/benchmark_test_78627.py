# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import unquote
from flask import request


def BenchmarkTest78627():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
