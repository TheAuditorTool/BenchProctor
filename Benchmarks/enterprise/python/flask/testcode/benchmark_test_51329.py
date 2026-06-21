# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest51329():
    upload_name = request.files['upload'].filename
    data = f'{upload_name:.200s}'
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
