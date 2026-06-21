# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest69595():
    user_id = request.args.get('id', '')
    data = str(user_id).replace('\x00', '')
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
