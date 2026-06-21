# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest05151():
    xml_value = request.get_data(as_text=True)
    data = '{}'.format(xml_value)
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
