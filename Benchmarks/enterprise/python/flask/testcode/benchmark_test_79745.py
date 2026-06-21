# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest79745():
    xml_value = request.get_data(as_text=True)
    data = str(xml_value).replace('\x00', '')
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
