# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest50887():
    raw_body = request.get_data(as_text=True)
    data = raw_body if raw_body else 'default'
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
