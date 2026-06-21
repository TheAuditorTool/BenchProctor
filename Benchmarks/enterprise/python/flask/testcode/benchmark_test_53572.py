# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest53572():
    upload_name = request.files['upload'].filename
    data = ' '.join(str(upload_name).split())
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
