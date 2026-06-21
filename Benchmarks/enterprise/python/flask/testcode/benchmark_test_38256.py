# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest38256():
    xml_value = request.get_data(as_text=True)
    data = xml_value if xml_value else 'default'
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
