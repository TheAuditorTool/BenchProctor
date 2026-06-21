# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest40882():
    multipart_value = request.form.get('multipart_field', '')
    data = '%s' % str(multipart_value)
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
