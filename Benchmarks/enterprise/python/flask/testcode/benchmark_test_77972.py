# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest77972():
    xml_value = request.get_data(as_text=True)
    data = f'{xml_value:.200s}'
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
