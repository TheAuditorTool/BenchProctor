# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def coalesce_blank(value):
    return value or ''

def BenchmarkTest65977():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = coalesce_blank(forwarded_ip)
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
