# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest80738():
    xml_value = request.get_data(as_text=True)
    kind = 'json' if str(xml_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = xml_value
            data = parsed
        case _:
            data = xml_value
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
