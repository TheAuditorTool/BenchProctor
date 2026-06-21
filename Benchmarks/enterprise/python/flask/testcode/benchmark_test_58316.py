# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request


def BenchmarkTest58316():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    return str(data), 200, {'Content-Type': 'text/html'}
