# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest22184():
    raw_body = request.get_data(as_text=True)
    normalized = unicodedata.normalize('NFKC', str(raw_body))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
