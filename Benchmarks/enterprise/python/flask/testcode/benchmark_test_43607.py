# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest43607():
    multipart_value = request.form.get('multipart_field', '')
    data = multipart_value if multipart_value else 'default'
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
