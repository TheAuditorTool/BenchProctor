# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request
import unicodedata


def BenchmarkTest24236():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
