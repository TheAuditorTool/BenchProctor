# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest23699():
    user_id = request.args.get('id', '')
    data = (lambda v: v.strip())(user_id)
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
