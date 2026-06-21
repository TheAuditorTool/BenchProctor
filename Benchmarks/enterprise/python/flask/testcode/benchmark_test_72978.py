# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest72978():
    upload_name = request.files['upload'].filename
    data = (lambda v: v.strip())(upload_name)
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
