# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest27145():
    xml_value = request.get_data(as_text=True)
    return '<script src="' + str(xml_value) + '"></script>', 200, {'Content-Type': 'text/html'}
