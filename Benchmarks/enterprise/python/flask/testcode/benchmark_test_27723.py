# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest27723():
    host_value = request.headers.get('Host', '')
    data = str(host_value).replace('\x00', '')
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
