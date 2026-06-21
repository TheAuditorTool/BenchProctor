# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest07457():
    user_id = request.args.get('id', '')
    data = ' '.join(str(user_id).split())
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
