# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest00920():
    user_id = request.args.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
