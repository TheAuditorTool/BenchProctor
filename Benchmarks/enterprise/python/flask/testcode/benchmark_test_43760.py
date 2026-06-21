# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest43760():
    field_value = request.form.get('field', '')
    data = '%s' % (field_value,)
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
