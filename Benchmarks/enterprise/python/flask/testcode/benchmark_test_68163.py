# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest68163():
    xml_value = request.get_data(as_text=True)
    data = xml_value if xml_value else 'default'
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
