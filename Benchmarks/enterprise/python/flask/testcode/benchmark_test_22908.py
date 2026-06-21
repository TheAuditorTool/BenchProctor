# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def normalise_input(value):
    return value.strip()

def BenchmarkTest22908():
    xml_value = request.get_data(as_text=True)
    data = normalise_input(xml_value)
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
