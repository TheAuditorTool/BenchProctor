# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest19101():
    upload_name = request.files['upload'].filename
    data = str(upload_name).replace('\x00', '')
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
