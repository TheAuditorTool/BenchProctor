# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest10231():
    xml_value = request.get_data(as_text=True)
    data, _sep, _rest = str(xml_value).partition('\x00')
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
