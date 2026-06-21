# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest68332():
    referer_value = request.headers.get('Referer', '')
    prefix = ''
    data = prefix + str(referer_value)
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
