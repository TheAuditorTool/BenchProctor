# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest10685():
    upload_name = request.files['upload'].filename
    data = '%s' % (upload_name,)
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
