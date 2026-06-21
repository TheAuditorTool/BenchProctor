# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest20685():
    user_id = request.args.get('id', '')
    prefix = ''
    data = prefix + str(user_id)
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
