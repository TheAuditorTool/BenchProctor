# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest30979():
    user_id = request.args.get('id', '')
    data = user_id if user_id else 'default'
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
